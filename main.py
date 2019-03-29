from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import os, os.path
import pickle
import operator
import example

#  Sources: Icons = Material Design icons by Google (https://github.com/google/material-design-icons)

bank_list = []
accounts_list = []
credit_cards_list = []
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
    for cc in credit_cards_list:
        sum = sum + cc.max_payment
    return sum


def sum_cc_min_payment():
    sum = 0
    for cc in credit_cards_list:
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
        self.total_balance_groupbox.setLayout(self.accounts_groupbox())
        self.total_balance_groupbox.setStyleSheet("""
            QGroupBox {
               border: 0px;
               background: #282828;
               }""")

        total_balance_groupbox2 = QGroupBox("")
        total_balance_groupbox2.setLayout(self.credit_card_groupbox())
        total_balance_groupbox2.setStyleSheet("""
            QGroupBox {
               border: 0px;
               background: #282828;
               }""")

        self.total_balance_groupbox3 = QGroupBox("")
        self.total_balance_layout_box3 = QVBoxLayout()
        latest_transactions_title = QLabel("Investments")
        latest_transactions_title.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        self.total_balance_layout_box3.addLayout(self.investments_groupbox())
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

    def accounts_groupbox(self):
        accounts_groupbox_layout = QVBoxLayout()
        balance_label = QLabel("$" + str(sum_accounts_balance()))
        balance_label.setStyleSheet(
            "font-family: Roboto; font: 36pt; background: #282828; color: white; font-weight: bold;")
        accounts_label = QLabel("Accounts")
        accounts_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        accounts_label.setMaximumHeight(14)
        accounts_groupbox_layout.addWidget(accounts_label)
        accounts_groupbox_layout.addItem(QSpacerItem(50, 15))
        accounts_groupbox_layout.addWidget(balance_label)
        accounts_groupbox_layout.addItem(QSpacerItem(50, 20))

        # Calculate percentages:
        percentages = []
        for acc in accounts_list:
            percent = round((acc.balance * 100 / sum_accounts_balance()) / 100, 2)
            if percent == 0:
                percent = 0.001
            percentages.append(percent)

        color_layout = QHBoxLayout()
        color_layout.setContentsMargins(0, 0, 0, 0)
        color_layout.addWidget(
            self.groupbox_color_strip(colors=["#006159", "#008654", "#00C582", "#00FEBC"], amount=len(accounts_list),
                                      percent=percentages))

        accounts_groupbox_layout.addLayout(color_layout)

        for i in range(0, len(accounts_list)):
            accounts_groupbox_layout.addWidget(self.account_box(accounts_list[i], color=i))
        if len(accounts_list) < 4:
            for i in range(0, 4 - len(accounts_list)):
                accounts_groupbox_layout.addWidget(self.account_box_empty())

        return accounts_groupbox_layout

    def investments_groupbox(self):
        investments_groupbox_layout = QVBoxLayout()
        balance_label = QLabel("$" + str(sum_total_investments()))
        balance_label.setStyleSheet(
            "font-family: Roboto; font: 36pt; background: #282828; color: white; font-weight: bold;")
        investments_label = QLabel("Investments")
        investments_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        investments_label.setMaximumHeight(14)
        investments_groupbox_layout.addWidget(investments_label)
        investments_groupbox_layout.addItem(QSpacerItem(50, 15))
        investments_groupbox_layout.addWidget(balance_label)
        investments_groupbox_layout.addItem(QSpacerItem(50, 20))

        percentages = []
        for investment in investments_list:
            percent = round((investment.balance * 100 / sum_total_investments()) / 100, 2)
            if percent == 0:
                percent = 0.001
            percentages.append(percent)

        investments_groupbox_layout.addWidget(
            self.groupbox_color_strip(colors=["#9c27b0", "#7c4dff", "#8e99f3", "#6ec6ff"], amount=len(investments_list),
                                      percent=percentages))
        for index, investment in enumerate(investments_list):
            investments_groupbox_layout.addWidget(self.investment_box(investment, color=index))
        if len(investments_list) < 4:
            for i in range(0, 4 - len(investments_list)):
                investments_groupbox_layout.addWidget(self.empty_investment_box())
        return investments_groupbox_layout

    def credit_card_groupbox(self):
        credit_card_groupbox_layout = QVBoxLayout()

        payment_box = QHBoxLayout()

        credit_card_balance_title_label = QLabel("Current balance")
        credit_card_balance_title_label.setStyleSheet(
            "font-family: Roboto; font: 10pt; background: #282828; color: white; font-weight: bold;")
        credit_card_total_balance_label = QLabel("$" + str(sum_cc_max_payment()))
        credit_card_total_balance_label.setStyleSheet(
            "font-family: Roboto; font: 24pt; background: #282828; color: white; font-weight: bold;")
        credit_card_total_balance_label.setMinimumWidth(225)
        credit_card_total_layout = QVBoxLayout()
        credit_card_total_layout.addWidget(credit_card_balance_title_label)
        credit_card_total_layout.addWidget(credit_card_total_balance_label)

        credit_card_min_payment_title_label = QLabel("Minimum Payment")
        credit_card_min_payment_title_label.setStyleSheet(
            "font-family: Roboto; font: 10pt; background: #282828; color: white; font-weight: bold;")
        credit_card_min_payment_label = QLabel("$" + str(sum_cc_min_payment()))
        credit_card_min_payment_label.setStyleSheet(
            "font-family: Roboto; font: 24pt; background: #282828; color: white; font-weight: bold;")
        credit_card_min_payment_layout = QVBoxLayout()
        credit_card_min_payment_layout.addWidget(credit_card_min_payment_title_label)
        credit_card_min_payment_layout.addWidget(credit_card_min_payment_label)

        accounts_label = QLabel("Credit Cards")
        accounts_label.setStyleSheet(
            "background-color: white; font-family: Roboto; font: 12pt; background: #282828; color: white;")

        payment_box.addLayout(credit_card_total_layout)
        payment_box.addLayout(credit_card_min_payment_layout)

        payment_box_title = QVBoxLayout()
        payment_box_title.addWidget(accounts_label)
        payment_box_title.addItem(QSpacerItem(50, 5))
        payment_box_title.addLayout(payment_box)

        credit_card_groupbox_layout.addLayout(payment_box_title)
        credit_card_groupbox_layout.addItem(QSpacerItem(50, 24))

        percentages = []
        for cc in credit_cards_list:
            percent = round((cc.max_payment * 100 / sum_cc_max_payment()) / 100, 2)
            if percent == 0:
                percent = 0.001
            percentages.append(percent)

        credit_card_groupbox_layout.addWidget(
            self.groupbox_color_strip(colors=["#c30000", "#f4511e", "#ff8f00", "#ffeb3b"],
                                      amount=len(credit_cards_list), percent=percentages))

        for index, cc in enumerate(credit_cards_list):
            credit_card_groupbox_layout.addWidget(self.credit_card_box(cc, color=index))
        if len(credit_cards_list) < 4:
            for i in range(0, 4 - len(credit_cards_list)):
                credit_card_groupbox_layout.addWidget(self.credit_card_box_empty())

        return credit_card_groupbox_layout

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

    def account_box_empty(self):
        account_box_layout = QHBoxLayout()

        account_name_layout = QHBoxLayout()
        account_name_label = QLabel()
        account_name_label.setMinimumWidth(100)
        account_name_label.setStyleSheet("font-family: Roboto; font: 10pt; background: #282828; color: white;")
        account_name_layout.addWidget(account_name_label)

        account_number_layout = QHBoxLayout()
        account_number_label = QLabel()
        account_number_label.setStyleSheet("font-family: Roboto; font: 8pt; background: #282828; color: grey;")
        account_number_layout.addWidget(account_number_label)

        account_balance_layout = QHBoxLayout()
        account_balance_label = QLabel()
        account_balance_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        account_balance_label.setMaximumWidth(75)
        account_money_sign_label = QLabel()
        account_money_sign_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        account_money_sign_label.setMaximumWidth(10)
        account_balance_layout.addWidget(account_money_sign_label)
        account_balance_layout.addWidget(account_balance_label)

        color_strip = QFrame()
        color_strip.setStyleSheet("background: #282828;")
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
               border-bottom: 1px solid #282828;
               background: transparent;
               }""")
        return frame

    def credit_card_box(self, cc: example.CreditCard, color):
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
        cc_due_date_label = QLabel("Due date: " + cc.due_date.print_date())
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
        if color == 0:
            color_strip.setStyleSheet("background: #c30000")
        if color == 1:
            color_strip.setStyleSheet("background: #f4511e")
        if color == 2:
            color_strip.setStyleSheet("background: #ff8f00")
        if color == 3:
            color_strip.setStyleSheet("background: #ffeb3b")
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

    def credit_card_box_empty(self):
        cc_box_layout = QHBoxLayout()

        cc_name_layout = QVBoxLayout()
        cc_name_label = QLabel()
        cc_name_label.setMinimumWidth(100)
        cc_name_label.setStyleSheet("font-family: Roboto; font: 10pt; background: #282828; color: white;")
        cc_currency_label = QLabel()
        cc_currency_label.setStyleSheet("font-family: Roboto; font: 8pt; background: #282828; color: grey;")
        cc_name_layout.addWidget(cc_name_label)
        cc_name_layout.addWidget(cc_currency_label)

        cc_due_date_layout = QHBoxLayout()
        cc_due_date_label = QLabel()
        cc_due_date_label.setStyleSheet("font-family: Roboto; font: 8pt; background: #282828; color: grey;")
        cc_due_date_layout.addWidget(cc_due_date_label)

        cc_balance_layout = QHBoxLayout()
        cc_balance_label = QLabel()
        cc_balance_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        cc_balance_label.setMaximumWidth(75)
        cc_money_sign_label = QLabel()
        cc_money_sign_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        cc_money_sign_label.setMaximumWidth(10)
        cc_balance_layout.addWidget(cc_money_sign_label)
        cc_balance_layout.addWidget(cc_balance_label)

        color_strip = QFrame()
        color_strip.setStyleSheet(
            "background: #282828;")
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
                              border-bottom: 1px solid #282828;
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
        if color == 0:
            color_strip.setStyleSheet("background: #9c27b0")
        if color == 1:
            color_strip.setStyleSheet("background: #7c4dff")
        if color == 2:
            color_strip.setStyleSheet("background: #8e99f3")
        if color == 3:
            color_strip.setStyleSheet("background: #6ec6ff")
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

    def groupbox_color_strip(self, colors, amount, percent):
        color_strip = QFrame()
        if amount >= 4:
            color_strip.setStyleSheet(
                "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 {}, stop:{} {}, stop:{} {}, stop:{} {}, stop:{} {}, stop:{} {}, stop:{} {}, stop:1 {});".format(
                    colors[0], percent[0], colors[0], percent[0] + 0.0001, colors[1], percent[0] + percent[1],
                    colors[1],
                                                      percent[0] + percent[1] + 0.0001, colors[2],
                                                      percent[0] + percent[1] + percent[2], colors[2],
                                                      percent[0] + percent[1] + percent[2] + 0.0001, colors[3],
                    colors[3]))
        if amount == 3:
            color_strip.setStyleSheet(
                "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 {}, stop:{} {}, stop:{} {}, stop:{} {}, stop:{} {}, stop:4 {});".format(
                    colors[0], percent[0], colors[0], percent[0] + 0.0001, colors[1], percent[0] + percent[1],
                    colors[1],
                                                      percent[0] + percent[1] + 0.0001, colors[2], colors[2]))
        if amount == 2:
            color_strip.setStyleSheet(
                "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 {}, stop:{} {}, stop:{} {}, stop:1 {});".format(
                    colors[0], percent[0], colors[0], percent[0] + 0.0001, colors[1], colors[1]))
        if amount == 1:
            color_strip.setStyleSheet(
                "background: {};".format(colors[0]))
        if amount == 0:
            color_strip.setStyleSheet("background: #202020;")
        color_strip.setFixedHeight(2)
        return color_strip


if __name__ == "__main__":
    app = QApplication(sys.argv)
    from example import *

    create_example_banks()
    splash_pix = QPixmap("lib/loading_screen_bg.png")

    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)
    splash = QSplashScreen(splash_pix)

    title = QLabel(splash)
    title.setText("PyBank")
    title.setGeometry(splash_pix.width() / 2, splash_pix.height() / 2, 100, 100)
    title.setStyleSheet("font-family: Roboto; font: 22pt; background: #282828; color: white; font-style: Thin;")
    # adding progress bar
    progressBar = QProgressBar(splash)
    progressBar.setMaximumWidth(620)
    progressBar.setStyleSheet("""QProgressBar {
                                                border: 0px;
                                                text-align: top;
                                                padding: 2px;
                                                background: #33333D;
                                                width: 15px;
                                                }

                                                QProgressBar::chunk {
                                                padding: 5px;
                                                background: #1EB980;
                                                border: 0px;
    }""")
    progressBar.setMaximum(10)
    progressBar.setGeometry(10, splash_pix.height() - 50, splash_pix.width(), 20)
    progressBar.setTextVisible(False)

    splash.show()

    for index, bank in enumerate(os.listdir("data/")):
        data = pickle.load(open("data/" + bank, "rb"))
        bank_list.append(data)
        progressBar.setValue(index)
        app.processEvents()
    for bank in bank_list:
        for account in bank.accounts:
            accounts_list.append(account)
        for cc in bank.credit_cards:
            credit_cards_list.append(cc)
        for investment in bank.investments:
            investments_list.append(investment)

    accounts_list.sort(key=operator.attrgetter("balance"), reverse=True)
    credit_cards_list.sort(key=operator.attrgetter("due_date"))
    # time.sleep(1)
    # progressBar.setValue(i)
    # t = time.time()
    # while time.time() < t + 0.1:
    #     app.processEvents()

    # Simulate something that takes time
    splash.hide()
    GUI = MainWindow()
    app.exec_()
