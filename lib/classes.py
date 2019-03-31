class Bank:
    def __init__(self, name, accounts, credit_cards, investments, bills, transactions):
        self.name = name
        self.accounts = accounts
        self.credit_cards = credit_cards
        self.investments = investments
        self.bills = bills
        self.transactions = transactions


class Account:
    def __init__(self, name, currency, balance, last_transactions, number):
        self.name = name
        self.currency = currency
        self.balance = balance
        self.last_transaction = last_transactions
        self.number = number


class CreditCard:
    def __init__(self, cc_type, card_number, max_payment, min_payment, due_date, close_date):
        self.cc_type = cc_type
        self.card_number = card_number
        self.max_payment = max_payment
        self.min_payment = min_payment
        self.close_date = close_date
        self.due_date = due_date


class Bill:
    def __init__(self, name, due_date, amount):
        self.name = name
        self.due_date = due_date
        self.amount = amount


class Transaction:
    def __init__(self, description, date, amount, bank_name):
        self.description = description
        self.date = date
        self.amount = amount
        self.bank_name = bank_name


class Investment:
    def __init__(self, name, currency, type, balance):
        self.name = name
        self.currency = currency
        self.type = type
        self.balance = balance


class Date:
    def __init__(self, day, month):
        self.day = day
        self.month = month

    def print_date(self):
        res = ""
        if self.day < 10:
            res = "0" + str(self.day)
        else:
            res = str(self.day)
        res = res + "/"
        if self.month < 10:
            res = res + "0" + str(self.month)
        else:
            res = res + str(self.month)
        return res

    def __lt__(self, other):
        if self.month < other.month:
            return self.month < other.month
        if self.month > other.month:
            return other.month > self.month
        if self.day < other.day:
            return self.day < other.day
        else:
            return other.month > self.month
