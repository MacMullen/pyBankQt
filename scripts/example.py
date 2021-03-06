import pickle
import os
from lib.classes import *

if __name__ == "__main__":
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
    path = os.path.abspath(".")
    os.makedirs(path + "/data", exist_ok=True)
    pickle.dump(bank_one, open(path + "/data/save.p", "wb"))
    pickle.dump(bank_two, open(path + "/data/save2.p", "wb"))
