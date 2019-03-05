from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

import plotly.offline as py
import plotly.graph_objs as go

import pandas as pd
from datetime import datetime

#  Sources: Icons = Material Design icons by Google (https://github.com/google/material-design-icons)

#  For test purposes
bank_list = ["Bank 1", "Bank 1"]


def center(main_window: QMainWindow):
    qr = main_window.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    main_window.move(qr.topLeft())


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1280, 720)
        self.setWindowTitle("PyBank")
        self.setWindowIcon(QIcon('/lib/ic_account_balance_2x.png'))
        bank_list_dropdown = QComboBox()
        bank_list_dropdown.move(800, 10)
        bank_list_dropdown.setFixedSize(200, 30)
        bank_list_dropdown.addItems(bank_list)
        # bank_list_dropdown.activated.connect(None)

        total_balance_groupbox = QGroupBox("")
        total_balance_groupbox.setLayout(self.total_balance_box())
        total_balance_groupbox.setMaximumWidth(360)
        total_balance_groupbox.setStyleSheet("""
            QGroupBox {
               border: 0px;
               background: #424242;
               }""")

        total_balance_groupbox2 = QGroupBox("")
        total_balance_groupbox2.setLayout(self.credit_card_box())
        total_balance_groupbox2.setMaximumWidth(360)
        total_balance_groupbox2.setStyleSheet("""
            QGroupBox {
               border: 0px;
               background: #424242;
               }""")

        self.total_balance_groupbox3 = QGroupBox("")
        self.total_balance_layout_box3 = QVBoxLayout()
        latest_transactions_title = QLabel("Latest Transactions")
        latest_transactions_title.setStyleSheet("font-family: Roboto; font: 12pt; background: #424242; color: white;")
        latest_transactions_scroll = QScrollArea()
        latest_transactions_list = QWidget()
        latest_transactions_list.setLayout(self.latest_transactions())
        latest_transactions_scroll.setWidget(latest_transactions_list)
        latest_transactions_scroll.setWidgetResizable(True)
        latest_transactions_scroll.setStyleSheet("background: #424242; border: 0px;")
        self.total_balance_layout_box3.addWidget(latest_transactions_title)
        self.total_balance_layout_box3.addWidget(latest_transactions_scroll)
        self.total_balance_groupbox3.setLayout(self.total_balance_layout_box3)
        self.total_balance_groupbox3.setStyleSheet("""
            QGroupBox {
               border: 0px;
               background: #424242;
               }""")

        self.home_window = QHBoxLayout()

        select_bank_layout = QHBoxLayout()
        select_bank_layout.addWidget(bank_list_dropdown)
        select_bank_layout.setDirection(QBoxLayout.RightToLeft)
        select_bank_layout.addStretch(1)

        total_balance_layout = QHBoxLayout()
        total_balance_layout.addWidget(total_balance_groupbox)

        total_balance_layout2 = QHBoxLayout()
        total_balance_layout2.addWidget(total_balance_groupbox2)

        total_balance_layout3 = QHBoxLayout()
        total_balance_layout3.addWidget(self.total_balance_groupbox3)

        view = QWebEngineView()
        view.load(QUrl.fromLocalFile(QFileInfo("time-series-simple.html").absoluteFilePath()))
        view.setMaximumHeight(300)
        view.setStyleSheet("background: transparent;")
        view.page().setBackgroundColor(Qt.transparent)
        graph_box = QGroupBox()
        graph_layout = QHBoxLayout()
        graph_layout.addWidget(view)
        graph_box.setLayout(graph_layout)
        graph_box.setStyleSheet("""
            QGroupBox {
               border: 0px;
               background: #424242;
               }""")
        graph = QHBoxLayout()
        graph.addWidget(graph_box)

        summary_information_layout = QHBoxLayout()
        summary_information_layout.addLayout(total_balance_layout)
        summary_information_layout.addLayout(total_balance_layout2)
        summary_information_layout.addLayout(total_balance_layout3)

        balance_information_layout = QHBoxLayout()

        balance_information_groupbox = QGroupBox("")
        balance_information_groupbox_layout = QVBoxLayout()
        balance_information_groupbox.setLayout(balance_information_groupbox_layout)

        new_layout = QHBoxLayout()
        new_layout.addWidget(balance_information_groupbox)

        balance_information_layout.addLayout(new_layout)
        balance_information_layout.addLayout(graph)

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

        account_transactions_groupbox = QGroupBox("Latest Transactions")
        account_transactions_layout_box = QVBoxLayout()
        account_transactions_groupbox.setLayout(account_transactions_layout_box)
        account_transactions_overview = QHBoxLayout()
        account_transactions_overview.addWidget(account_transactions_groupbox)

        account_data_layout = QVBoxLayout()
        account_data_layout.addLayout(select_bank_layout)
        account_data_layout.addLayout(account_cc_overview)
        account_data_layout.addLayout(account_transactions_overview)

        self.account_data_widget = QWidget()
        self.account_data_widget.setLayout(account_data_layout)
        self.account_data_widget.hide()

        self.overview_data_widget.setLayout(bank_data_layout)

        main_menu_layout = QVBoxLayout()
        self.home_window.addLayout(main_menu_layout)
        self.home_window.addWidget(self.overview_data_widget)
        self.home_window.addWidget(self.account_data_widget)

        self.base_layout = QWidget()
        self.base_layout.setStyleSheet("""
        QWidget {
            background: #212121;
        }""")
        self.setCentralWidget(self.base_layout)
        self.base_layout.setLayout(self.home_window)

        self.show()

        # loading_screen = self.newWindow()

    def hide_summary_data(self, item):
        if item.text() == "Overview":
            self.overview_data_widget.show()
            self.account_data_widget.hide()
        else:
            self.overview_data_widget.hide()
            self.account_data_widget.show()

    def total_balance_box(self):
        total_balance_box = QVBoxLayout()
        balance_label = QLabel("$120,587.56")
        balance_label.setStyleSheet("font-family: Roboto; font: 36pt; background: #424242; color: #1EB980;")
        accounts_label = QLabel("Accounts")
        accounts_label.setStyleSheet("font-family: Roboto; font: 12pt; background: #424242; color: white;")
        accounts_label.setMaximumHeight(14)
        total_balance_box.addWidget(accounts_label)
        total_balance_box.addWidget(balance_label)
        total_balance_box.addItem(QSpacerItem(50, 30))

        see_all_layout = QVBoxLayout()
        see_all_label = QPushButton("SEE ALL")
        see_all_layout.addWidget(see_all_label)

        total_balance_box.addLayout(self.account_box(money="30146.89"))
        total_balance_box.addLayout(self.account_box(money="0.00"))
        total_balance_box.addLayout(self.account_box(money="30146.89"))
        total_balance_box.addLayout(self.account_box(money="60293.78"))
        total_balance_box.addLayout(see_all_layout)
        return total_balance_box

    def credit_card_box(self):
        credit_card_box = QVBoxLayout()

        payment_box = QHBoxLayout()
        credit_card_label_total = QLabel("Current balance")
        credit_card_label_total.setStyleSheet(
            "font-family: Roboto; font-weight: bold; font: 10pt; background: #424242; color: white;")
        credit_card_total = QLabel("$587.56")
        credit_card_total.setStyleSheet("font-family: Roboto; font: 24pt; background: #424242; color: #ef6c00;")
        credit_card_total_layout = QVBoxLayout()
        credit_card_total_layout.addWidget(credit_card_label_total)
        credit_card_total_layout.addWidget(credit_card_total)
        credit_card_min_payment_title = QLabel("Minimum Payment       ")
        credit_card_min_payment_title.setStyleSheet(
            "font-family: Roboto; font: 10pt; background: #424242; color: white;")
        credit_card_min_payment_value = QLabel("$250.58 ")
        credit_card_min_payment_value.setStyleSheet(
            "font-family: Roboto; font: 24pt; background: #424242; color: #ff9d3f;")
        credit_card_min_payment_layout = QVBoxLayout()
        credit_card_min_payment_layout.addWidget(credit_card_min_payment_title, 0, Qt.AlignRight)
        credit_card_min_payment_layout.addWidget(credit_card_min_payment_value, 0, Qt.AlignRight)
        credit_card_total.setTextInteractionFlags(Qt.TextSelectableByMouse)
        accounts_label = QLabel("Credit Cards")
        accounts_label.setStyleSheet(
            "background-color: white; font-family: Roboto; font: 12pt; background: #424242; color: white;")

        payment_box.addLayout(credit_card_total_layout)
        payment_box.addLayout(credit_card_min_payment_layout)

        payment_box_title = QVBoxLayout()
        payment_box_title.addWidget(accounts_label)
        payment_box_title.addItem(QSpacerItem(50, 5))
        payment_box_title.addLayout(payment_box)

        credit_card_box.addLayout(payment_box_title)
        credit_card_box.addItem(QSpacerItem(50, 20))

        see_all_layout = QVBoxLayout()
        see_all_label = QPushButton("SEE ALL")
        see_all_layout.addWidget(see_all_label)

        credit_card_box.addLayout(self.credit_card_balance(cc_type="Mastercard"))
        credit_card_box.addLayout(self.credit_card_balance(cc_type="Visa"))
        credit_card_box.addLayout(self.credit_card_balance(cc_type="Visa"))
        credit_card_box.addLayout(self.credit_card_balance(cc_type="Mastercard"))
        credit_card_box.addLayout(see_all_layout)

        return credit_card_box

    def newWindow(self):
        self.mainwindow2 = MainWindow2(self)
        self.mainwindow2.closed.connect(self.show)
        self.mainwindow2.show()
        self.hide()

    def account_box(self, money):
        account_box4 = QHBoxLayout()

        accounts_name_box4 = QVBoxLayout()
        account_name_label4 = QLabel("Bank 2 Savings")
        account_name_label4.setStyleSheet("font-family: Roboto; font: 10pt; background: #424242; color: white;")
        account_number_label4 = QLabel("xxxx-xxxx-xxxx-9658")
        account_number_label4.setStyleSheet("font-family: Roboto; font: 8pt; background: #424242; color: grey;")
        accounts_name_box4.setContentsMargins(0, 0, 0, 0)
        accounts_name_box4.addWidget(account_name_label4, 0, Qt.AlignBottom)
        accounts_name_box4.addWidget(account_number_label4, 0, Qt.AlignTop)

        account_balance_box4 = QHBoxLayout()
        account_balance_label4 = QLabel(money)
        account_balance_label4.setStyleSheet("font-family: Roboto; font: 12pt; background: #424242; color: white;")
        account_balance_box4.addWidget(account_balance_label4, Qt.AlignCenter)
        account_balance_box4.addStretch(1)

        account_balance_money_sign_layout = QHBoxLayout()
        account_balance_money_sign = QLabel("$")
        account_balance_money_sign.setStyleSheet("font-family: Roboto; font: 12pt; background: #424242; color: white;")
        account_balance_money_sign_layout.addWidget(account_balance_money_sign, 0, Qt.AlignRight)
        account_balance_money_sign_layout.setContentsMargins(0, 0, 50, 0)

        # account_box4.setContentsMargins(0, 0, 0, 0)
        account_box4.addLayout(accounts_name_box4)
        account_box4.addLayout(account_balance_money_sign_layout, Qt.AlignRight)
        account_box4.addLayout(account_balance_box4, Qt.AlignLeft)
        return account_box4

    def credit_card_balance(self, cc_type):
        credit_card_box4 = QHBoxLayout()

        credit_cards_name_box4 = QVBoxLayout()
        credit_card_name_label4 = QLabel(cc_type)
        credit_card_name_label4.setStyleSheet("font-family: Roboto; font: 10pt; background: #424242; color: white;")
        credit_card_number_label4 = QLabel("xxxx-xxxx-xxxx-9658")
        credit_card_number_label4.setStyleSheet("font-family: Roboto; font: 8pt; background: #424242; color: grey;")
        credit_cards_name_box4.setContentsMargins(0, 0, 0, 0)
        credit_cards_name_box4.addWidget(credit_card_name_label4, 0, Qt.AlignBottom)
        credit_cards_name_box4.addWidget(credit_card_number_label4, 0, Qt.AlignTop)

        credit_card_balance_box4 = QHBoxLayout()
        credit_card_balance_label4 = QLabel("Min: $0.00 Total: $0.00")
        credit_card_balance_label4.setStyleSheet(
            "font-family: Roboto; font: 10pt; background: #424242; color: white;")
        credit_card_balance_box4.addWidget(credit_card_balance_label4, 0, Qt.AlignCenter)
        credit_card_balance_box4.setDirection(QBoxLayout.RightToLeft)
        credit_card_balance_box4.setContentsMargins(0, 0, 0, 0)
        credit_card_balance_box4.addStretch(1)

        credit_card_box4.setContentsMargins(0, 0, 0, 0)
        credit_card_box4.addLayout(credit_cards_name_box4)
        credit_card_box4.addLayout(credit_card_balance_box4)
        return credit_card_box4

    def latest_transactions(self):
        layout = QVBoxLayout()

        for i in range(0, 20):
            layout.addLayout(self.transcation_item("01/02", 200, "Debit"))
            layout.addLayout(self.transcation_item("01/02", -200, "Money Transfer and payments"))

        return layout

    def transcation_item(self, date, amount, description):
        credit_card_box4 = QHBoxLayout()

        credit_card_name_label4 = QLabel(date)
        credit_card_name_label4.setStyleSheet("font-family: Roboto; font: 14pt; background: #424242; color: white;")

        credit_card_number_label4 = QLabel(description)
        credit_card_number_label4.setStyleSheet("font-family: Roboto; font: 14pt; background: #424242; color: grey;")

        credit_card_balance_label4 = QLabel("$" + str(amount))
        if amount >= 0:
            credit_card_balance_label4.setStyleSheet(
                "font-family: Roboto; font: 14pt; background: #424242; color: #1EB980;")
        else:
            credit_card_balance_label4.setStyleSheet(
                "font-family: Roboto; font: 14pt; background: #424242; color: #FF6589;")

        credit_card_box4.setContentsMargins(0, 0, 0, 0)
        credit_card_box4.addSpacing(2)
        credit_card_box4.addWidget(credit_card_name_label4)
        credit_card_box4.addWidget(credit_card_number_label4, 0, Qt.AlignCenter)
        credit_card_box4.addWidget(credit_card_balance_label4, 0, Qt.AlignRight)
        return credit_card_box4


class MainWindow2(QMainWindow):
    # QMainWindow doesn't have a closed signal, so we'll make one.
    closed = pyqtSignal()

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.parent = parent
        label = QLabel('Retrieving Bank Data', self)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()


def main():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    data = [go.Scatter(x=[0, 1, 2, 5, 8, 7], y=[1, 2, 3, 4, 5, 6], mode="lines+markers+text",
                       line=dict(color="rgb(30, 185, 128)"), text=[1, 2, 3, 4, 5, 6], textposition="top center",
                       fill='tonexty')]
    layout = go.Layout(paper_bgcolor='rgb(66,66,66)', plot_bgcolor='rgb(66,66,66)',
                       font=dict(family="Roboto", size=15, color='rgb(255,255,255)'),
                       autosize=False, width=620, height=280,
                       margin=go.layout.Margin(l=50, r=50, b=50, t=50, pad=0))
    fig = go.Figure(data=data, layout=layout)

    py.plot(fig, filename='time-series-simple.html', auto_open=False)

    app = QApplication(sys.argv)
    GUI = MainWindow()
    app.exec_()


main()
