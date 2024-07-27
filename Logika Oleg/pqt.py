from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint
def click():
    num_win = randint(0,100)
    txt1.setText("Переможець")
    txt2.setText(str(num_win))

app = QApplication([])
win1 = QWidget()
win1.resize(300,200)
win1.move(500,200)
win1.setWindowTitle("wind")
txt1 = QLabel("Нажми!!!")
txt2 = QLabel("?")
bnt = QPushButton("Нажми")
bnt.clicked.connect(click)
line = QVBoxLayout()
line.addWidget(txt1, alignment=Qt.AlignCenter) 
line.addWidget(txt2, alignment=Qt.AlignCenter)
line.addWidget(bnt)
win1.setLayout(line)
win1.show()
win1.show()
app.exec_()