from PySide2 import QtCore
from UI.mainUI import Ui_MainWindow
from functions.functionsUI import MCU51UI
import functions.MCU51Main as MCUFunc
from PyQt5 import QtWidgets
import sys


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    user_name = "齐承文"

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.set_background_image()
        self.MCU51_btn.clicked.connect(self.MCU51Entry)


    def MCU51Entry(self):
        self.MUC51 = MCUFunc.MyWindow()
        self.MUC51.show()

    def set_background_image(self):# 设置背景颜色
        self.setStyleSheet("QPushButton{background-color: rgb(235, 235, 255);border:2px groove "
                           "gray;border-radius:10px;padding:4px 20px;border-style: outset;} "
                           "QPushButton:hover{background-color:rgb(229, 241, 251); color: black;}"
                           "QPushButton:pressed{background-color:rgb(204, 228, 247);border-style: inset;}"
                           "#MainWindow {\n"
                           "    border-image: url(Pictures/background.jpg);\n"
                           "}")


QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 使得窗口比例和用Qt设计时完全一致

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
