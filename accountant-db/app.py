# Initiations:
import os
import datetime
from accountant import mng
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///accountant.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
trans_date = datetime.date.today()
warning_msg = ""
action = []

class Warehouse(db.Model):
    goods_id = db.Column(db.String(50), primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=False)

class Transactions(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, unique=False)
    procedure = db.Column(db.String(15), nullable=False, unique=False)
    amount = db.Column(db.Integer, nullable=True, unique=False)
    description = db.Column(db.String(50), nullable=True, unique=False)
    goods_id = db.Column(db.String(20), nullable=True, unique=False)
    number = db.Column(db.Integer, nullable=True, unique=False)
    price = db.Column(db.Integer, nullable=True, unique=False)

class Balance(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Integer, nullable=False, unique=False)

db.create_all()

# Data entry from import file: ### PROCEDURA AWARYJNA - ZABLOKOWANA
# mng.block_writing = 1
# import_file = open("input.txt", "r", encoding="utf-8")
# for line in import_file:
#     transaction = line.replace("\n", "").split(" ")
#     procedure = transaction[0]
#     trans_args = transaction[1:]
#     mng.callbacks[procedure](trans_args)
# mng.block_writing = 0

@mng.set("saldo")
def trans_cash(trans_args):
    warning_msg = ""
    amount = int(trans_args[0])
    description = trans_args[1]
    if mng.balance + amount < 0:
        warning_msg = ("Transakcja saldo pominięta: kwota przekroczy stan konta")
    else:                       # wpisy do managera:
        mng.balance += amount
        action = ["saldo", amount, description]
        mng.actions.append(action)
        if mng.block_add_db == 0:       # wpisy do db:
            db_transactions = Transactions(date=trans_date, procedure="saldo",
                                    amount=amount, description=description)
            db.session.add(db_transactions)
            if_balance = db.session.query(Balance).filter(Balance.pk == 1).first()
            if not if_balance:  # pierwsza transakcja
                db_balance = Balance(balance=mng.trans_db[1])
                db.session.add(db_balance)
            else:
                if_balance.balance += mng.trans_db[1]
            db.session.commit()
    mng.warning_msg = warning_msg

@mng.set("zakup")
def trans_supply(trans_args):
    warning_msg = ""
    goods_id = trans_args[0]
    number = int(trans_args[1])
    price = int(trans_args[2])
    amount = -1 * (number * price)
    if mng.balance + amount < 0:
        warning_msg = ("Transakcja zakup odrzucona: kwota przekroczy stan konta")
    else:                           # wpisy do managera:
        mng.balance += amount
        if goods_id not in mng.warehouse:
            mng.warehouse[goods_id] = number
        else:
            mng.warehouse[goods_id] += number
        action = ["zakup", goods_id, number, price]
        mng.actions.append(action)
        if mng.block_add_db == 0:       # wpisy do db:
            db_transactions = Transactions(date=trans_date, procedure="zakup",
                        goods_id=goods_id, number=number, price=price)
            db.session.add(db_transactions)
            if_product = db.session.query(Warehouse).filter(Warehouse.goods_id == goods_id).first()
            if not if_product:      # nowy towar:
                db_warehouse = Warehouse(goods_id=goods_id, number=number)
                db.session.add(db_warehouse)
            else:
                if_product.number += number
            if_balance = db.session.query(Balance).filter(Balance.pk == 1).first()
            if_balance.balance += amount
            db.session.commit()
    mng.warning_msg = warning_msg

@mng.set("sprzedaz")
def trans_sale(trans_args):
    warning_msg = ""
    goods_id = trans_args[0]
    number = int(trans_args[1])
    price = int(trans_args[2])
    if goods_id not in mng.warehouse:
        warning_msg = ("Transakcja sprzedaż odrzucona: nie ma takiego towaru")
    else:
        if number > mng.warehouse[goods_id]:
            warning_msg = ("Transakcja sprzedaż odrzucona: za mało towaru w magazynie")
        else:
            amount = (number * price)
            mng.balance += amount
            mng.warehouse[goods_id] -= number
            action = ["sprzedaz", goods_id, number, price]
            mng.actions.append(action)
            if mng.block_add_db == 0:  # wpisy do db:
                db_transactions = Transactions(date=trans_date, procedure="sprzedaz",
                                goods_id=goods_id, number=number, price=price)
                db.session.add(db_transactions)
                if_product = db.session.query(Warehouse).filter(Warehouse.goods_id == goods_id).first()
                if_product.number += number
                if_balance = db.session.query(Balance).filter(Balance.pk == 1).first()
                if_balance.balance += amount
                db.session.commit()
    mng.warning_msg = warning_msg

# Data refresh at start-up procedure:
mng.block_add_db = 1            #wyłącznik zapobiegający zdublowaniu bazy przy restarcie
prev_transactions = db.session.query(Transactions).all()
for transaction in prev_transactions:
    procedure = transaction.procedure
    amount = transaction.amount
    description = transaction.description
    goods_id = transaction.goods_id
    number = transaction.number
    price = transaction.price
    if procedure == 'saldo':
        trans_args = [amount, description]
    else:
        trans_args = [goods_id, number, price]
    mng.callbacks[procedure](trans_args)

@mng.set("przeglad")
def review(trans_args):
    mng.review = []
    nr_start = int(trans_args[0])
    nr_end = int(trans_args[1])
    nr_act = 0
    for list in mng.actions:
        nr_act += 1
        if nr_act < nr_start:
            continue
        elif nr_act > nr_end:
            continue
        else:
            mng.review.append(list)

@app.route("/", methods=["POST", "GET"])
def main_forms():
    warning_msg = ""
    if request.method == "POST":
        response = dict(request.form)
        procedure = response["procedure"]
        mng.block_add_db = 0
        # print("Z formularza {}".format(mng.block_add_db))
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
    return render_template("historia.html", balance=mng.balance, warehouse=mng.warehouse,
                           review=mng.review)
