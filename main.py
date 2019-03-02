from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from functools import partial
import time
import sys

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

        test_list = QListWidget()
        # test_list.setViewMode(QListView.IconMode)
        list_overview_button = QListWidgetItem(QIcon("lib/ic_home_2x.png"), "Overview")
        list_overview_button.setSizeHint(QSize(120, 60))
        list_overview_button.setTextAlignment(Qt.AlignCenter)
        list_account_button = QListWidgetItem(QIcon("lib/ic_assessment_2x.png"), "Accounts")
        list_account_button.setSizeHint(QSize(120, 60))
        list_account_button.setTextAlignment(Qt.AlignHCenter)
        test_list.addItem(list_overview_button)
        test_list.addItem(list_account_button)
        test_list.setFixedSize(120, 720)
        test_list.itemClicked.connect(self.hide_summary_data)

        total_balance_groupbox = QGroupBox("Total Balance")
        total_balance_groupbox.setLayout(self.total_balance_box())
        total_balance_groupbox.setMaximumWidth(360)

        total_balance_groupbox2 = QGroupBox("Credit Card Summary")
        total_balance_groupbox2.setLayout(self.credit_card_box())
        total_balance_groupbox2.setMaximumWidth(360)

        self.total_balance_groupbox3 = QGroupBox("Latest Transactions")
        self.total_balance_layout_box3 = QVBoxLayout()
        self.total_balance_groupbox3.setLayout(self.total_balance_layout_box3)

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

        graph = QLabel()
        pixmap = QPixmap("lib/area_graph.png")
        graph.setPixmap(pixmap)
        graph_layout = QHBoxLayout()
        graph_layout.addWidget(graph)

        summary_information_layout = QHBoxLayout()
        summary_information_layout.addLayout(total_balance_layout)
        summary_information_layout.addLayout(total_balance_layout2)
        summary_information_layout.addLayout(total_balance_layout3)

        bank_data_layout = QVBoxLayout()
        bank_data_layout.addLayout(summary_information_layout)
        bank_data_layout.addLayout(graph_layout)

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
        main_menu_layout.addWidget(test_list)

        self.home_window.addLayout(main_menu_layout)
        self.home_window.addWidget(self.overview_data_widget)
        self.home_window.addWidget(self.account_data_widget)

        self.base_layout = QWidget()
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
        balance_label.setStyleSheet("font: 36pt")
        accounts_label = QLabel("Accounts")
        accounts_label.setStyleSheet("font: 16pt")
        total_balance_box.addWidget(balance_label)
        total_balance_box.addWidget(accounts_label)

        account_box = QHBoxLayout()

        accounts_name_box = QVBoxLayout()
        account_name_label = QLabel("Bank 1 Savings")
        account_number_label = QLabel("xxxx-xxxx-xxxx-5689")
        accounts_name_box.addWidget(account_name_label)
        accounts_name_box.addWidget(account_number_label)

        account_balance_box = QHBoxLayout()
        account_balance_label = QLabel("$12,000.00")
        account_balance_box.addWidget(account_balance_label)
        account_balance_box.setDirection(QBoxLayout.RightToLeft)
        account_balance_box.addStretch(1)

        account_box.addLayout(accounts_name_box)
        account_box.addLayout(account_balance_box)

        account_box2 = QHBoxLayout()

        accounts_name_box2 = QVBoxLayout()
        account_name_label2 = QLabel("Bank 1 Investments")
        account_number_label2 = QLabel("xxxx-xxxx-xxxx-6985")
        accounts_name_box2.addWidget(account_name_label2)
        accounts_name_box2.addWidget(account_number_label2)

        account_balance_box2 = QHBoxLayout()
        account_balance_label2 = QLabel("$587.56")
        account_balance_box2.addWidget(account_balance_label2)
        account_balance_box2.setDirection(QBoxLayout.RightToLeft)
        account_balance_box2.addStretch(1)

        account_box2.addLayout(accounts_name_box2)
        account_box2.addLayout(account_balance_box2)

        account_box3 = QHBoxLayout()

        accounts_name_box3 = QVBoxLayout()
        account_name_label3 = QLabel("Bank 2 Savings")
        account_number_label3 = QLabel("xxxx-xxxx-xxxx-9658")
        accounts_name_box3.addWidget(account_name_label3)
        accounts_name_box3.addWidget(account_number_label3)

        account_balance_box3 = QHBoxLayout()
        account_balance_label3 = QLabel("$0.00")
        account_balance_box3.addWidget(account_balance_label3)
        account_balance_box3.setDirection(QBoxLayout.RightToLeft)
        account_balance_box3.addStretch(1)

        account_box3.addLayout(accounts_name_box3)
        account_box3.addLayout(account_balance_box3)

        see_all_layout = QVBoxLayout()
        see_all_label = QPushButton("SEE ALL")
        see_all_layout.addWidget(see_all_label)

        total_balance_box.addLayout(account_box)
        total_balance_box.addLayout(account_box2)
        total_balance_box.addLayout(account_box3)
        total_balance_box.addLayout(see_all_layout)
        return total_balance_box

    def credit_card_box(self):
        credit_card_box = QVBoxLayout()
        credit_card_label_total = QLabel("Total Owned")
        credit_card_total = QLabel("$120,587.56")
        credit_card_total.setStyleSheet("font:24pt")
        accounts_label = QLabel("Credit Cards")
        accounts_label.setStyleSheet("font: 10pt")
        credit_card_box.addWidget(credit_card_label_total)
        credit_card_box.addWidget(credit_card_total)
        credit_card_box.addWidget(accounts_label)

        return credit_card_box

    def newWindow(self):
        self.mainwindow2 = MainWindow2(self)
        self.mainwindow2.closed.connect(self.show)
        self.mainwindow2.show()
        self.hide()


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
    app = QApplication(sys.argv)
    GUI = MainWindow()
    app.exec_()

main()
