# import and initiations:

import datetime
from flask import Flask
app = Flask(__name__)
trans_date = datetime.date.today()
action = []

# Managing:

class Manager:
    def __init__(self):
        self.callbacks = {}
        self.balance = 0
        self.warehouse = {}
        self.actions = []
        self.review = []
        self.warning_msg = ""
        self.block_add_db = 1

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

