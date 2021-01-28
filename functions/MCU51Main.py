from PySide2 import QtCore
from functions.functionsUI.MCU51UI import Ui_MainWindow
from functions.functionsUI import MCU51UI
from PyQt5 import QtWidgets
import sys


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setStyleSheet("QPushButton{background-color: rgb(235, 235, 255);border:2px groove "
                           "gray;border-radius:10px;padding:4px 20px;border-style: outset;} "
                           "QPushButton:hover{background-color:rgb(229, 241, 251); color: black;}"
                           "QPushButton:pressed{background-color:rgb(204, 228, 247);border-style: inset;}"
                           "QLineEdit{background-color: rgb(240, 255, 255);border:2px groove "
                           "gray;border-radius:10px;padding:4px 20px;border-style: outset;}"
                           )  # 设置相应按钮
        self.STgenerate_btn.clicked.connect(self.STgenerate)

    def STgenerate(self):
        Frequency = eval(self.STsysClockFqyInput.text())
        timeLength = eval(self.STtimeLengthInput.text())  # 获取时长和系统时钟频率
        timeStep = 1 / (Frequency * 1000000)
        timeStep = timeStep * 12  # 12个时钟周期代表一个机器周期
        if Frequency == 12:
            if timeLength == 500000:
                self.printSTCode(23, 205, 160, 500)
            elif timeLength == 200000:
                self.printSTCode(10, 31, 147, 200)
            elif timeLength == 1000000:
                self.printSTCode(46, 153, 245, 1000)
            elif timeLength == 10:
                self.STdisplay.setText("void delay_10us(){")
                self.STdisplay.append("    _NOP_();")
                self.STdisplay.append("    _NOP_();")
                self.STdisplay.append("    _NOP_();")
                self.STdisplay.append("    _NOP_();")
                self.STdisplay.append("    _NOP_();")
                self.STdisplay.append("    _NOP_();")
                self.STdisplay.append("}")
            else:
                self.STdisplay.setText("无对应的延时时间程序存储")
        elif Frequency == 11.0592:  # 由于经常要用的就这几个，所以直接写了，精确定时写在定时器那里
            if timeLength == 500000:
                self.printSTCode(22, 3, 227, 500)
            elif timeLength == 200000:
                self.printSTCode(9, 104, 139, 200)
            elif timeLength == 100000:
                self.printSTCode(5, 52, 195, 100)
            elif timeLength == 50000:
                self.printSTCode(3, 26, 223, 50)
            elif timeLength == 20000:
                self.printSTCode(1, 216, 35, 20)
            else:
                self.STdisplay.setText("无对应的延时时间程序存储")

    def printSTCode(self, i, j, k, length):
        self.STdisplay.setText("void delay_" + str(length) + "ms(){//@11.0592")
        self.STdisplay.append("    unsigned char i, j, k;")
        self.STdisplay.append("    _nop_();\n    _nop_();")
        self.STdisplay.append("    for(i = " + str(i) + "; i > 0; i--)")
        self.STdisplay.append("        for(j = " + str(j) + "; j > 0; j--)")
        self.STdisplay.append("            for(k = " + str(k) + "; k > 0; k--);")
        self.STdisplay.append("}")
