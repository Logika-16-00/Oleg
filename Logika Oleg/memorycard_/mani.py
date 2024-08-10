from PyQt5.QtWidgets import QWidget
from card import *
from app import App

win_card = QWidget()
win_menu = QWidget()
def set_card():
    win_card.resize(600,500)
    win_card.setWindowTitle("Memory Card")
    win_card.move(0,0)
    win_card.setLayout(mani_line)

def set_card():
    win_menu.resize(600,500)
    win_menu.setWindowTitle("Memory menu")
    win_menu.move(0,0)

def back_to_menu():
    win_card.hide()
    win_menu.show()

bnt_menu.clicked.connect(back_to_menu)

set_card()
set_menu()
win_card.show()
App.exec_()