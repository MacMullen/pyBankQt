import jsonpickle

class Bank:
    def __init__(self, name, accounts, credit_cards, investments):
        self.name = name
        self.accounts = accounts
        self.credit_cards = credit_cards
        self.investments = investments


class Account:
    def __init__(self, name, currency, balance, last_transactions, number):
        self.name = name
        self.currency = currency
        self.balance = balance
        self.last_transaction = last_transactions
        self.number = number


class CreditCard:
    def __init__(self, cc_type, card_number, max_payment, min_payment, due_date):
        self.cc_type = cc_type
        self.card_number = card_number
        self.max_payment = max_payment
        self.min_payment = min_payment
        self.due_date = due_date


class Bill:
    def __init__(self, name, due_date, amount):
        self.name = name
        self.due_date = due_date
        self.amount = amount


class Transaction:
    def __init__(self, description, date, amount):
        self.description = description
        self.date = date
        self.amount = amount


class Investment:
    def __init__(self, name, currency, type, balance):
        self.name = name
        self.currency = currency
        self.type = type
        self.balance = balance


def create_example_banks():
    transactions_account_one = []
    transactions_account_two = []
    for i in range(0, 10):
        transactions_account_one.append(Transaction("CC Payment", "20/12/19", 623.00))
    for i in range(0, 15):
        transactions_account_two.append(Transaction("Market", "12/05/19", 25.30))

    account_one = Account("Salary", "ARS", 5200.00, transactions_account_one, "XXXXXXXX6985")
    account_two = Account("Savings", "USD", 256.00, [], "XXXXXXXX1154")
    account_three = Account("Pension", "ARS", 3200.00, transactions_account_two, "XXXXXXXX6999")
    account_four = Account("Pension Savings", "ARS", 632.24, [], "XXXXXXXX6987")

    credit_card_one = CreditCard("Visa", "XXXX-XXXX-5874", 625.00, 210.00, "20/03")
    credit_card_two = CreditCard("MasterCard", "XXXX-XXXX-9857", 63.00, 3.00, "02/04")
    credit_card_three = CreditCard("MasterCard", "XXXX-XXXX-3257", 1547.00, 365.00, "03/03")
    credit_card_four = CreditCard("Visa", "XXXX-XXXX-7541", 0.00, 0.00, "15/03")

    investment_one = Investment("Bitcoin", "BTC", "Cryptocurrencies", 5000.00)
    investment_two = Investment("Certificate of Deposit", "ARS", "Banking investments", 365.00)

    bank_one = Bank("New Bank of Stormwind", [account_one, account_two, account_three],
                    [credit_card_one, credit_card_two], [investment_one])
    bank_two = Bank("Bank of Ogrimmar", [account_four], [credit_card_three, credit_card_four], [investment_two])

    return [bank_one, bank_two]
