# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/melike/Documents/GitHub/BankingApp_SQL/admin_statements_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_admin_statements_window(object):
    def setupUi(self, admin_statements_window):
        admin_statements_window.setObjectName("admin_statements_window")
        admin_statements_window.setWindowModality(QtCore.Qt.ApplicationModal)
        admin_statements_window.resize(600, 700)
        admin_statements_window.setMinimumSize(QtCore.QSize(600, 700))
        admin_statements_window.setMaximumSize(QtCore.QSize(600, 700))
        admin_statements_window.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        admin_statements_window.setAcceptDrops(False)
        admin_statements_window.setStyleSheet("background-color: rgb(241, 242, 248);")
        admin_statements_window.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(admin_statements_window)
        self.centralwidget.setObjectName("centralwidget")
        self.ADstatementswdw_lbl_heading = QtWidgets.QLabel(self.centralwidget)
        self.ADstatementswdw_lbl_heading.setGeometry(QtCore.QRect(30, 0, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ADstatementswdw_lbl_heading.setFont(font)
        self.ADstatementswdw_lbl_heading.setStyleSheet("color: rgb(0, 51, 51);")
        self.ADstatementswdw_lbl_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.ADstatementswdw_lbl_heading.setObjectName("ADstatementswdw_lbl_heading")
        self.ADstatementswdw_btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.ADstatementswdw_btn_back.setEnabled(True)
        self.ADstatementswdw_btn_back.setGeometry(QtCore.QRect(210, 590, 180, 60))
        self.ADstatementswdw_btn_back.setMinimumSize(QtCore.QSize(180, 60))
        self.ADstatementswdw_btn_back.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ADstatementswdw_btn_back.setFont(font)
        self.ADstatementswdw_btn_back.setStyleSheet("QPushButton{\n"
"color: rgb(39, 82, 97);\n"
"background-color: rgb(187, 207, 237);\n"
"border:2px solid rgb(123, 169, 191);\n"
"border-radius:20px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(225, 229, 241);\n"
"     border:2px solid rgb(196, 218, 245);\n"
"}\n"
"   ")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/back-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ADstatementswdw_btn_back.setIcon(icon)
        self.ADstatementswdw_btn_back.setIconSize(QtCore.QSize(40, 40))
        self.ADstatementswdw_btn_back.setObjectName("ADstatementswdw_btn_back")
        self.ADstatementswdw_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.ADstatementswdw_tableWidget.setGeometry(QtCore.QRect(20, 280, 561, 301))
        self.ADstatementswdw_tableWidget.setStyleSheet("background-color: rgb(225, 229, 241);")
        self.ADstatementswdw_tableWidget.setObjectName("ADstatementswdw_tableWidget")
        self.ADstatementswdw_tableWidget.setColumnCount(8)
        self.ADstatementswdw_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(187, 207, 237))
        self.ADstatementswdw_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(210, 218, 243))
        self.ADstatementswdw_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(187, 207, 237))
        self.ADstatementswdw_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(210, 218, 243))
        self.ADstatementswdw_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(187, 207, 237))
        self.ADstatementswdw_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(210, 218, 243))
        self.ADstatementswdw_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(187, 207, 237))
        self.ADstatementswdw_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(210, 218, 243))
        self.ADstatementswdw_tableWidget.setHorizontalHeaderItem(7, item)
        self.ADstatementswdw_tableWidget.horizontalHeader().setDefaultSectionSize(65)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 40, 521, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ADstatementswdw_lbl_end = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ADstatementswdw_lbl_end.setMinimumSize(QtCore.QSize(109, 0))
        self.ADstatementswdw_lbl_end.setMaximumSize(QtCore.QSize(110, 150))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.ADstatementswdw_lbl_end.setFont(font)
        self.ADstatementswdw_lbl_end.setAlignment(QtCore.Qt.AlignCenter)
        self.ADstatementswdw_lbl_end.setObjectName("ADstatementswdw_lbl_end")
        self.gridLayout_2.addWidget(self.ADstatementswdw_lbl_end, 0, 2, 1, 1)
        self.ADstatementswdw_lbl_start = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ADstatementswdw_lbl_start.setMinimumSize(QtCore.QSize(110, 30))
        self.ADstatementswdw_lbl_start.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.ADstatementswdw_lbl_start.setFont(font)
        self.ADstatementswdw_lbl_start.setAlignment(QtCore.Qt.AlignCenter)
        self.ADstatementswdw_lbl_start.setObjectName("ADstatementswdw_lbl_start")
        self.gridLayout_2.addWidget(self.ADstatementswdw_lbl_start, 0, 0, 1, 1)
        self.ADstatementswdw_dateEdit_start = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.ADstatementswdw_dateEdit_start.setMinimumSize(QtCore.QSize(0, 30))
        self.ADstatementswdw_dateEdit_start.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ADstatementswdw_dateEdit_start.setStyleSheet("background-color: rgb(225, 229, 241);")
        self.ADstatementswdw_dateEdit_start.setObjectName("ADstatementswdw_dateEdit_start")
        self.gridLayout_2.addWidget(self.ADstatementswdw_dateEdit_start, 0, 1, 1, 1)
        self.ADstatementswdw_dateEdit_end = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.ADstatementswdw_dateEdit_end.setMinimumSize(QtCore.QSize(0, 30))
        self.ADstatementswdw_dateEdit_end.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ADstatementswdw_dateEdit_end.setStyleSheet("background-color: rgb(225, 229, 241);")
        self.ADstatementswdw_dateEdit_end.setObjectName("ADstatementswdw_dateEdit_end")
        self.gridLayout_2.addWidget(self.ADstatementswdw_dateEdit_end, 0, 3, 1, 1)
        self.ADstatementswdw_lbl_filter_date_Ttype = QtWidgets.QLabel(self.centralwidget)
        self.ADstatementswdw_lbl_filter_date_Ttype.setGeometry(QtCore.QRect(40, 230, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ADstatementswdw_lbl_filter_date_Ttype.setFont(font)
        self.ADstatementswdw_lbl_filter_date_Ttype.setObjectName("ADstatementswdw_lbl_filter_date_Ttype")
        self.ADstatementswdw_combobox_Ttype = QtWidgets.QComboBox(self.centralwidget)
        self.ADstatementswdw_combobox_Ttype.setGeometry(QtCore.QRect(200, 240, 131, 30))
        self.ADstatementswdw_combobox_Ttype.setMinimumSize(QtCore.QSize(0, 30))
        self.ADstatementswdw_combobox_Ttype.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ADstatementswdw_combobox_Ttype.setStyleSheet("background-color: rgb(225, 229, 241);")
        self.ADstatementswdw_combobox_Ttype.setObjectName("ADstatementswdw_combobox_Ttype")
        self.ADstatementswdw_combobox_Ttype.addItem("")
        self.ADstatementswdw_combobox_Ttype.addItem("")
        self.ADstatementswdw_combobox_Ttype.addItem("")
        self.ADstatementswdw_combobox_Ttype.addItem("")
        self.ADstatementswdw_combobox_Ttype.addItem("")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 90, 341, 140))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ADstatementswdw_lnedit_name = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.ADstatementswdw_lnedit_name.setMinimumSize(QtCore.QSize(0, 30))
        self.ADstatementswdw_lnedit_name.setMaximumSize(QtCore.QSize(280, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ADstatementswdw_lnedit_name.setFont(font)
        self.ADstatementswdw_lnedit_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ADstatementswdw_lnedit_name.setObjectName("ADstatementswdw_lnedit_name")
        self.gridLayout_3.addWidget(self.ADstatementswdw_lnedit_name, 1, 2, 1, 1)
        self.ADstatementswdw_lbl_filter_email = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.ADstatementswdw_lbl_filter_email.setMinimumSize(QtCore.QSize(110, 30))
        self.ADstatementswdw_lbl_filter_email.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ADstatementswdw_lbl_filter_email.setFont(font)
        self.ADstatementswdw_lbl_filter_email.setStyleSheet("color: rgb(0, 51, 51);")
        self.ADstatementswdw_lbl_filter_email.setObjectName("ADstatementswdw_lbl_filter_email")
        self.gridLayout_3.addWidget(self.ADstatementswdw_lbl_filter_email, 3, 0, 1, 1)
        self.ADstatementswdw_lnedit_email = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.ADstatementswdw_lnedit_email.setMinimumSize(QtCore.QSize(0, 30))
        self.ADstatementswdw_lnedit_email.setMaximumSize(QtCore.QSize(280, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ADstatementswdw_lnedit_email.setFont(font)
        self.ADstatementswdw_lnedit_email.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ADstatementswdw_lnedit_email.setObjectName("ADstatementswdw_lnedit_email")
        self.gridLayout_3.addWidget(self.ADstatementswdw_lnedit_email, 3, 2, 1, 1)
        self.ADstatementswdw_lnedit_amount = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.ADstatementswdw_lnedit_amount.setMinimumSize(QtCore.QSize(0, 30))
        self.ADstatementswdw_lnedit_amount.setMaximumSize(QtCore.QSize(280, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ADstatementswdw_lnedit_amount.setFont(font)
        self.ADstatementswdw_lnedit_amount.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ADstatementswdw_lnedit_amount.setObjectName("ADstatementswdw_lnedit_amount")
        self.gridLayout_3.addWidget(self.ADstatementswdw_lnedit_amount, 2, 2, 1, 1)
        self.lbl_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_3.setMinimumSize(QtCore.QSize(20, 30))
        self.lbl_3.setMaximumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_3.setFont(font)
        self.lbl_3.setStyleSheet("color: rgb(0, 51, 51);")
        self.lbl_3.setObjectName("lbl_3")
        self.gridLayout_3.addWidget(self.lbl_3, 1, 1, 1, 1)
        self.lbl_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_2.setMinimumSize(QtCore.QSize(20, 30))
        self.lbl_2.setMaximumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_2.setFont(font)
        self.lbl_2.setStyleSheet("color: rgb(0, 51, 51);")
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout_3.addWidget(self.lbl_2, 2, 1, 1, 1)
        self.ADstatementswdw_lnedit_csid = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.ADstatementswdw_lnedit_csid.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ADstatementswdw_lnedit_csid.sizePolicy().hasHeightForWidth())
        self.ADstatementswdw_lnedit_csid.setSizePolicy(sizePolicy)
        self.ADstatementswdw_lnedit_csid.setMinimumSize(QtCore.QSize(250, 30))
        self.ADstatementswdw_lnedit_csid.setMaximumSize(QtCore.QSize(280, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ADstatementswdw_lnedit_csid.setFont(font)
        self.ADstatementswdw_lnedit_csid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ADstatementswdw_lnedit_csid.setObjectName("ADstatementswdw_lnedit_csid")
        self.gridLayout_3.addWidget(self.ADstatementswdw_lnedit_csid, 0, 2, 1, 1)
        self.lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl.setMinimumSize(QtCore.QSize(20, 30))
        self.lbl.setMaximumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setStyleSheet("color: rgb(0, 51, 51);")
        self.lbl.setObjectName("lbl")
        self.gridLayout_3.addWidget(self.lbl, 0, 1, 1, 1)
        self.ADstatementswdw_lbl_filter_amount = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.ADstatementswdw_lbl_filter_amount.setMinimumSize(QtCore.QSize(110, 30))
        self.ADstatementswdw_lbl_filter_amount.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ADstatementswdw_lbl_filter_amount.setFont(font)
        self.ADstatementswdw_lbl_filter_amount.setStyleSheet("color: rgb(0, 51, 51);")
        self.ADstatementswdw_lbl_filter_amount.setObjectName("ADstatementswdw_lbl_filter_amount")
        self.gridLayout_3.addWidget(self.ADstatementswdw_lbl_filter_amount, 2, 0, 1, 1)
        self.lbl_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_4.setMinimumSize(QtCore.QSize(20, 30))
        self.lbl_4.setMaximumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_4.setFont(font)
        self.lbl_4.setStyleSheet("color: rgb(0, 51, 51);")
        self.lbl_4.setObjectName("lbl_4")
        self.gridLayout_3.addWidget(self.lbl_4, 3, 1, 1, 1)
        self.ADstatementswdw_lbl_filter_name = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.ADstatementswdw_lbl_filter_name.setMinimumSize(QtCore.QSize(110, 30))
        self.ADstatementswdw_lbl_filter_name.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ADstatementswdw_lbl_filter_name.setFont(font)
        self.ADstatementswdw_lbl_filter_name.setStyleSheet("color: rgb(0, 51, 51);")
        self.ADstatementswdw_lbl_filter_name.setObjectName("ADstatementswdw_lbl_filter_name")
        self.gridLayout_3.addWidget(self.ADstatementswdw_lbl_filter_name, 1, 0, 1, 1)
        self.ADstatementswdw_lbl_filter_csid = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.ADstatementswdw_lbl_filter_csid.setMinimumSize(QtCore.QSize(110, 30))
        self.ADstatementswdw_lbl_filter_csid.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ADstatementswdw_lbl_filter_csid.setFont(font)
        self.ADstatementswdw_lbl_filter_csid.setStyleSheet("color: rgb(0, 51, 51);")
        self.ADstatementswdw_lbl_filter_csid.setObjectName("ADstatementswdw_lbl_filter_csid")
        self.gridLayout_3.addWidget(self.ADstatementswdw_lbl_filter_csid, 0, 0, 1, 1)
        self.ADstatementswdw_btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.ADstatementswdw_btn_search.setGeometry(QtCore.QRect(390, 220, 180, 50))
        self.ADstatementswdw_btn_search.setMinimumSize(QtCore.QSize(180, 50))
        self.ADstatementswdw_btn_search.setMaximumSize(QtCore.QSize(180, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ADstatementswdw_btn_search.setFont(font)
        self.ADstatementswdw_btn_search.setStyleSheet("QPushButton{\n"
"color: rgb(39, 82, 97);\n"
"background-color: rgb(211, 224, 243);\n"
"border:2px solid rgb(123, 169, 191);\n"
"border-radius:20px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(225, 229, 241);\n"
"     border:2px solid rgb(196, 218, 245);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ADstatementswdw_btn_search.setIcon(icon1)
        self.ADstatementswdw_btn_search.setIconSize(QtCore.QSize(35, 35))
        self.ADstatementswdw_btn_search.setObjectName("ADstatementswdw_btn_search")
        admin_statements_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(admin_statements_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        admin_statements_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(admin_statements_window)
        self.statusbar.setObjectName("statusbar")
        admin_statements_window.setStatusBar(self.statusbar)

        self.retranslateUi(admin_statements_window)
        QtCore.QMetaObject.connectSlotsByName(admin_statements_window)

    def retranslateUi(self, admin_statements_window):
        _translate = QtCore.QCoreApplication.translate
        admin_statements_window.setWindowTitle(_translate("admin_statements_window", "Customer Bank Statement"))
        self.ADstatementswdw_lbl_heading.setText(_translate("admin_statements_window", "Statements"))
        self.ADstatementswdw_btn_back.setText(_translate("admin_statements_window", "  Back"))
        item = self.ADstatementswdw_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("admin_statements_window", "ID"))
        item = self.ADstatementswdw_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("admin_statements_window", "Name"))
        item = self.ADstatementswdw_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("admin_statements_window", "Email"))
        item = self.ADstatementswdw_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("admin_statements_window", "Amount"))
        item = self.ADstatementswdw_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("admin_statements_window", "Type"))
        item = self.ADstatementswdw_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("admin_statements_window", "Receiver"))
        item = self.ADstatementswdw_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("admin_statements_window", "Date"))
        item = self.ADstatementswdw_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("admin_statements_window", "Balance"))
        self.ADstatementswdw_lbl_end.setText(_translate("admin_statements_window", "Date End"))
        self.ADstatementswdw_lbl_start.setText(_translate("admin_statements_window", "Date Start"))
        self.ADstatementswdw_lbl_filter_date_Ttype.setText(_translate("admin_statements_window", "Transaction Type"))
        self.ADstatementswdw_combobox_Ttype.setItemText(0, _translate("admin_statements_window", "All"))
        self.ADstatementswdw_combobox_Ttype.setItemText(1, _translate("admin_statements_window", "Deposit Money"))
        self.ADstatementswdw_combobox_Ttype.setItemText(2, _translate("admin_statements_window", "Withdraw Money"))
        self.ADstatementswdw_combobox_Ttype.setItemText(3, _translate("admin_statements_window", "Internal Money Transfer"))
        self.ADstatementswdw_combobox_Ttype.setItemText(4, _translate("admin_statements_window", "Money Received"))
        self.ADstatementswdw_lbl_filter_email.setText(_translate("admin_statements_window", "Email"))
        self.lbl_3.setText(_translate("admin_statements_window", ":"))
        self.lbl_2.setText(_translate("admin_statements_window", ":"))
        self.lbl.setText(_translate("admin_statements_window", ":"))
        self.ADstatementswdw_lbl_filter_amount.setText(_translate("admin_statements_window", "Amount"))
        self.lbl_4.setText(_translate("admin_statements_window", ":"))
        self.ADstatementswdw_lbl_filter_name.setText(_translate("admin_statements_window", "Name"))
        self.ADstatementswdw_lbl_filter_csid.setText(_translate("admin_statements_window", "Customer ID"))
        self.ADstatementswdw_btn_search.setText(_translate("admin_statements_window", "  SEARCH"))
