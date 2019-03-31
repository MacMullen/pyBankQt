from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import os, os.path
import pickle
import operator
import example
from lib.classes import *

#  Sources: Icons = Material Design icons by Google (https://github.com/google/material-design-icons)

bank_list = []
accounts_list = []
credit_cards_list = []
investments_list = []
bill_list = []
transactions_list = []


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


def sum_total_bills():
    sum = 0
    for bill in bill_list:
        sum = sum + bill.amount
    return sum


def sum_latest_transactions():
    sum_outcome = 0
    sum_income = 0
    for transaction in transactions_list:
        if transaction.amount < 0:
            sum_outcome = sum_outcome - transaction.amount
        else:
            sum_income = sum_income + transaction.amount
    return [sum_income, sum_outcome]


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1280, 720)
        self.setWindowTitle("PyBank")
        self.setWindowIcon(QIcon('assests/appicon.png'))
        center(self)

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

        summary_information_layout = QHBoxLayout()
        summary_information_layout.setContentsMargins(0, 0, 0, 0)
        summary_information_layout.addLayout(total_balance_layout)
        summary_information_layout.addLayout(total_balance_layout2)
        summary_information_layout.addLayout(total_balance_layout3)

        balance_information_layout = QHBoxLayout()

        balance_information_layout.setContentsMargins(0, 0, 0, 0)
        balance_information_layout.addWidget(self.bills_groupbox())
        balance_information_layout.addWidget(self.latest_transactions_groupbox())

        bank_data_layout = QVBoxLayout()
        bank_data_layout.addLayout(summary_information_layout)
        bank_data_layout.addLayout(balance_information_layout)
        self.overview_data_widget = QWidget()
        self.overview_data_widget.setLayout(bank_data_layout)

        coming_soon_layout = QVBoxLayout()
        coming_soon_label = QLabel("COMING SOON")
        coming_soon_label.setStyleSheet("color: white;")
        coming_soon_layout.addWidget(coming_soon_label)
        self.coming_soon_widget = QWidget()
        self.coming_soon_widget.setLayout(coming_soon_layout)
        self.coming_soon_widget.hide()

        self.overview_data_widget.setLayout(bank_data_layout)

        main_menu_bg = QFrame()
        main_menu_bg.setStyleSheet("background: #121212;")
        main_menu_bg.setMinimumWidth(100)
        main_menu_bg.setMaximumWidth(100)
        main_menu_layout = QVBoxLayout()
        # main_menu_layout.setContentsMargins(0, 0, 0, 0)
        main_menu_layout.addWidget(self.menu_overview_button(), 0, Qt.AlignCenter)
        main_menu_layout.addWidget(self.menu_account_button(), 0, Qt.AlignCenter)
        main_menu_layout.addWidget(self.menu_credit_cards_button(), 0, Qt.AlignCenter)
        main_menu_layout.addWidget(self.menu_investments_button(), 0, Qt.AlignCenter)
        main_menu_layout.addWidget(self.menu_bills_button(), 0, Qt.AlignCenter)
        main_menu_layout.addWidget(self.menu_transactions_button(), 0, Qt.AlignCenter)
        main_menu_layout.setSpacing(0)
        main_menu_bg.setLayout(main_menu_layout)
        self.home_window.addWidget(main_menu_bg, 0, Qt.AlignLeft)
        self.home_window.addWidget(self.overview_data_widget)
        self.home_window.addWidget(self.coming_soon_widget)
        self.home_window.setContentsMargins(0, 0, 0, 0)
        # self.home_window.addWidget(self.account_data_widget) How to add several views

        self.base_layout = QWidget()
        self.base_layout.setStyleSheet("""
        QWidget {
            background: #181818;
        }""")
        self.setCentralWidget(self.base_layout)
        self.base_layout.setLayout(self.home_window)

        # Property to make the window borderless
        # self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.show()

    def show_summary_data(self):
        self.overview_data_widget.show()
        self.coming_soon_widget.hide()
        self.home_button.setChecked(True)
        self.account_button.setChecked(False)
        self.credit_cards_button.setChecked(False)
        self.investments_button.setChecked(False)
        self.bills_button.setChecked(False)
        self.transactions_button.setChecked(False)

    def show_accounts_data(self):
        self.overview_data_widget.hide()
        self.coming_soon_widget.show()
        self.home_button.setChecked(False)
        self.account_button.setChecked(True)
        self.credit_cards_button.setChecked(False)
        self.investments_button.setChecked(False)
        self.bills_button.setChecked(False)
        self.transactions_button.setChecked(False)

    def show_credit_cards_data(self):
        self.overview_data_widget.hide()
        self.coming_soon_widget.show()
        self.home_button.setChecked(False)
        self.account_button.setChecked(False)
        self.credit_cards_button.setChecked(True)
        self.investments_button.setChecked(False)
        self.bills_button.setChecked(False)
        self.transactions_button.setChecked(False)

    def show_investments_data(self):
        self.overview_data_widget.hide()
        self.coming_soon_widget.show()
        self.home_button.setChecked(False)
        self.account_button.setChecked(False)
        self.credit_cards_button.setChecked(False)
        self.investments_button.setChecked(True)
        self.bills_button.setChecked(False)
        self.transactions_button.setChecked(False)

    def show_bills_data(self):
        self.overview_data_widget.hide()
        self.coming_soon_widget.show()
        self.home_button.setChecked(False)
        self.account_button.setChecked(False)
        self.credit_cards_button.setChecked(False)
        self.investments_button.setChecked(False)
        self.bills_button.setChecked(True)
        self.transactions_button.setChecked(False)

    def show_transactions_data(self):
        self.overview_data_widget.hide()
        self.coming_soon_widget.show()
        self.home_button.setChecked(False)
        self.account_button.setChecked(False)
        self.credit_cards_button.setChecked(False)
        self.investments_button.setChecked(False)
        self.bills_button.setChecked(False)
        self.transactions_button.setChecked(True)

    def menu_overview_button(self):
        self.home_button = QToolButton()
        self.home_button.setText("Overview")
        self.home_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.home_button.setMinimumWidth(50)
        self.home_button.setMaximumHeight(50)
        self.home_button.setIcon(QIcon("assests/overview_white_icon.png"))
        self.home_button.setStyleSheet(open('assests/style.css').read())
        self.home_button.setIconSize(QSize(25, 25))
        self.home_button.setCheckable(True)
        self.home_button.clicked.connect(self.show_summary_data)

        return self.home_button

    def menu_account_button(self):
        self.account_button = QToolButton()
        self.account_button.setText("Accounts")
        self.account_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.account_button.setMinimumWidth(50)
        self.account_button.setMaximumHeight(50)
        self.account_button.setIcon(QIcon("assests/accounts_white_icon.png"))
        self.account_button.setStyleSheet(open('assests/style.css').read())
        self.account_button.setIconSize(QSize(25, 25))
        self.account_button.setCheckable(True)
        self.account_button.clicked.connect(self.show_accounts_data)

        return self.account_button

    def menu_credit_cards_button(self):
        self.credit_cards_button = QToolButton()
        self.credit_cards_button.setText("Credit Cards")
        self.credit_cards_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.credit_cards_button.setMinimumWidth(50)
        self.credit_cards_button.setMaximumHeight(50)
        self.credit_cards_button.setIcon(QIcon("assests/credit_card_white_icon.png"))
        self.credit_cards_button.setStyleSheet(open('assests/style.css').read())
        self.credit_cards_button.setIconSize(QSize(25, 25))
        self.credit_cards_button.setCheckable(True)
        self.credit_cards_button.clicked.connect(self.show_credit_cards_data)

        return self.credit_cards_button

    def menu_investments_button(self):
        self.investments_button = QToolButton()
        self.investments_button.setText("Investments")
        self.investments_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.investments_button.setMinimumWidth(50)
        self.investments_button.setMaximumHeight(50)
        self.investments_button.setIcon(QIcon("assests/investments_white_icon.png"))
        self.investments_button.setStyleSheet(open('assests/style.css').read())
        self.investments_button.setIconSize(QSize(25, 25))
        self.investments_button.setCheckable(True)
        self.investments_button.clicked.connect(self.show_investments_data)

        return self.investments_button

    def menu_bills_button(self):
        self.bills_button = QToolButton()
        self.bills_button.setText("Bills")
        self.bills_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.bills_button.setMinimumWidth(50)
        self.bills_button.setMaximumHeight(50)
        self.bills_button.setIcon(QIcon("assests/bills_white_icon.png"))
        self.bills_button.setStyleSheet(open('assests/style.css').read())
        self.bills_button.setIconSize(QSize(25, 25))
        self.bills_button.setCheckable(True)
        self.bills_button.clicked.connect(self.show_bills_data)

        return self.bills_button

    def menu_transactions_button(self):
        self.transactions_button = QToolButton()
        self.transactions_button.setText("Transactions")
        self.transactions_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.transactions_button.setMinimumWidth(50)
        self.transactions_button.setMaximumHeight(50)
        self.transactions_button.setIcon(QIcon("assests/transactions_white_icon.png"))
        self.transactions_button.setStyleSheet(open('assests/style.css').read())
        self.transactions_button.setIconSize(QSize(25, 25))
        self.transactions_button.setCheckable(True)
        self.transactions_button.clicked.connect(self.show_transactions_data)

        return self.transactions_button

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
                percent = 0.002
            percentages.append(percent - 0.002)

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
                percent = 0.002
            percentages.append(percent - 0.002)

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
                percent = 0.002
            percentages.append(percent - 0.002)

        credit_card_groupbox_layout.addWidget(
            self.groupbox_color_strip(colors=["#c30000", "#f4511e", "#ff8f00", "#ffeb3b"],
                                      amount=len(credit_cards_list), percent=percentages))

        for index, cc in enumerate(credit_cards_list):
            credit_card_groupbox_layout.addWidget(self.credit_card_box(cc, color=index))
        if len(credit_cards_list) < 4:
            for i in range(0, 4 - len(credit_cards_list)):
                credit_card_groupbox_layout.addWidget(self.credit_card_box_empty())

        return credit_card_groupbox_layout

    def bills_groupbox(self):
        balance_bills_groupbox = QGroupBox()

        balance_bills_groupbox_layout = QVBoxLayout()
        balance_bills_title = QLabel("Bills")
        balance_bills_title.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        balance_label = QLabel("$" + str(sum_total_bills()))
        balance_label.setStyleSheet(
            "font-family: Roboto; font: 24pt; background: #282828; color: white; font-weight: bold;")
        balance_bills_groupbox_layout.addWidget(balance_bills_title)
        balance_bills_groupbox_layout.addWidget(balance_label)
        balance_bills_groupbox_layout.addWidget(self.groupbox_color_strip(colors=["#282828"], amount=1, percent=[]))

        for bill in bill_list:
            balance_bills_groupbox_layout.addWidget(self.bills_box(bill))

        balance_bills_groupbox.setLayout(balance_bills_groupbox_layout)
        balance_bills_groupbox.setStyleSheet("""
            QGroupBox {
               border: 0px;
               background: #282828;
               }""")
        balance_bills_groupbox.setMaximumWidth(600)

        return balance_bills_groupbox

    def latest_transactions_groupbox(self):
        transactions_box = QGroupBox()
        transactions_layout = QVBoxLayout()
        transactions_title = QLabel("Latest Transactions")
        transactions_title.setStyleSheet("font-family: Roboto; font: 12pt; background: #282828; color: white;")
        transactions_layout.addWidget(transactions_title)

        balance_layout = QHBoxLayout()
        balance_label_income = QLabel("$" + str(sum_latest_transactions()[0]))
        balance_label_income.setStyleSheet(
            "font-family: Roboto; font: 24pt; background: #282828; color: #1EB980; font-weight: bold;")
        balance_label_outcome = QLabel("$" + str(sum_latest_transactions()[1]))
        balance_label_outcome.setAlignment(Qt.AlignRight)
        balance_label_outcome.setStyleSheet(
            "font-family: Roboto; font: 24pt; background: #282828; color: #E53935; font-weight: bold;")
        balance_layout.addWidget(balance_label_income)
        balance_layout.addWidget(balance_label_outcome)

        percentage_income = 0.0
        percentage_outcome = 0.0
        sum_income = 0
        sum_outcome = 0
        for transaction in transactions_list[:4]:
            if transaction.amount < 0:
                sum_outcome = sum_outcome + (transaction.amount * -1)
            else:
                sum_income = sum_income + transaction.amount
        percentage_income = round((sum_income / (sum_income + sum_outcome)) - 0.002 / 100, 2)
        percentage_outcome = round((sum_outcome / (sum_income + sum_outcome)) - 0.002 / 100, 2)

        transactions_layout.addLayout(balance_layout)

        transactions_layout.addWidget(self.groupbox_color_strip(colors=["#1EB980", "#E53935"],
                                                                amount=2,
                                                                percent=[percentage_income, percentage_outcome]))

        for transaction in transactions_list[:5]:
            transactions_layout.addWidget(self.latest_transactions_box(transaction))
        transactions_box.setLayout(transactions_layout)
        transactions_box.setStyleSheet("""
            QGroupBox {
               border: 0px;
               background: #282828;
               }""")
        return transactions_box

    def account_box(self, account: Account, color: int):
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

    def credit_card_box(self, cc: CreditCard, color):
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

    def investment_box(self, investment: Investment, color):
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

    def bills_box(self, bill: Bill):
        account_box4 = QHBoxLayout()

        account_name_label4 = QLabel(bill.name)
        account_name_label4.setStyleSheet("font-family: Roboto; font: 10pt; background: #282828; color: white;")
        account_name_label4_layout = QHBoxLayout()
        account_name_label4_layout.addWidget(account_name_label4)

        account_number_label4 = QLabel("Date: " + bill.due_date.print_date())
        account_number_label4.setStyleSheet("font-family: Roboto; font: 8pt; background: #282828; color: grey;")
        account_number_label4_layout = QHBoxLayout()
        account_number_label4_layout.addWidget(account_number_label4)

        account_balance_label4 = QLabel(str(bill.amount))
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

    def latest_transactions_box(self, transaction: Transaction):
        account_box4 = QHBoxLayout()

        account_name_label4 = QLabel(transaction.description)
        account_name_label4.setStyleSheet("font-family: Roboto; font: 10pt; background: #282828; color: white;")
        account_name_label4.setMinimumWidth(180)
        account_bank_name_label4 = QLabel(transaction.bank_name)
        account_bank_name_label4.setMaximumWidth(50)
        account_bank_name_label4.setStyleSheet("font-family: Roboto; font: 8pt; background: #282828; color: grey;")
        account_bank_name_label4.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        account_name_label4_layout = QHBoxLayout()
        account_name_label4_layout.addWidget(account_name_label4)
        account_name_label4_layout.addWidget(account_bank_name_label4)

        account_number_label4 = QLabel("Date: " + transaction.date.print_date())
        account_number_label4.setStyleSheet("font-family: Roboto; font: 8pt; background: #282828; color: grey;")
        account_number_label4.setAlignment(Qt.AlignCenter)
        account_number_label4_layout = QHBoxLayout()
        account_number_label4_layout.addWidget(account_number_label4)

        account_balance_label4 = QLabel(str(transaction.amount))
        if transaction.amount < 0:
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
                "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 {}, stop:{} {}, stop:{} {}, stop:{} {}, stop:{} {}, stop:1 {});".format(
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
    splash_pix = QPixmap("assests/loading_screen_bg.png")

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
        for bill in bank.bills:
            bill_list.append(bill)
        for transaction in bank.transactions:
            transactions_list.append(transaction)

    accounts_list.sort(key=operator.attrgetter("balance"), reverse=True)
    credit_cards_list.sort(key=operator.attrgetter("due_date"))
    bill_list.sort(key=operator.attrgetter("due_date"))
    transactions_list.sort(key=operator.attrgetter("date"))
    # time.sleep(1)
    # progressBar.setValue(i)
    # t = time.time()
    # while time.time() < t + 0.1:
    #     app.processEvents()

    # Simulate something that takes time
    splash.hide()
    GUI = MainWindow()
    GUI.home_button.setChecked(True)
    app.exec_()
