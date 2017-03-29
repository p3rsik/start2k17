"""Main project file."""
# coding=utf-8


from sys import argv, exit
from PyQt5.QtWidgets import QWidget, QApplication, QFormLayout, QDesktopWidget
from PyQt5.QtCore import Qt
from gui.scene import Scene


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.__size = QDesktopWidget().size()
        self.__scene = Scene(0, 0, self.__size.width(), self.__size.height())

        self.initUI()

    def initUI(self):
        self.setLayout(QFormLayout())
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(argv)
    win = MainWindow()
    exit(app.exec_())