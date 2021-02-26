import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QRadioButton, QLabel
from PyQt5.uic import loadUi
import sqlite3
import re
import time

class login(QDialog):
    def __init__(self):
        super(login,self).__init__()
        loadUi("login.ui",self)
        self.setWindowTitle("Close")
        self.LoginButton.clicked.connect(self.loginfunction)
        self.Pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.gotocreat)
        self.invalidLogin.setVisible(False)


    def loginfunction(self):
            email = self.Email.text()
            password = self.Pass.text()

            conn = sqlite3.connect('tut.db')
            cursor = conn.cursor()

            cursor.execute("SELECT email,password FROM student")
            val = cursor.fetchall()

            if len(val) >= 1:
                for x in val:
                    if email in x[0] and password in x[1]:
                        print("welcome ")
                    else:
                        pass
            else:
                print('No user Found')

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
        self.invalidLabel_2.setVisible(False)
        self.invalidLabel.setVisible(False)
        self.creatAcc.clicked.connect(self.creatAccFun)
        self.Pass_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Pass_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.backtologin.clicked.connect(self.gotoback)
        self.invalidLabel.clicked.connect(self.popMessage)
        self.invalidLabel_2.clicked.connect(self.popMessage)

    def creatAccFun(self):
        firstname = (self.firstName.text()).lower()
        familyname = (self.familyName.text()).lower()
        email = (self.Email.text()).lower()
        if self.passCheck()==True:
            Pass = self.Pass_2.text()
            conn = sqlite3.connect("tut.db")
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS student(email TEXT,firstname TEXT,familyname TEXT,password TEXT)")
            c.execute("INSERT INTO student(email,firstname,familyname,password) VALUES (?, ?, ?, ?)", (email, firstname, familyname, Pass))
            conn.commit()
            c.close()
            conn.close()
            print("the value is inserted successfuly!")
            self.gotoback()
        else:
            self.invalidLabel.setVisible(True)
            self.invalidLabel_2.setVisible(True)
    def passCheck(self):
        password = self.Pass_2.text()
        if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password) and (self.Pass_2.text()==self.Pass_3.text()) and ((4<len(self.Pass_2.text())<12) and (4<len(self.Pass_3.text())<12)):
            return True
        else:
            print("\npassword must be >6 and contain A-Z,a-z,0-9 ... ",self.Pass_2.text(),self.Pass_3.text(),len(self.Pass_2.text()))
            return False

    def gotoback(self):
        creatacc = login()
        widget.addWidget(creatacc)
        widget.setCurrentIndex(widget.currentIndex() - 1)


    def popMessage(self):
        msg = message()
        widget.addWidget(msg)
        widget.setCurrentIndex(widget.currentIndex()+1)

class message(QDialog):
    def __init__(self):
        super(message,self).__init__()
        loadUi("message.ui",self)
        widget.setFixedWidth(480)
        widget.setFixedHeight(620)
        self.backtocreat.clicked.connect(self.gotoback2)
    def gotoback2(self):
        g = creatAccount()
        widget.addWidget(g)
        widget.setCurrentIndex(widget.currentIndex() - 1)

app=QApplication(sys.argv)
mainWin=login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainWin)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec()





"""
#-->data base connection
conn = sqlite3.connect("tut.db")
c = conn.cursor()

def creatTable():
    c.execute("CREATE TABLE IF NOT EXISTS student(name TEXT,age TEXT,password TEXT)")

def data_entery():
    x=str(input("here"))
    y=str(input("here2"))
    z=str(input("here3"))
    c.execute("INSERT INTO student(name,age,password) VALUES (?, ?, ?)",(x,y,z))
    conn.commit()
    c.close()
    conn.close()
def read_from_db():
    c.execute("SELECT * FROM student")


creatTable()
data_entery()

"""