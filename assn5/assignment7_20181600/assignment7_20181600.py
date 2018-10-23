from keypad import *
from calcFunctions import factorial, decToBin, binToDec, decToRoman
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QMessageBox




class Button(QToolButton):

    def __init__(self, text, slot):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(slot)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.error_message = 'Error!'
        self.last_len = 1
        self.warn_box = QMessageBox()
        self.warn_box.setIcon(QMessageBox.Warning)
        self.warn_box.setText("Too long")
        # Layout
        main_layout = QGridLayout()
        main_layout.setSizeConstraint(QLayout.SetFixedSize)

        num_layout= QGridLayout()
        op_layout = QGridLayout()
        const_layout = QGridLayout()
        func_layout = QGridLayout()

        button_groups = {
            'num': {'buttons': numPadList, 'layout': num_layout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': op_layout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': const_layout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': func_layout, 'columns': 1},
        }

        main_r = 2
        main_c = 0

        for label in button_groups.keys():
            r = 0
            c = 0
            button_pad = button_groups[label]
            for btn_text in button_pad['buttons']:
                button = Button(btn_text, self.button_clicked)
                button_pad['layout'].addWidget(button, r, c)
                c += 1
                if c >= button_pad['columns']:
                    c = 0
                    r += 1

            main_layout.addLayout(button_groups[label]['layout'], main_r, main_c) 
            main_c += 1
            if main_c >= 2:
                main_c = 0
                main_r += 1

        # Display Window
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(30)

        main_layout.addWidget(self.display, 0, 0, 1, 2)

        self.setLayout(main_layout)

        self.setWindowTitle("My Calculator")

    def button_clicked(self):
        op =  ['+', '-', '*', '/', '.']
        number = [str(x) for x in range(1, 10)]
        sender = self.sender()

        if sender.text() == '=':
            try:
                self.display.setText(str(eval(self.display.text())))
            except SyntaxError:
                self.display.setText(self.error_message)
        elif sender.text() == 'C':
            self.display.setText('0')
        else:
            text = sender.text()
            # process of constant is same as number

            if text in constantList.keys():
                text = '%5f' % constantList[text]
            
            if self.display.text().find(self.error_message) > 0:
                self.display.setText('0')
            if text in functionList:
                try:
                    temp = str(eval(self.display.text()))

                    # for type handling
                    expression = functionList[text].__name__ + '(' + str(temp) + ')'
                    result = eval(expression)
                    self.display.setText(str(result))
                    return
                except:
                    self.display.setText(self.error_message)

            # prevention of '01' or '02'
            if self.display.text() == '0' and text not in op:
                self.display.setText(self.display.text()[:-1] + text)
                return
            # too short
            if len(self.display.text()) < 2:
                self.display.setText(self.display.text() + text)
                return

            # prevention of '+02'
            if self.display.text()[-2] in op and self.display.text()[-1] == '0':
                # by-pass
                if text == '0':
                    return
                # '+2'
                if text in number:
                    self.display.setText(self.display.text()[:-1])
            # prevention of duplicate operator            
            if self.display.text()[-1] in op and text in op:
                return
            self.display.setText(self.display.text() + text)
        if len(self.display.text()) + 0 > self.display.maxLength():
            self.warn_box.show() 

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
