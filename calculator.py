from PyQt5 import QtWidgets
from pyCalc import Ui_Calculator


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):

    firstNum = None
    # typingSecondNum = True

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.typingSecondNum = True

        # connect buttons
        self.pushButton_0.clicked.connect(self.digit_pressed)
        self.pushButton_1.clicked.connect(self.digit_pressed)
        self.pushButton_2.clicked.connect(self.digit_pressed)
        self.pushButton_3.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)

        self.pushButton_decimal.clicked.connect(self.decimal_pressed)

        self.pushButton_sign.clicked.connect(self.unary_operation_pressed)
        self.pushButton_percent.clicked.connect(self.unary_operation_pressed)

        self.pushButton_add.clicked.connect(self.binary_operation_pressed)
        self.pushButton_minus.clicked.connect(self.binary_operation_pressed)
        self.pushButton_multiply.clicked.connect(self.binary_operation_pressed)
        self.pushButton_divide.clicked.connect(self.binary_operation_pressed)

        self.pushButton_equal.clicked.connect(self.equals_pressed)

        self.pushButton_clear.clicked.connect(self.clear_pressed)

        self.pushButton_add.setCheckable(True)
        self.pushButton_minus.setCheckable(True)
        self.pushButton_multiply.setCheckable(True)
        self.pushButton_divide.setCheckable(True)

    def digit_pressed(self):
        button = self.sender()
        if ((self.pushButton_add.isChecked or self.pushButton_minus.isChecked or self.pushButton_multiply.isChecked
             or self.pushButton_divide.isChecked) and (not self.typingSecondNum)):
            newLabel = format(float(button.text()), '.15g')
            self.typingSecondNum = False # bug is in here
        else:
            if ('.' in self.label.text() and (button.text() == 0)):
                newLabel = format((self.label.text() + button.text()), '.15')
            else:
                newLabel = format(float(self.label.text() + button.text()), '.15g')

        self.label.setText(newLabel)
        self.typingSecondNum = True

    def decimal_pressed(self):
        # add conditional to check for a decimal already in label
        self.label.setText(self.label.text() + '.')

    def unary_operation_pressed(self):
        button = self.sender()

        labelNumber = float(self.label.text())

        if button.text() == '+/-':
            labelNumber = labelNumber * -1
        else: # button text must be %
            labelNumber = labelNumber * 0.01

        newLabel = format(labelNumber, '.15g')
        self.label.setText(newLabel)

    def binary_operation_pressed(self):
        self.typingSecondNum = False
        button = self.sender()

        self.firstNum = float(self.label.text())

        button.setChecked(True)

    def equals_pressed(self):

        secondNum = float(self.label.text())

        if self.pushButton_add.isChecked():
            labelNumber = self.firstNum + secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_add.setChecked(False)
        elif self.pushButton_minus.isChecked():
            labelNumber = self.firstNum - secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_minus.setChecked(False)
        elif self.pushButton_multiply.isChecked():
            labelNumber = self.firstNum * secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_multiply.setChecked(False)
        elif self.pushButton_divide.isChecked():
            labelNumber = self.firstNum / secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_divide.setChecked(False)

        self.typingSecondNum = False

    def clear_pressed(self):
        self.pushButton_add.setChecked(False)
        self.pushButton_minus.setChecked(False)
        self.pushButton_multiply.setChecked(False)
        self.pushButton_divide.setChecked(False)

        self.typingSecondNum = False

        self.label.setText('0')


