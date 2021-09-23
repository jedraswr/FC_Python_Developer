# import and initiations:
from flask import Flask
app = Flask(__name__)

# Managing:

class Manager:
    def __init__(self):
        self.callbacks = {}
        self.balance = 0
        self.warehouse = {}
        self.actions = []
        self.review = []
        self.warning_msg = ""
        self.block_writing = 0

    def set(self, procedure):
        def decorate(callback):
            self.callbacks[procedure] = callback
        return decorate

    def do_that(self, procedure, trans_args):
        if procedure in self.callbacks:
            self.callbacks[procedure](trans_args)
        else:
            warning_msg = ("Nie ma takiej procedury!")
        return warning_msg

mng = Manager()

# Operations:

@mng.set("saldo")
def trans_cash(trans_args):
    warning_msg = ""
    amount = int(trans_args[0])
    description = trans_args[1]
    if mng.balance + amount < 0:
        warning_msg = ("Transakcja saldo pominięta: kwota przekroczy stan konta")
    else:
        mng.balance += amount
        action = ["saldo", amount, description]
        mng.actions.append(action)
        new_trans = 'saldo '+str(amount)+' '+description
        add_trans(new_trans)
    mng.warning_msg = warning_msg

@mng.set("zakup")
def trans_supply(trans_args):
    warning_msg = ""
    goods_id = trans_args[0]
    number = int(trans_args[1])
    price = int(trans_args[2])
    amount = number * price
    if mng.balance - amount < 0:
        warning_msg = ("Transakcja zakup odrzucona: kwota przekroczy stan konta")
    else:
        mng.balance -= amount
        if goods_id not in mng.warehouse:
            mng.warehouse[goods_id] = number
        else:
            mng.warehouse[goods_id] += number
        action = ["zakup", goods_id, number, price]
        mng.actions.append(action)
        new_trans = 'zakup ' + goods_id + ' ' + str(number) + ' ' + str(price)
        add_trans(new_trans)
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
            new_trans = 'sprzedaz ' + goods_id + ' ' + str(number) + ' ' + str(price)
            add_trans(new_trans)
    mng.warning_msg = warning_msg

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

def add_trans(new_trans):
    if mng.block_writing == 0:
        with open("input.txt", "a", encoding="utf-8") as it:
            it.write(new_trans)
            it.write('\n')


