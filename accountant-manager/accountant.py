
class Manager:
    def __init__(self):
        self.callbacks = {}
        self.balance = 0
        self.warehouse = {}
        self.actions = []
        self.log = []
        self.stocks = []

    def set(self, procedure):
        def decorate(callback):
            self.callbacks[procedure] = callback
        return decorate

    def do_that(self, procedure, trans_args):
        if procedure in self.callbacks:
            self.callbacks[procedure](trans_args)
        else:
            print("Nie ma takiej procedury!")

mng = Manager()

# Operations:

@mng.set("saldo")
def trans_cash(trans_args):
    amount = int(trans_args[0])
    description = trans_args[1]
    if mng.balance + amount < 0:
        print("Transakcja saldo {} {} pominięta: kwota przekroczy stan konta"
              .format(amount, description))
    else:
        mng.balance += amount
        action = ["saldo", amount, description]
        mng.actions.append(action)

@mng.set("zakup")
def trans_supply(trans_args):
    goods_id = trans_args[0]
    number = int(trans_args[1])
    price = int(trans_args[2])
    amount = number * price
    if mng.balance - amount < 0:
        print("Transakcja zakup {} {} {} odrzucona: kwota przekroczy stan konta"
              .format(goods_id, number, price))
    else:
        mng.balance -= amount
        if goods_id not in mng.warehouse:
            mng.warehouse[goods_id] = number
        else:
            mng.warehouse[goods_id] += number
        action = ["zakup", goods_id, number, price]
        mng.actions.append(action)

@mng.set("sprzedaz")
def trans_sale(trans_args):
    goods_id = trans_args[0]
    number = int(trans_args[1])
    price = int(trans_args[2])
    if goods_id not in mng.warehouse:
        print("Transakcja sprzedaż {} {} {} odrzucona: nie ma takiego towaru"
              .format(goods_id, number, price))
    else:
        if number > mng.warehouse[goods_id]:
            print("Transakcja sprzedaż {} {} {} odrzucona: za mało towaru w magazynie"
                .format(goods_id, number, price))
        else:
            amount = (number * price)
            mng.balance += amount
            mng.warehouse[goods_id] -= number
            action = ["sprzedaz", goods_id, number, price]
            mng.actions.append(action)

@mng.set("magazyn")
def check_stock(trans_args):
    for element in trans_args:
        if element in mng.warehouse:
            listing = [element, mng.warehouse[element]]
            mng.stocks.append(listing)
        else:
            print("Żądanie magazyn {} odrzucone: nie ma takiego towaru"
                .format(element))
