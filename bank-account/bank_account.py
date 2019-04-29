import threading

class BankAccount(object):
    def __init__(self):
        self.is_open = False
        self.balance = 0
        self.lock = threading.Lock()

    def get_balance(self):
        with self.lock:
            if self.is_open:
                return self.balance
            else:
                raise ValueError('cannot check balance of closed account')

    def open(self):
        if not self.is_open:
            self.is_open = True
            self.balance = 0
        else:
            raise ValueError('cannot open already opened account')


    def deposit(self, amount):
        with self.lock:
            if self.is_open and amount>0:
                self.balance += amount
            else:
                raise ValueError('cannot deposit in closed account')

    def withdraw(self, amount):
        with self.lock:
            if self.is_open and amount > 0 and amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError('cannot withdraw from closed account or amount > to balance')

    def close(self):
        if self.is_open:
            self.is_open = False
        else:
            raise ValueError('cannot close already closed account')
