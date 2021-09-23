# Initiations:
import os
from accountant import mng
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
warning_msg = ""

# Starting procedures:
if not os.path.isfile("input.txt"):         #sprawdzanie pliku z danymi
    warning_msg = ("Nie znaleziono pliku wejściowego.")   
    exit()
outputfile = open("output.txt", "w")        #czyszczenie pliku output
outputfile.close()

# Data entry from import file:
mng.block_writing = 1
import_file = open("input.txt", "r", encoding="utf-8")
for line in import_file:
    transaction = line.replace("\n", "").split(" ")
    procedure = transaction[0]
    trans_args = transaction[1:]
    mng.callbacks[procedure](trans_args)
mng.block_writing = 0

@app.route("/", methods=["POST", "GET"])
def main_forms():
    warning_msg = ""
    if request.method == "POST":
        response = dict(request.form)
        procedure = response["procedure"]
        if procedure == 'saldo':
            amount = response["amount"]
            description = response["description"]
            trans_args = [amount, description]
            mng.callbacks[procedure](trans_args)
        else:
            goods_id = response["goods_id"]
            number = response["number"]
            price = response["price"]
            trans_args = [goods_id, number, price]
            mng.callbacks[procedure](trans_args)
        return redirect("/")
    return render_template("index.html", warning_msg=mng.warning_msg, balance=mng.balance,
                           warehouse=mng.warehouse)

@app.route("/historia/", methods=["POST", "GET"])
def hist_forms():
    if request.method == "POST":
        response = dict(request.form)
        procedure = response["procedure"]
        if procedure == 'przeglad':
            nr_start = response["nr_start"]
            if nr_start == "":
                nr_start = 0
            nr_end = response["nr_end"]
            if nr_end == "":
                nr_end = 999999
            trans_args = [nr_start, nr_end]
            mng.callbacks[procedure](trans_args)
    return render_template("historia.html", balance=mng.balance, warehouse=mng.warehouse, review=mng.review)

