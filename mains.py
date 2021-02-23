import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QRadioButton, QLabel
from PyQt5.uic import loadUi
class login(QDialog):
    def __init__(self):
        super(login,self).__init__()
        loadUi("login.ui",self)
        self.setWindowTitle("Close")
        self.LoginButton.clicked.connect(self.loginfunction)
        self.setWindowTitle("Close Window")
        self.Pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.gotocreat)
        self.LoginButton.clicked.connect(sys.exit)




    def loginfunction(self):
        email = self.Email.text()
        password = self.Pass.text()
        print(f"Successfully logged with email: {email} and Password: {password}")

    def gotocreat(self):
        creatacc = creatAccount()
        widget.addWidget(creatacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class creatAccount(QDialog):
    def __init__(self):
        super(creatAccount,self).__init__()
        loadUi("creatAccount.ui",self)
        widget.setFixedWidth(480)
        widget.setFixedHeight(620)

        self.creatAcc.clicked.connect(self.creatAccFun)
        self.Pass_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Pass_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.backtologin.clicked.connect(self.gotoback)
        self.b1 = QRadioButton("Male")
        self.creatAcc.clicked.connect(sys.exit)

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print("Country is %s" % (radioButton.country))

    def gotoback(self):
        creatacc = login()
        widget.addWidget(creatacc)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def creatAccFun(self):
        firstname = self.firstName.text()
        familyname = self.familyName.text()
        email = self.Email.text()
        if self.Pass_2.text()==self.Pass_3.text():
            Pass = self.Pass_2.text()
            print("seccsucfly created! \nfirstName:",firstname,
                  "\nFamilyname:",familyname,
                  "\nemail:",email,
                  "\npassword:",Pass)
        else:print("failed signup!!!")



app=QApplication(sys.argv)
mainWin=login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainWin)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec()


