import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QMessageBox)
from score_db import ScoreDB

class ScoreDB_Gui(QWidget):

    def __init__(self):
        super().__init__()

        self.is_first_shown = False
        self.db = ScoreDB('assignment6.dat')
        self.db.read()

        self.initUI()

    def initUI(self):
        # set window size and title
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        # to send warning to user
        self.warning_msg = QMessageBox()
        self.warning_msg.setIcon(QMessageBox.Warning)
        self.warning_msg.setText("empty DB")
        self.warning_msg.setDetailedText("Add Student's Data")
        self.warning_msg.setWindowTitle(self.windowTitle())
        self.warning_msg.setStandardButtons(QMessageBox.Ok)

        # to send is Ok or not
        self.ask_msg = QMessageBox()
        self.ask_msg.setIcon(QMessageBox.Question)
        self.ask_msg.setText("are you sure?")
        self.ask_msg.setWindowTitle(self.windowTitle())
        self.ask_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # first row is user input
        name_lbl = QLabel('Name:')
        age_lbl = QLabel('Age:')
        score_lbl = QLabel('Score:')

        self.name_edit = QLineEdit()
        self.age_edit = QLineEdit()
        self.score_edit = QLineEdit()

        vbox = QVBoxLayout()
        user_data_hbox = QHBoxLayout()

        user_data_hbox.addWidget(name_lbl)
        user_data_hbox.addWidget(self.name_edit)
        user_data_hbox.addWidget(age_lbl)
        user_data_hbox.addWidget(self.age_edit)
        user_data_hbox.addWidget(score_lbl)
        user_data_hbox.addWidget(self.score_edit)

        vbox.addLayout(user_data_hbox)
        # end of first row

        # second row is key combo and amount
        amount_lbl = QLabel('Amount:')
        self.amount_edit = QLineEdit()

        sort_key_lbl = QLabel('Key')
        self.sort_key_combo = QComboBox()
        self.sort_key_combo.addItems(ScoreDB.ColumnName)

        key_and_amount_hbox = QHBoxLayout()
        key_and_amount_hbox.addStretch(1)

        key_and_amount_hbox.addWidget(amount_lbl)
        key_and_amount_hbox.addWidget(self.amount_edit)
        key_and_amount_hbox.addWidget(sort_key_lbl)
        key_and_amount_hbox.addWidget(self.sort_key_combo)

        vbox.addLayout(key_and_amount_hbox)
        # end of second row

        # third row is 5 push buttons
        # command buttons
        self.add_btn = QPushButton('Add')
        self.del_btn = QPushButton('Del')
        self.find_btn = QPushButton('Find')
        self.inc_btn = QPushButton('Inc')
        self.show_btn = QPushButton('show')

        command_hbox = QHBoxLayout()
        command_hbox.addStretch(1)

        command_hbox.addWidget(self.add_btn)
        command_hbox.addWidget(self.del_btn)
        command_hbox.addWidget(self.find_btn)
        command_hbox.addWidget(self.inc_btn)
        command_hbox.addWidget(self.show_btn)

        vbox.addLayout(command_hbox)
        # end of third row

        # last row is label and text edit
        result_lbl = QLabel('Result:')
        self.result_txt = QTextEdit()
        self.result_txt.setReadOnly(True)

        result_hbox = QHBoxLayout()
        result_vbox = QVBoxLayout()
        result_vbox.addWidget(result_lbl)

        result_vbox.addStretch(1)
        result_hbox.addLayout(result_vbox)
        result_hbox.addWidget(self.result_txt)

        vbox.addLayout(result_hbox)
        # end of last row

        self.setLayout(vbox)
        self.is_first_shown = True
        self.connect_events()

        self.show()

    def connect_events(self):
        self.add_btn.clicked.connect(self.add_btn_on_clicked)
        self.show_btn.clicked.connect(self.show_btn_on_clicked)
        self.del_btn.clicked.connect(self.del_btn_on_clicked)
        self.find_btn.clicked.connect(self.find_btn_on_clicked)
        self.inc_btn.clicked.connect(self.inc_btn_on_clicked)

    def closeEvent(self, event):
        self.db.write()
        
    def showEvent(self, event):
        # it must execute one time.
        if self.is_first_shown:
            self.showScoreDB(self.db.show('Name'))

    def show_btn_on_clicked(self):
        key = self.sort_key_combo.currentText()
        self.showScoreDB(self.db.show(key))

    def add_btn_on_clicked(self):
        if self.db.add_record(self.name_edit.text(),
                        self.age_edit.text(), self.score_edit.text()):
            self.show_btn_on_clicked()
        else:
            self.show_message('input right name and age and score')

        self.name_edit.clear()
        self.age_edit.clear()
        self.score_edit.clear()

    def del_btn_on_clicked(self):
        self.ask_msg.show()
        self.ask_msg.buttonClicked.connect(self.del_data)
        self.name_edit.clear()

    def del_data(self, event):
        if self.ask_msg.result() == QMessageBox.Yes:
            if not self.db.del_record(self.name_edit.text()):
                self.show_message('input right name')
            self.show_btn_on_clicked()

    def find_btn_on_clicked(self):
        finded_list = self.db.find(self.name_edit.text())
        if not finded_list:
            self.result_txt.clear()
            self.show_message('not found')
        else:
            self.showScoreDB(finded_list)

    def inc_btn_on_clicked(self):
        if not self.db.inc(self.name_edit.text(), self.amount_edit.text()):
           self.show_message("input right name or amount")
           self.amount_edit.clear()
        self.show_btn_on_clicked()
        self.name_edit.clear()
        self.amount_edit.clear()

    def show_message(self, msg):
        self.warning_msg.setText(msg)
        self.warning_msg.show()

    def showScoreDB(self, listed_db):
        self.result_txt.clear()
        if listed_db is None or not listed_db:
            self.result_txt.setText("db is emtpy")
        if not listed_db:
            self.warning_msg.show()
        self.result_txt.clear()
        for record in listed_db:
            temp_str = ''
            for column in ScoreDB.ColumnName:
                temp_str += '%s = %-20s' % (column, str(record[column]))
            self.result_txt.append(temp_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB_Gui()
    sys.exit(app.exec_())
