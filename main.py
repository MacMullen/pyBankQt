from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import time
import operator
import example

#  Sources: Icons = Material Design icons by Google (https://github.com/google/material-design-icons)

bank_list = []
accounts_list = []
credit_cars_list = []
investments_list = []


def center(main_window: QMainWindow):
    qr = main_window.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    main_window.move(qr.topLeft())


def sum_accounts_balance():
    sum = 0
    for account in accounts_list:
        sum = sum + account.balance
    return sum


def sum_cc_max_payment():
    sum = 0
    for cc in credit_cars_list:
        sum = sum + cc.max_payment
    return sum


def sum_cc_min_payment():
    sum = 0
    for cc in credit_cars_list:
        sum = sum + cc.min_payment
    return sum


def sum_total_investments():
    sum = 0
    for investment in investments_list:
        sum = sum + investment.balance
    return sum


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1280, 720)
        self.setWindowTitle("PyBank")
        self.setWindowIcon(QIcon('lib/ic_account_balance_2x.png'))

        self.total_balance_groupbox = QGroupBox("")
        self.total_balance_groupbox.setLayout(self.total_balance_box())
        self.total_balance_groupbox.setStyleSheet("""
            QGroupBox {
               border: 0px;
               background: #282828;
               }""")

        total_balance_groupbox2 = QGroupBox("")
        total_balance_groupbox2.setLayout(self.credit_card_box())
        total_balance_groupbox2.setStyleSheet("""
            QGroupBox {
               border: 0px;
               background: #282828;
               }""")

        self.total_balance_groupbox3 = QGroupBox("")
        self.total_balance_layout_box3 = QVBoxLayout()
        latest_transactions_title = QLabel("Investments")
        latest_transactions_title.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        self.total_balance_layout_box3.addLayout(self.investments_box())
        self.total_balance_groupbox3.setLayout(self.total_balance_layout_box3)
        self.total_balance_groupbox3.setStyleSheet("""
            QGroupBox {
               border: 0px;
               background: #282828;
               }""")

        self.home_window = QHBoxLayout()

        total_balance_layout = QHBoxLayout()
        total_balance_layout.addWidget(self.total_balance_groupbox)

        total_balance_layout2 = QHBoxLayout()
        total_balance_layout2.addWidget(total_balance_groupbox2)

        total_balance_layout3 = QHBoxLayout()
        total_balance_layout3.addWidget(self.total_balance_groupbox3)

        transactions_box = QGroupBox()
        transactions_layout = QVBoxLayout()
        transactions_title = QLabel("Latest Transactions")
        transactions_title.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        transactions_layout.addWidget(transactions_title)
        transactions_layout.addWidget(
            self.latest_transactions_box("ACCOUNT TRANSFER", "BANK 2 INVESTMENTS", "10/10/19", 40.00))
        transactions_layout.addWidget(self.latest_transactions_box("MARKET", "BANK 1 SAVINGS", "10/10/19", -800.00))
        transactions_layout.addWidget(
            self.latest_transactions_box("CREDIT CARD", "BANK 2 TRANSFER", "10/10/19", -120.00))
        transactions_layout.addWidget(
            self.latest_transactions_box("RANDOM BILL", "BANK 2 TRANSFER", "10/10/19", -1540.00))
        transactions_box.setLayout(transactions_layout)
        transactions_box.setStyleSheet("""
            QGroupBox {
               border: 0px;
               background: #282828;
               }""")

        summary_information_layout = QHBoxLayout()
        summary_information_layout.setContentsMargins(10, 10, 10, 0)
        summary_information_layout.addLayout(total_balance_layout)
        summary_information_layout.addLayout(total_balance_layout2)
        summary_information_layout.addLayout(total_balance_layout3)

        balance_information_layout = QHBoxLayout()

        balance_bills_groupbox = QGroupBox()
        balance_bills_groupbox_layout = QVBoxLayout()
        balance_bills_title = QLabel("Bills")
        balance_bills_title.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        balance_bills_groupbox_layout.addWidget(balance_bills_title)
        balance_bills_groupbox_layout.addWidget(self.bills_box("CAR INSURANCE", "20/05/19", 800.00))
        balance_bills_groupbox_layout.addWidget(self.bills_box("HOSPITAL", "20/05/19", 800.00))
        balance_bills_groupbox_layout.addWidget(self.bills_box("ELECTRICITY", "20/05/19", 800.00))
        balance_bills_groupbox_layout.addWidget(self.bills_box("WATER", "20/05/19", 800.53))
        balance_bills_groupbox.setLayout(balance_bills_groupbox_layout)
        balance_bills_groupbox.setStyleSheet("""
            QGroupBox {
               border: 0px;
               background: #282828;
               }""")
        balance_bills_groupbox.setMaximumWidth(600)
        balance_information_layout.setContentsMargins(10, 0, 10, 0)
        balance_information_layout.addWidget(balance_bills_groupbox)
        balance_information_layout.addWidget(transactions_box)

        bank_data_layout = QVBoxLayout()
        bank_data_layout.addLayout(summary_information_layout)
        bank_data_layout.addLayout(balance_information_layout)

        self.overview_data_widget = QWidget()
        self.overview_data_widget.setLayout(bank_data_layout)

        account_cc_groupbox = QGroupBox("Credit Cards")
        account_cc_layout_box = QVBoxLayout()
        account_cc_groupbox.setLayout(account_cc_layout_box)
        account_cc_overview = QHBoxLayout()
        account_cc_overview.addWidget(account_cc_groupbox)

        account_transactions_groupbox = QGroupBox("Investments")
        account_transactions_layout_box = QVBoxLayout()
        account_transactions_groupbox.setLayout(account_transactions_layout_box)
        account_transactions_overview = QHBoxLayout()
        account_transactions_overview.addWidget(account_transactions_groupbox)

        account_data_layout = QVBoxLayout()
        account_data_layout.addLayout(account_cc_overview)
        account_data_layout.addLayout(account_transactions_overview)

        self.overview_data_widget.setLayout(bank_data_layout)

        main_menu_layout = QVBoxLayout()
        self.home_window.addLayout(main_menu_layout)
        self.home_window.addWidget(self.overview_data_widget)
        # self.home_window.addWidget(self.account_data_widget) How to add several views

        self.base_layout = QWidget()
        self.base_layout.setStyleSheet("""
        QWidget {
            background: #1e1c1d;
        }""")
        self.setCentralWidget(self.base_layout)
        self.base_layout.setLayout(self.home_window)

        # Property to make the window borderless
        # self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)

        self.show()

    def hide_summary_data(self, item):
        if item.text() == "Overview":
            self.overview_data_widget.show()
            self.account_data_widget.hide()
        else:
            self.overview_data_widget.hide()
            self.account_data_widget.show()

    def total_balance_box(self):
        total_balance_box = QVBoxLayout()
        balance_label = QLabel("$" + str(sum_accounts_balance()))
        balance_label.setStyleSheet(
            "font-family: Roboto; font: 36pt; background: #282828; color: white; font-weight: bold;")
        accounts_label = QLabel("Accounts")
        accounts_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        accounts_label.setMaximumHeight(14)
        total_balance_box.addWidget(accounts_label)
        total_balance_box.addItem(QSpacerItem(50, 15))
        total_balance_box.addWidget(balance_label)
        total_balance_box.addItem(QSpacerItem(50, 20))

        # Calculate percetanges:
        percentages = []
        for acc in accounts_list:
            percentages.append(round((acc.balance * 100 / sum_accounts_balance()) / 100, 2))
        print(percentages[0], percentages[0] + 0.001, percentages[1], percentages[1] + 0.001, percentages[2],
              percentages[2] + 0.0001, percentages[3])

        color_strip = QFrame()
        color_strip.setStyleSheet(
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #006159, stop:{} #006159, stop:{} #008654, stop:{} #008654, stop:{} #00C582, stop:{} #00C582, stop:{} #00FEBC, stop:1 #00FEBC );".format(
                percentages[0], percentages[0] + 0.0001, percentages[1], percentages[1] + 0.0001, percentages[2],
                                percentages[2] + 0.0001, percentages[3]))
        color_strip.setFixedHeight(2)

        color_layout = QHBoxLayout()
        color_layout.setContentsMargins(0, 0, 0, 0)
        color_layout.addWidget(color_strip)

        total_balance_box.addLayout(color_layout)
        if len(accounts_list) < 4:
            for i in range(0, len(accounts_list)):
                total_balance_box.addWidget(self.account_box(accounts_list[i], color=i))
            for i in range(0, 4 - len(accounts_list)):
                total_balance_box.addWidget(self.account_box_empty())
        else:
            for i in range(0, 4):
                total_balance_box.addWidget(self.account_box(accounts_list[i], color=i))
        return total_balance_box

    def investments_box(self):
        total_balance_box = QVBoxLayout()
        balance_label = QLabel("$" + str(sum_total_investments()))
        balance_label.setStyleSheet(
            "font-family: Roboto; font: 36pt; background: #282828; color: white; font-weight: bold;")
        accounts_label = QLabel("Investments")
        accounts_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        accounts_label.setMaximumHeight(14)
        total_balance_box.addWidget(accounts_label)
        total_balance_box.addItem(QSpacerItem(50, 15))
        total_balance_box.addWidget(balance_label)
        total_balance_box.addItem(QSpacerItem(50, 20))

        color_strip = QFrame()
        color_strip.setStyleSheet(
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #B15DFF, stop:0.3 #B15DFF, stop:0.3001 #72DEFF, stop:1 #72DEFF);")
        color_strip.setFixedHeight(2)

        color_layout = QHBoxLayout()
        color_layout.setContentsMargins(0, 0, 0, 0)
        color_layout.addWidget(color_strip)

        total_balance_box.addLayout(color_layout)
        for investment in investments_list:
            total_balance_box.addWidget(self.investment_box(investment, color="#B15DFF"))
        if len(investments_list) < 4:
            for i in range(0, 4 - len(investments_list)):
                total_balance_box.addWidget(self.empty_investment_box())
        # total_balance_box.addWidget(self.investment_box(investment, color="#B15DFF"))
        # total_balance_box.addWidget(self.investment_box(money="2000.00", empty=False, color="#72DEFF"))
        # total_balance_box.addWidget(self.investment_box(money="30146.89", empty=True, color=None))
        # total_balance_box.addWidget(self.investment_box(money="60293.78", empty=True, color=None))
        return total_balance_box

    def credit_card_box(self):
        credit_card_box = QVBoxLayout()

        payment_box = QHBoxLayout()

        credit_card_label_total = QLabel("Current balance")
        credit_card_label_total.setStyleSheet(
            "font-family: Roboto; font: 10pt; background: #282828; color: white; font-weight: bold;")
        credit_card_total = QLabel("$" + str(sum_cc_max_payment()))
        credit_card_total.setStyleSheet(
            "font-family: Roboto; font: 24pt; background: #282828; color: white; font-weight: bold;")
        credit_card_total.setMinimumWidth(225)
        credit_card_total_layout = QVBoxLayout()
        credit_card_total_layout.addWidget(credit_card_label_total)
        credit_card_total_layout.addWidget(credit_card_total)

        credit_card_min_payment_title = QLabel("Minimum Payment")
        credit_card_min_payment_title.setStyleSheet(
            "font-family: Roboto; font: 10pt; background: #282828; color: white; font-weight: bold;")
        credit_card_min_payment_value = QLabel("$" + str(sum_cc_min_payment()))
        credit_card_min_payment_value.setStyleSheet(
            "font-family: Roboto; font: 24pt; background: #282828; color: white; font-weight: bold;")
        credit_card_min_payment_layout = QVBoxLayout()
        credit_card_min_payment_layout.addWidget(credit_card_min_payment_title)
        credit_card_min_payment_layout.addWidget(credit_card_min_payment_value)
        credit_card_total.setTextInteractionFlags(Qt.TextSelectableByMouse)

        accounts_label = QLabel("Credit Cards")
        accounts_label.setStyleSheet(
            "background-color: white; font-family: Roboto; font: 12pt; background: #282828; color: white;")

        payment_box.addLayout(credit_card_total_layout)
        payment_box.addLayout(credit_card_min_payment_layout)

        payment_box_title = QVBoxLayout()
        payment_box_title.addWidget(accounts_label)
        payment_box_title.addItem(QSpacerItem(50, 5))
        payment_box_title.addLayout(payment_box)

        credit_card_box.addLayout(payment_box_title)
        credit_card_box.addItem(QSpacerItem(50, 24))

        color_strip = QFrame()
        color_strip.setStyleSheet(
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #ffdc78, stop:0.2 #ffdc78, stop:0.2001 #d85f4e, stop:0.5 #d85f4e, stop:0.5001 #ffac12, stop:1 #ffac12);")
        color_strip.setFixedHeight(2)

        color_layout = QHBoxLayout()
        color_layout.setContentsMargins(0, 0, 0, 0)
        color_layout.addWidget(color_strip)

        credit_card_box.addLayout(color_layout)
        for cc in credit_cars_list:
            credit_card_box.addWidget(self.cc_box(cc, color="white"))
        # credit_card_box.addWidget(self.credit_card_balance(cc_type="Mastercard", color="#FFDC78"))
        # credit_card_box.addWidget(self.credit_card_balance(cc_type="Visa", color="#d85f4e"))
        # credit_card_box.addWidget(self.credit_card_balance(cc_type="Visa", color="#ffac12"))
        # credit_card_box.addWidget(self.credit_card_balance(cc_type="Mastercard", color="#ffac12"))

        return credit_card_box

    def account_box(self, account: example.Account, color: int):
        account_box_layout = QHBoxLayout()

        account_name_layout = QHBoxLayout()
        account_name_label = QLabel(account.name)
        account_name_label.setMinimumWidth(100)
        account_name_label.setStyleSheet("font-family: Roboto; font: 10pt; background: #282828; color: white;")
        account_name_layout.addWidget(account_name_label)

        account_number_layout = QHBoxLayout()
        account_number_label = QLabel(account.number)
        account_number_label.setStyleSheet("font-family: Roboto; font: 8pt; background: #282828; color: grey;")
        account_number_layout.addWidget(account_number_label)

        account_balance_layout = QHBoxLayout()
        account_balance_label = QLabel(str(account.balance))
        account_balance_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        account_balance_label.setMaximumWidth(75)
        account_money_sign_label = QLabel("$")
        account_money_sign_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        account_money_sign_label.setMaximumWidth(10)
        account_balance_layout.addWidget(account_money_sign_label)
        account_balance_layout.addWidget(account_balance_label)

        color_strip = QFrame()
        if color == 0:
            color_strip.setStyleSheet("background: #006159;")
        if color == 1:
            color_strip.setStyleSheet("background: #008654;")
        if color == 2:
            color_strip.setStyleSheet("background: #00C582;")
        if color == 3:
            color_strip.setStyleSheet("background: #00FEBC;")
        color_strip.setFixedWidth(2)

        account_box_layout.addWidget(color_strip)
        account_box_layout.addLayout(account_name_layout)
        account_box_layout.addLayout(account_number_layout)
        account_box_layout.addLayout(account_balance_layout, Qt.AlignRight)

        frame = QWidget()
        frame.setObjectName("Frame")
        frame.setLayout(account_box_layout)
        frame.setStyleSheet("""
            QWidget#Frame {
               border-bottom: 1px solid #33333D;
               background: transparent;
               }""")
        return frame

    def cc_box(self, cc: example.CreditCard, color):
        cc_box_layout = QHBoxLayout()

        cc_name_layout = QVBoxLayout()
        cc_name_label = QLabel(cc.cc_type)
        cc_name_label.setMinimumWidth(100)
        cc_name_label.setStyleSheet("font-family: Roboto; font: 10pt; background: #282828; color: white;")
        cc_currency_label = QLabel(cc.card_number)
        cc_currency_label.setStyleSheet("font-family: Roboto; font: 8pt; background: #282828; color: grey;")
        cc_name_layout.addWidget(cc_name_label)
        cc_name_layout.addWidget(cc_currency_label)

        cc_due_date_layout = QHBoxLayout()
        cc_due_date_label = QLabel("Due date: " + cc.due_date)
        cc_due_date_label.setStyleSheet("font-family: Roboto; font: 8pt; background: #282828; color: grey;")
        cc_due_date_layout.addWidget(cc_due_date_label)

        cc_balance_layout = QHBoxLayout()
        cc_balance_label = QLabel(str(cc.max_payment))
        cc_balance_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        cc_balance_label.setMaximumWidth(75)
        cc_money_sign_label = QLabel("$")
        cc_money_sign_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        cc_money_sign_label.setMaximumWidth(10)
        cc_balance_layout.addWidget(cc_money_sign_label)
        cc_balance_layout.addWidget(cc_balance_label)

        color_strip = QFrame()
        color_strip.setStyleSheet(
            "background: {};".format(color))
        color_strip.setFixedWidth(2)

        cc_box_layout.addWidget(color_strip)
        cc_box_layout.addLayout(cc_name_layout)
        cc_box_layout.addLayout(cc_due_date_layout)
        cc_box_layout.addLayout(cc_balance_layout, Qt.AlignRight)

        frame = QWidget()
        frame.setObjectName("Frame")
        frame.setLayout(cc_box_layout)
        frame.setStyleSheet("""
                           QWidget#Frame {
                              border-bottom: 1px solid #33333D;
                              background: transparent;
                              }""")
        return frame

    def investment_box(self, investment: example.Investment, color):
        investment_box_layout = QHBoxLayout()

        investment_name_layout = QVBoxLayout()
        investment_name_label = QLabel(investment.name)
        investment_name_label.setMinimumWidth(100)
        investment_name_label.setStyleSheet("font-family: Roboto; font: 10pt; background: #282828; color: white;")
        investment_currency_label = QLabel(investment.currency)
        investment_currency_label.setStyleSheet("font-family: Roboto; font: 10pt; background: #282828; color: white;")
        investment_name_layout.addWidget(investment_name_label)
        investment_name_layout.addWidget(investment_currency_label)

        investment_type_layout = QHBoxLayout()
        investment_type_label = QLabel(investment.type)
        investment_type_label.setStyleSheet("font-family: Roboto; font: 8pt; background: #282828; color: grey;")
        investment_type_layout.addWidget(investment_type_label)

        investment_balance_layout = QHBoxLayout()
        investment_balance_label = QLabel(str(investment.balance))
        investment_balance_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        investment_balance_label.setMaximumWidth(75)
        investment_money_sign_label = QLabel("$")
        investment_money_sign_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        investment_money_sign_label.setMaximumWidth(10)
        investment_balance_layout.addWidget(investment_money_sign_label)
        investment_balance_layout.addWidget(investment_balance_label)

        color_strip = QFrame()
        color_strip.setStyleSheet(
            "background: {};".format(color))
        color_strip.setFixedWidth(2)

        investment_box_layout.addWidget(color_strip)
        investment_box_layout.addLayout(investment_name_layout)
        investment_box_layout.addLayout(investment_type_layout)
        investment_box_layout.addLayout(investment_balance_layout, Qt.AlignRight)

        frame = QWidget()
        frame.setObjectName("Frame")
        frame.setLayout(investment_box_layout)
        frame.setStyleSheet("""
                    QWidget#Frame {
                       border-bottom: 1px solid #33333D;
                       background: transparent;
                       }""")
        return frame

    def empty_investment_box(self):
        investment_box_layout = QHBoxLayout()

        investment_name_layout = QVBoxLayout()
        investment_name_label = QLabel()
        investment_name_label.setMinimumWidth(100)
        investment_name_label.setStyleSheet("font-family: Roboto; font: 10pt; background: #282828; color: white;")
        investment_currency_label = QLabel()
        investment_currency_label.setStyleSheet("font-family: Roboto; font: 10pt; background: #282828; color: white;")
        investment_name_layout.addWidget(investment_name_label)
        investment_name_layout.addWidget(investment_currency_label)

        investment_type_layout = QHBoxLayout()
        investment_type_label = QLabel()
        investment_type_label.setStyleSheet("font-family: Roboto; font: 8pt; background: #282828; color: grey;")
        investment_type_layout.addWidget(investment_type_label)

        investment_balance_layout = QHBoxLayout()
        investment_balance_label = QLabel()
        investment_balance_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        investment_balance_label.setMaximumWidth(75)
        investment_money_sign_label = QLabel()
        investment_money_sign_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        investment_money_sign_label.setMaximumWidth(10)
        investment_balance_layout.addWidget(investment_money_sign_label)
        investment_balance_layout.addWidget(investment_balance_label)

        color_strip = QFrame()
        color_strip.setStyleSheet(
            "background: {};".format("#282828"))
        color_strip.setFixedWidth(2)

        investment_box_layout.addWidget(color_strip)
        investment_box_layout.addLayout(investment_name_layout)
        investment_box_layout.addLayout(investment_type_layout)
        investment_box_layout.addLayout(investment_balance_layout, Qt.AlignRight)

        frame = QWidget()
        frame.setObjectName("Frame")
        frame.setLayout(investment_box_layout)
        frame.setStyleSheet("""
                    QWidget#Frame {
                       border-bottom: 1px solid #282828;
                       background: transparent;
                       }""")
        return frame

    def bills_box(self, bill_name: str, due_date: str, amount: int):
        account_box4 = QHBoxLayout()

        account_name_label4 = QLabel(bill_name)
        account_name_label4.setStyleSheet("font-family: Roboto; font: 10pt; background: #282828; color: white;")
        account_name_label4_layout = QHBoxLayout()
        account_name_label4_layout.addWidget(account_name_label4)

        account_number_label4 = QLabel("Date: " + due_date)
        account_number_label4.setStyleSheet("font-family: Roboto; font: 8pt; background: #282828; color: grey;")
        account_number_label4_layout = QHBoxLayout()
        account_number_label4_layout.addWidget(account_number_label4)

        account_balance_label4 = QLabel(str(amount))
        account_balance_label4.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: #E53935;")
        account_balance_label4.setMaximumWidth(75)
        account_balance_label4.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        account_balance_money_sign = QLabel("$")
        account_balance_money_sign.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        account_balance_money_sign.setMaximumWidth(10)
        account_balance_label4_layout = QHBoxLayout()
        account_balance_label4_layout.addWidget(account_balance_money_sign)
        account_balance_label4_layout.addWidget(account_balance_label4)

        account_box4.addLayout(account_name_label4_layout)
        account_box4.addLayout(account_number_label4_layout)
        account_box4.addLayout(account_balance_label4_layout)

        frame = QWidget()
        frame.setObjectName("Frame")
        frame.setLayout(account_box4)
        frame.setStyleSheet("""
            QWidget#Frame {
               border-bottom: 1px solid #33333D;
               background: transparent;
               }""")
        return frame

    def latest_transactions_box(self, description: str, bank_account_name: str, date: str, amount: int):
        account_box4 = QHBoxLayout()

        account_name_label4 = QLabel(description)
        account_name_label4.setStyleSheet("font-family: Roboto; font: 10pt; background: #282828; color: white;")
        account_name_label4.setMinimumWidth(180)
        account_bank_name_label4 = QLabel(bank_account_name)
        account_bank_name_label4.setMaximumWidth(50)
        account_bank_name_label4.setStyleSheet("font-family: Roboto; font: 8pt; background: #282828; color: grey;")
        account_bank_name_label4.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        account_name_label4_layout = QHBoxLayout()
        account_name_label4_layout.addWidget(account_name_label4)
        account_name_label4_layout.addWidget(account_bank_name_label4)

        account_number_label4 = QLabel("Date: " + date)
        account_number_label4.setStyleSheet("font-family: Roboto; font: 8pt; background: #282828; color: grey;")
        account_number_label4.setAlignment(Qt.AlignCenter)
        account_number_label4_layout = QHBoxLayout()
        account_number_label4_layout.addWidget(account_number_label4)

        account_balance_label4 = QLabel(str(amount))
        if amount < 0:
            account_balance_label4.setStyleSheet(
                "font-family: Roboto; font: 12pt; background: #282828; color: #E53935;")
        else:
            account_balance_label4.setStyleSheet(
                "font-family: Roboto; font: 12pt; background: #282828; color: #1EB980;")
        account_balance_label4.setMaximumWidth(75)
        account_balance_label4.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        account_balance_money_sign = QLabel("$")
        account_balance_money_sign.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        account_balance_money_sign.setMaximumWidth(10)
        account_balance_label4_layout = QHBoxLayout()
        account_balance_label4_layout.addWidget(account_balance_money_sign)
        account_balance_label4_layout.addWidget(account_balance_label4)

        account_box4.addLayout(account_name_label4_layout)
        account_box4.addLayout(account_number_label4_layout)
        account_box4.addLayout(account_balance_label4_layout)

        frame = QWidget()
        frame.setObjectName("Frame")
        frame.setLayout(account_box4)
        frame.setStyleSheet("""
            QWidget#Frame {
               border-bottom: 1px solid #33333D;
               background: transparent;
               }""")
        return frame


if __name__ == "__main__":
    app = QApplication(sys.argv)
    bank_list = example.create_example_banks()
    for bank in bank_list:
        for account in bank.accounts:
            accounts_list.append(account)
        for cc in bank.credit_cards:
            credit_cars_list.append(cc)
        for investment in bank.investments:
            investments_list.append(investment)

    accounts_list.sort(key=operator.attrgetter("balance"), reverse=True)
    credit_cars_list.sort(key=operator.attrgetter("due_date"))

    # splash_pix = QPixmap("lib/loading_screen_bg.png")
    #
    # splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    # splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    # splash.setEnabled(False)
    # splash = QSplashScreen(splash_pix)
    #
    # title = QLabel(splash)
    # title.setText("PyBank")
    # title.setGeometry(splash_pix.width() / 2, splash_pix.height() / 2, 100, 100)
    # title.setStyleSheet("font-family: Roboto; font: 22pt; background: #282828; color: white; font-style: Thin;")
    # # adding progress bar
    # progressBar = QProgressBar(splash)
    # progressBar.setMaximumWidth(620)
    # progressBar.setStyleSheet("""QProgressBar {
    #                                             border: 0px;
    #                                             text-align: top;
    #                                             padding: 2px;
    #                                             background: #33333D;
    #                                             width: 15px;
    #                                             }
    #
    #                                             QProgressBar::chunk {
    #                                             padding: 5px;
    #                                             background: #1EB980;
    #                                             border: 0px;
    # }""")
    # progressBar.setMaximum(10)
    # progressBar.setGeometry(10, splash_pix.height() - 50, splash_pix.width(), 20)
    # progressBar.setTextVisible(False)
    # splash.show()
    #
    # for i in range(1, 11):
    #     time.sleep(1)
    #     progressBar.setValue(i)
    #     t = time.time()
    #     while time.time() < t + 0.1:
    #         app.processEvents()
    #
    # # Simulate something that takes time
    # splash.hide()
    GUI = MainWindow()
    app.exec_()
