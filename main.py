from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from functools import partial
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
        bank_list_dropdown.activated.connect(self.hide_summary_data)

        test_list = QListWidget()
        test_list.addItem("Lorem Ipsum")
        test_list.addItem("Lorem Ipsum")
        test_list.setFixedSize(120,720)

        total_balance_groupbox = QGroupBox("Total Balance")
        total_balance_text = QLabel("")
        total_balance_layout_box = QVBoxLayout()
        total_balance_layout_box.addWidget(total_balance_text)
        total_balance_groupbox.setLayout(total_balance_layout_box)

        total_balance_groupbox2 = QGroupBox("Credit Card Summary")
        total_balance_text2 = QLabel("")
        total_balance_layout_box2 = QVBoxLayout()
        total_balance_layout_box2.addWidget(total_balance_text2)
        total_balance_groupbox2.setLayout(total_balance_layout_box2)

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
        bank_data_layout.addLayout(select_bank_layout)
        bank_data_layout.addLayout(summary_information_layout)
        bank_data_layout.addLayout(graph_layout)

        self.bank_data_widget = QWidget()
        self.bank_data_widget.setLayout(bank_data_layout)

        main_menu_layout = QVBoxLayout()
        main_menu_layout.addWidget(test_list)

        self.home_window.addLayout(main_menu_layout)
        self.home_window.addWidget(self.bank_data_widget)

        self.base_layout = QWidget()
        self.setCentralWidget(self.base_layout)
        self.base_layout.setLayout(self.home_window )

        self.show()

    def hide_summary_data(self):
        self.bank_data_widget.hide()

def main():
    app = QApplication(sys.argv)
    GUI = MainWindow()
    sys.exit(app.exec_())


main()
