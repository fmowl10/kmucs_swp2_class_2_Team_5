import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import *


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.str = ""

        # label
        namelbl = QLabel('Name:', self)
        agelbl = QLabel('Age:', self)
        scorelbl = QLabel('Score:', self)
        amountlbl = QLabel('Amount:', self)
        keylbl = QLabel('Key:', self)

        # QLineEdit
        self.nameLE = QLineEdit()
        self.ageLE = QLineEdit()
        self.scoreLE = QLineEdit()
        self.amountLE = QLineEdit()

        # hbox1
        hbox1 = QHBoxLayout()
        hbox1.addWidget(namelbl)
        hbox1.addWidget(self.nameLE)
        hbox1.addWidget(agelbl)
        hbox1.addWidget(self.ageLE)
        hbox1.addWidget(scorelbl)
        hbox1.addWidget(self.scoreLE)

        # QComboBox
        self.keyCB = QComboBox()
        self.keyCB.addItems(['Name', 'Score', 'Age'])

        # hbox2
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(amountlbl)
        hbox2.addWidget(self.amountLE)
        hbox2.addWidget(keylbl)
        hbox2.addWidget(self.keyCB)

        # Buttons
        addButton = QPushButton("Add", self)
        addButton.clicked.connect(self.add)
        delButton = QPushButton("Del", self)
        delButton.clicked.connect(self.delete)
        findButton = QPushButton("Find", self)
        findButton.clicked.connect(self.find)
        incButton = QPushButton("Inc", self)
        incButton.clicked.connect(self.inc)
        showButton = QPushButton("Show")
        showButton.clicked.connect(self.showScoreDB)

        # hbox3
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(addButton)
        hbox3.addWidget(delButton)
        hbox3.addWidget(findButton)
        hbox3.addWidget(incButton)
        hbox3.addWidget(showButton)

        # result
        resultlbl = QLabel('Result:', self)
        self.resultTE = QTextEdit()

        vbox = QVBoxLayout()

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(resultlbl)
        vbox.addWidget(self.resultTE)
        self.setLayout(vbox)
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return
        try:
            self.scoredb = pickle.load(fH)
            for i in self.scoredb:
                i["Score"] = int(i["Score"])
                i["Age"] = int(i["Age"])
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        keyname = self.keyCB.currentText()
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                self.str += str(attr) + "=" + str(p[attr]) + " "
            self.str += '\n'
        self.resultTE.setPlainText(self.str)
        self.str = ""

    def add(self):
        try:
            record = {'Name': self.nameLE.text(), 'Age': int(self.ageLE.text()), 'Score': int(self.scoreLE.text())}
            self.scoredb += [record]
        except ValueError:
            self.resultTE.setPlainText("")
            self.resultTE.setPlainText("Value Error!")
        else:
            self.showScoreDB()

    def find(self):
        name = self.nameLE.text()
        try:
            for p in self.scoredb:
                if p['Name'] == name:
                    for attr in sorted(p):
                        self.str += attr + '=' + str(p[attr]) + ' '
                    self.str += '\n'
                self.resultTE.setPlainText(self.str)
            self.str = ""
        except IndexError:
            self.resultTE.setPlainText("")
            self.resultTE.setPlainText("Index Error!")

    def delete(self):
        try:
            for i in range(len(self.scoredb)):
                for j in self.scoredb:
                    if j['Name'] == self.nameLE.text():
                        self.scoredb.remove(j)
                        break
        except IndexError:
            self.resultTE.setPlainText("")
            self.resultTE.setPlainText("Index Error!")
        else:
            self.showScoreDB()

    def inc(self):
        try:
            for p in self.scoredb:
                if p['Name'] == self.nameLE.text():
                    p['Score'] += int(self.amountLE.text())
        except ValueError:
            self.resultTE.setPlainText("")
            self.resultTE.setPlainText("Value Error!")
        else:
            self.showScoreDB()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
