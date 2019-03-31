import pickle


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


def create_example_banks():
    transactions_account_one = []
    transactions_account_two = []
    for i in range(0, 3):
        transactions_account_one.append(Transaction("CC Payment", Date(20, 12), 623.00, "SANTANDER"))
    for i in range(0, 2):
        transactions_account_two.append(Transaction("Market", Date(12, 5), -25.30, "CHASE"))

    account_one = Account("Salary", "ARS", 5200.00, transactions_account_one, "XXXXXXXX6985")
    account_two = Account("Savings", "USD", 256.00, [], "XXXXXXXX1154")
    account_three = Account("Pension", "ARS", 3200.00, transactions_account_two, "XXXXXXXX6999")
    account_four = Account("Pension Savings", "ARS", 632.24, [], "XXXXXXXX6987")

    credit_card_one = CreditCard("Visa", "XXXX-XXXX-5874", 625.00, 210.00, Date(2, 3), "05/04")
    credit_card_two = CreditCard("MasterCard", "XXXX-XXXX-9857", 63.00, 3.00, Date(2, 4), "15/04")
    credit_card_three = CreditCard("MasterCard", "XXXX-XXXX-3257", 1547.00, 365.00, Date(13, 4), "15/03")
    credit_card_four = CreditCard("Visa", "XXXX-XXXX-7541", 0.00, 0.00, Date(4, 5), "30/03")

    investment_one = Investment("Bitcoin", "BTC", "Cryptocurrencies", 5000.00)
    investment_two = Investment("Certificate of Deposit", "ARS", "Banking investments", 365.00)
    investment_three = Investment("Bitcoin", "BTC", "Cryptocurrencies", 5000.00)
    investment_four = Investment("Certificate of Deposit", "ARS", "Banking investments", 365.00)

    bill_one = Bill("CAR INSURANCE", Date(20, 5), 800)
    bill_two = Bill("HOSPITAL", Date(19, 5), 1200)
    bill_three = Bill("ELECTRICITY", Date(2, 5), 30)
    bill_four = Bill("WATER", Date(31, 5), 555.63)
    bill_five = Bill("GAS", Date(4, 5), 28.63)

    bank_one = Bank("New Bank of Stormwind", [account_one, account_two, account_three],
                    [credit_card_one, credit_card_two], [investment_one], [bill_one, bill_two],
                    transactions_account_one)
    bank_two = Bank("Bank of Ogrimmar", [account_four], [credit_card_three, credit_card_four],
                    [investment_two, investment_three, investment_four], [bill_three, bill_four, bill_five],
                    transactions_account_two)

    pickle.dump(bank_one, open("data/save.p", "wb"))
    pickle.dump(bank_two, open("data/save2.p", "wb"))
