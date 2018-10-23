from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad import numPadList, operatorList, constantList, functionList
import calcFunctions



class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # buttons creation and placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constantLayout = QGridLayout()
        functionLayout = QGridLayout()
        buttonGroups = {
            'num' : {'buttons': numPadList, 'layout': numLayout, 'columns':3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns':2},
            'constants': {'buttons': constantList, 'layout': constantLayout, 'columns':1},
            'functions': {'buttons': functionList,'layout': functionLayout, 'columns':1},
        }
        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1



        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constantLayout, 2, 0)
        mainLayout.addLayout(functionLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


    def buttonClicked(self):

        button = self.sender()
        key = button.text()

        if key == '=':
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif key == 'C':
            self.display.clear()
        elif key in constantList:
            from keypad import constantappendList
            for i in constantList[i]:
                self.display.setLayout(self.display.layout() + constantapeendList[i])
        elif key in functionList:
            for i in functionList[i]:
                n = self.display.text()
                value = calcFunctions.functionList[i](n)
                self.display.setTest(str(value))

        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

