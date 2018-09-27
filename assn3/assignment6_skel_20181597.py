import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()


        addButton.clicked.connect(self.addButton_clicked)
        delButton.clicked.connect(self.delButton_clicked)
        #delButton.clicked.connect(self.findButton_clicked)
        delButton.clicked.connect(self.incButton_clicked)
        #delButton.clicked.connect(self.showButton_clicked)



    def initUI(self):

        # 라벨(글자)
        lbName = QLabel('Name:')
        lbAge = QLabel('Age:')
        lbScore = QLabel('Score:')

        # 값 입력창
        nameEdit = QLineEdit().text()
        ageEdit = QLineEdit()
        scoreEdit = QLineEdit()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(lbName)
        hbox1.addWidget(nameEdit)
        hbox1.addWidget(lbAge)
        hbox1.addWidget(ageEdit)
        hbox1.addWidget(lbScore)
        hbox1.addWidget(scoreEdit)


        # 라벨
        lbAmount = QLabel('Amount:')
        lbKey = QLabel('Key:')

        # 값 입력창
        amountEdit = QLineEdit()

        # 정렬 키
        keyBox = QComboBox()
        keyBox.addItems(['Name', 'Age', 'Score'])


        hbox2 = QHBoxLayout()
        hbox2.addWidget(lbAmount)
        hbox2.addWidget(amountEdit)
        hbox2.addWidget(lbKey)
        hbox2.addWidget(keyBox)


        # 명령 버튼
        addButton = QPushButton("Add")
        delButton = QPushButton("Del")
        findButton = QPushButton("Find")
        incButton = QPushButton("Inc")
        showButton = QPushButton("Show")

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(addButton)
        hbox3.addWidget(delButton)
        hbox3.addWidget(findButton)
        hbox3.addWidget(incButton)
        hbox3.addWidget(showButton)


        # 결과 화면
        lbResult = QLabel('Result:')
        resultEdit = QTextEdit()

        hbox4 = QHBoxLayout()
        hbox4.addWidget(lbResult)
        hbox4.addStretch(1)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(resultEdit)


        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)


        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
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
            self.scoredb =  pickle.load(fH)
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
        pass


    # add
    def addButton_clicked(self):
        record = {'Name': nameEdit, 'Age': ageEdit, 'Score': scoreEdit}
        scdb += [record]

    # del
    def delButton_clicked(self):
        for p in list(scdb):
            if p['Name'] == nameEdit
                scdb.remove(p)
                continue

    '''
    # find
    def findButton_clicked(self):
        for p in scdb:
            if p['Name'] == nameEdit:
                for q in sorted(p):
                    print(q + "=" + p[q], end=' ')
    '''

    # inc
    def incButton_clicked(self):
        for p in scdb:
            if p['Name'] == nameEdit:
                p['Score'] = str(int(p['Score']) + int(amountEdit))

    '''
    # show
    def showButton_clicked(self):
        
    '''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())


