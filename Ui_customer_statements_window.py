# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\qwert\OneDrive\Masaüstü\DATA SCIENCE\PROJECTS\PROJECT-2\BankingApp_SQL\customer_statements_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_customer_statements_window(object):
    def setupUi(self, customer_statements_window):
        customer_statements_window.setObjectName("customer_statements_window")
        customer_statements_window.setWindowModality(QtCore.Qt.ApplicationModal)
        customer_statements_window.resize(600, 700)
        customer_statements_window.setMinimumSize(QtCore.QSize(600, 700))
        customer_statements_window.setMaximumSize(QtCore.QSize(600, 700))
        customer_statements_window.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        customer_statements_window.setAcceptDrops(False)
        customer_statements_window.setStyleSheet("background-color: rgb(5, 130, 202);")
        customer_statements_window.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(customer_statements_window)
        self.centralwidget.setObjectName("centralwidget")
        self.CSstatementswdw_lbl_heading = QtWidgets.QLabel(self.centralwidget)
        self.CSstatementswdw_lbl_heading.setGeometry(QtCore.QRect(30, 0, 541, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.CSstatementswdw_lbl_heading.setFont(font)
        self.CSstatementswdw_lbl_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.CSstatementswdw_lbl_heading.setObjectName("CSstatementswdw_lbl_heading")
        self.CSstatementswdw_btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.CSstatementswdw_btn_back.setEnabled(True)
        self.CSstatementswdw_btn_back.setGeometry(QtCore.QRect(220, 570, 180, 70))
        self.CSstatementswdw_btn_back.setMinimumSize(QtCore.QSize(180, 70))
        self.CSstatementswdw_btn_back.setMaximumSize(QtCore.QSize(180, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.CSstatementswdw_btn_back.setFont(font)
        self.CSstatementswdw_btn_back.setStyleSheet("QPushButton {\n"
"background-color: rgb(0, 150, 199);\n"
"   border-color: rgb(66, 167, 255);\n"
"   border-bottom-color: rgb(255, 255, 255);\n"
"   border:2px solid rgb(202, 240, 248);\n"
"   border-radius:20px;\n"
"   border-color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(202, 240, 248);\n"
"     border:2px solid rgb(202, 240, 248);\n"
"}\n"
"    \n"
"   ")
        self.CSstatementswdw_btn_back.setObjectName("CSstatementswdw_btn_back")
        self.CSstatementswdw_lbl_filter = QtWidgets.QLabel(self.centralwidget)
        self.CSstatementswdw_lbl_filter.setGeometry(QtCore.QRect(30, 50, 91, 41))
        self.CSstatementswdw_lbl_filter.setObjectName("CSstatementswdw_lbl_filter")
        self.CSstatementswdw_btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.CSstatementswdw_btn_search.setGeometry(QtCore.QRect(330, 170, 75, 23))
        self.CSstatementswdw_btn_search.setObjectName("CSstatementswdw_btn_search")
        self.CSstatementswdw_lbl_filter_date = QtWidgets.QLabel(self.centralwidget)
        self.CSstatementswdw_lbl_filter_date.setGeometry(QtCore.QRect(30, 100, 47, 14))
        self.CSstatementswdw_lbl_filter_date.setObjectName("CSstatementswdw_lbl_filter_date")
        self.CSstatementswdw_lbl_filter_date_Ttype = QtWidgets.QLabel(self.centralwidget)
        self.CSstatementswdw_lbl_filter_date_Ttype.setGeometry(QtCore.QRect(20, 170, 101, 16))
        self.CSstatementswdw_lbl_filter_date_Ttype.setObjectName("CSstatementswdw_lbl_filter_date_Ttype")
        self.CSstatementswdw_lbl_start = QtWidgets.QLabel(self.centralwidget)
        self.CSstatementswdw_lbl_start.setGeometry(QtCore.QRect(90, 100, 31, 16))
        self.CSstatementswdw_lbl_start.setObjectName("CSstatementswdw_lbl_start")
        self.CSstatementswdw_lbl_end = QtWidgets.QLabel(self.centralwidget)
        self.CSstatementswdw_lbl_end.setGeometry(QtCore.QRect(330, 90, 31, 16))
        self.CSstatementswdw_lbl_end.setObjectName("CSstatementswdw_lbl_end")
        self.CSstatements_Transection_Types_combo = QtWidgets.QComboBox(self.centralwidget)
        self.CSstatements_Transection_Types_combo.setGeometry(QtCore.QRect(160, 170, 91, 22))
        self.CSstatements_Transection_Types_combo.setObjectName("CSstatements_Transection_Types_combo")
        self.CSstatements_Transection_Types_combo.addItem("")
        self.CSstatements_Transection_Types_combo.addItem("")
        self.CSstatements_Transection_Types_combo.addItem("")
        self.CSstatements_Transection_Types_combo.addItem("")
        self.CSstatements_Transection_Types_combo.addItem("")
        self.CSstatementswdw_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.CSstatementswdw_tableWidget.setGeometry(QtCore.QRect(10, 240, 700, 192))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CSstatementswdw_tableWidget.sizePolicy().hasHeightForWidth())
        self.CSstatementswdw_tableWidget.setSizePolicy(sizePolicy)
        self.CSstatementswdw_tableWidget.setObjectName("CSstatementswdw_tableWidget")
        self.CSstatementswdw_tableWidget.setColumnCount(3)
        self.CSstatementswdw_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.CSstatementswdw_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CSstatementswdw_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.CSstatementswdw_tableWidget.setHorizontalHeaderItem(2, item)
        self.dateEdit_end = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_end.setGeometry(QtCore.QRect(400, 90, 110, 22))
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.dateEdit_start = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_start.setGeometry(QtCore.QRect(160, 100, 110, 22))
        self.dateEdit_start.setObjectName("dateEdit_start")
        customer_statements_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(customer_statements_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        customer_statements_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(customer_statements_window)
        self.statusbar.setObjectName("statusbar")
        customer_statements_window.setStatusBar(self.statusbar)

        self.retranslateUi(customer_statements_window)
        QtCore.QMetaObject.connectSlotsByName(customer_statements_window)

    def retranslateUi(self, customer_statements_window):
        _translate = QtCore.QCoreApplication.translate
        customer_statements_window.setWindowTitle(_translate("customer_statements_window", "Customer Bank Statement"))
        self.CSstatementswdw_lbl_heading.setText(_translate("customer_statements_window", "Statements"))
        self.CSstatementswdw_btn_back.setText(_translate("customer_statements_window", "Back"))
        self.CSstatementswdw_lbl_filter.setText(_translate("customer_statements_window", "Filtering Options:"))
        self.CSstatementswdw_btn_search.setText(_translate("customer_statements_window", "Search"))
        self.CSstatementswdw_lbl_filter_date.setText(_translate("customer_statements_window", "Date:"))
        self.CSstatementswdw_lbl_filter_date_Ttype.setText(_translate("customer_statements_window", "Transaction Type:"))
        self.CSstatementswdw_lbl_start.setText(_translate("customer_statements_window", "Start:"))
        self.CSstatementswdw_lbl_end.setText(_translate("customer_statements_window", "End:"))
        self.CSstatements_Transection_Types_combo.setItemText(0, _translate("customer_statements_window", "All"))
        self.CSstatements_Transection_Types_combo.setItemText(1, _translate("customer_statements_window", "Deposit Money"))
        self.CSstatements_Transection_Types_combo.setItemText(2, _translate("customer_statements_window", "Withdraw Money"))
        self.CSstatements_Transection_Types_combo.setItemText(3, _translate("customer_statements_window", "Internal Money Transfer"))
        self.CSstatements_Transection_Types_combo.setItemText(4, _translate("customer_statements_window", "Money Received"))
        item = self.CSstatementswdw_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("customer_statements_window", "Transaction Type"))
        item = self.CSstatementswdw_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("customer_statements_window", "Amount"))
        item = self.CSstatementswdw_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("customer_statements_window", "                        Date                "))
