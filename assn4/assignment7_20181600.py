from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


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

        # Display Window
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # . and = Buttons
        self.dec_button = Button('.', self.button_clicked)
        self.eq_button = Button('=', self.button_clicked)

        # Operator Buttons
        self.mul_button = Button('*', self.button_clicked)
        self.div_button = Button('/', self.button_clicked)
        self.add_button = Button('+', self.button_clicked)
        self.sub_button = Button('-', self.button_clicked)

        # Parentheses Buttons
        self.lpar_button = Button('(', self.button_clicked)
        self.rpar_button = Button(')', self.button_clicked)

        # Clear Button
        self.clear_button = Button('C', self.button_clicked)

        # Layout
        main_layout = QGridLayout()
        main_layout.setSizeConstraint(QLayout.SetFixedSize)

        main_layout.addWidget(self.display, 0, 0, 1, 2)

        # Digital number Layoutn and Buttnos
        num_layout = QGridLayout()
        number_matrix = (3, 3)
        for y in range(number_matrix[1]):
            for x in range(number_matrix[0]):
                num_layout.addWidget(Button(
                    str((number_matrix[1] - y - 1) *
                        number_matrix[0] + x + 1),
                    self.button_clicked),
                                     y, x)
        num_layout.addWidget(Button('0', self.button_clicked),
                             number_matrix[1], 0)

        num_layout.addWidget(self.dec_button, 3, 1)
        num_layout.addWidget(self.eq_button, 3, 2)

        main_layout.addLayout(num_layout, 1, 0)

        op_layout = QGridLayout()

        op_layout.addWidget(self.mul_button, 0, 0)
        op_layout.addWidget(self.div_button, 0, 1)
        op_layout.addWidget(self.add_button, 1, 0)
        op_layout.addWidget(self.sub_button, 1, 1)

        op_layout.addWidget(self.lpar_button, 2, 0)
        op_layout.addWidget(self.rpar_button, 2, 1)

        op_layout.addWidget(self.clear_button, 3, 0)

        main_layout.addLayout(op_layout, 1, 1)

        self.setLayout(main_layout)

        self.setWindowTitle("My Calculator")

    def button_clicked(self):
        sender = self.sender()
        if sender.text() == '=':
            self.display.setText(str(eval(self.display.text())))
        elif sender.text() == 'c':
            self.display.setText('0')
        else:
            if self.display.text()[-1] == '0':
                self.display.setText(self.display.text()[:-1] + sender.text())
                return
            self.display.setText(self.display.text() + sender.text())


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

