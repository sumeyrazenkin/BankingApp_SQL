# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\90506\Documents\GitHub\BankingApp_SQL\customer_edit_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Customer_infoEdit_window(object):
    def setupUi(self, Customer_infoEdit_window):
        Customer_infoEdit_window.setObjectName("Customer_infoEdit_window")
        Customer_infoEdit_window.resize(600, 700)
        Customer_infoEdit_window.setStyleSheet("background-color: rgb(5, 130, 202);")
        self.centralwidget = QtWidgets.QWidget(Customer_infoEdit_window)
        self.centralwidget.setObjectName("centralwidget")
        self.cseditwdw_lbl_heading = QtWidgets.QLabel(self.centralwidget)
        self.cseditwdw_lbl_heading.setGeometry(QtCore.QRect(110, 20, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.cseditwdw_lbl_heading.setFont(font)
        self.cseditwdw_lbl_heading.setObjectName("cseditwdw_lbl_heading")
        self.cseditwdw_lbl_showname = QtWidgets.QLabel(self.centralwidget)
        self.cseditwdw_lbl_showname.setGeometry(QtCore.QRect(290, 20, 191, 81))
        self.cseditwdw_lbl_showname.setText("")
        self.cseditwdw_lbl_showname.setObjectName("cseditwdw_lbl_showname")
        self.cseditwdw_lbl_headingPers = QtWidgets.QLabel(self.centralwidget)
        self.cseditwdw_lbl_headingPers.setGeometry(QtCore.QRect(90, 140, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cseditwdw_lbl_headingPers.setFont(font)
        self.cseditwdw_lbl_headingPers.setObjectName("cseditwdw_lbl_headingPers")
        self.cseditwdw_lbl_name = QtWidgets.QLabel(self.centralwidget)
        self.cseditwdw_lbl_name.setGeometry(QtCore.QRect(90, 200, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cseditwdw_lbl_name.setFont(font)
        self.cseditwdw_lbl_name.setObjectName("cseditwdw_lbl_name")
        self.cseditwdw_lbl_headingCntc = QtWidgets.QLabel(self.centralwidget)
        self.cseditwdw_lbl_headingCntc.setGeometry(QtCore.QRect(90, 270, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cseditwdw_lbl_headingCntc.setFont(font)
        self.cseditwdw_lbl_headingCntc.setObjectName("cseditwdw_lbl_headingCntc")
        self.cseditwdw_lbl_email = QtWidgets.QLabel(self.centralwidget)
        self.cseditwdw_lbl_email.setGeometry(QtCore.QRect(90, 330, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cseditwdw_lbl_email.setFont(font)
        self.cseditwdw_lbl_email.setObjectName("cseditwdw_lbl_email")
        self.cseditwdw_lbl_headingAcc = QtWidgets.QLabel(self.centralwidget)
        self.cseditwdw_lbl_headingAcc.setGeometry(QtCore.QRect(90, 400, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cseditwdw_lbl_headingAcc.setFont(font)
        self.cseditwdw_lbl_headingAcc.setObjectName("cseditwdw_lbl_headingAcc")
        self.cseditwdw_lbl_password = QtWidgets.QLabel(self.centralwidget)
        self.cseditwdw_lbl_password.setGeometry(QtCore.QRect(90, 460, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cseditwdw_lbl_password.setFont(font)
        self.cseditwdw_lbl_password.setObjectName("cseditwdw_lbl_password")
        self.cseditwdw_btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.cseditwdw_btn_save.setGeometry(QtCore.QRect(210, 550, 180, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cseditwdw_btn_save.setFont(font)
        self.cseditwdw_btn_save.setStyleSheet("QPushButton {\n"
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
        self.cseditwdw_btn_save.setObjectName("cseditwdw_btn_save")
        self.cseditwdw_plntxt_CSname_show = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.cseditwdw_plntxt_CSname_show.setGeometry(QtCore.QRect(230, 210, 151, 31))
        self.cseditwdw_plntxt_CSname_show.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cseditwdw_plntxt_CSname_show.setObjectName("cseditwdw_plntxt_CSname_show")
        self.cseditwdw_plntxt_CSemail_show = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.cseditwdw_plntxt_CSemail_show.setGeometry(QtCore.QRect(230, 340, 151, 31))
        self.cseditwdw_plntxt_CSemail_show.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cseditwdw_plntxt_CSemail_show.setObjectName("cseditwdw_plntxt_CSemail_show")
        self.cseditwdw_plntxt_CSpassword_show = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.cseditwdw_plntxt_CSpassword_show.setGeometry(QtCore.QRect(230, 460, 151, 31))
        self.cseditwdw_plntxt_CSpassword_show.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cseditwdw_plntxt_CSpassword_show.setObjectName("cseditwdw_plntxt_CSpassword_show")
        Customer_infoEdit_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Customer_infoEdit_window)
        self.statusbar.setObjectName("statusbar")
        Customer_infoEdit_window.setStatusBar(self.statusbar)

        self.retranslateUi(Customer_infoEdit_window)
        QtCore.QMetaObject.connectSlotsByName(Customer_infoEdit_window)

    def retranslateUi(self, Customer_infoEdit_window):
        _translate = QtCore.QCoreApplication.translate
        Customer_infoEdit_window.setWindowTitle(_translate("Customer_infoEdit_window", "MainWindow"))
        self.cseditwdw_lbl_heading.setText(_translate("Customer_infoEdit_window", "Hello"))
        self.cseditwdw_lbl_headingPers.setText(_translate("Customer_infoEdit_window", "Personal Information"))
        self.cseditwdw_lbl_name.setText(_translate("Customer_infoEdit_window", "Name:"))
        self.cseditwdw_lbl_headingCntc.setText(_translate("Customer_infoEdit_window", "Contact Information"))
        self.cseditwdw_lbl_email.setText(_translate("Customer_infoEdit_window", "Email:"))
        self.cseditwdw_lbl_headingAcc.setText(_translate("Customer_infoEdit_window", "Account Information"))
        self.cseditwdw_lbl_password.setText(_translate("Customer_infoEdit_window", "Password:"))
        self.cseditwdw_btn_save.setText(_translate("Customer_infoEdit_window", "SAVE"))
 