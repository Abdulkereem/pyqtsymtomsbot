from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets 
from ui import res
import sys

class splash_ui(QMainWindow):
    def __init__(self):
        super(splash_ui,self).__init__()
        loadUi('./ui/work.ui',self)
        self.pushButton.clicked.connect(self.show_screen_two)


    def show_screen_two(self):
        self.two=screen_two()
        self.two.show()
        self.hide()




class screen_two(QMainWindow):
    def __init__(self):
        super(screen_two,self).__init__()
        loadUi('./ui/work2.ui',self)
        self.pushButton.clicked.connect(self.show_screen_three)
    
    def show_screen_three(self):
        self.three = screen_three()
        self.three.show()
        self.hide()


class screen_three(QMainWindow):
    def __init__(self):
        super(screen_three,self).__init__()
        loadUi('./ui/work3.ui',self)
        self.pushButton.clicked.connect(self.show_bot)

            
    def show_bot(self):
        self.bot = screen_four()
        self.bot.show()
        self.hide()



class screen_four(QMainWindow):
    def __init__(self):
        super(screen_four,self).__init__()
        loadUi('./ui/untitled.ui',self)









if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=splash_ui()
    window.show()
    sys.exit(app.exec_())