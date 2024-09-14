import random
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.generation)

    def generation(self):
        signs = ""
        if self.ui.checkBox.isChecked():
            signs += "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
        if self.ui.checkBox_2.isChecked():
            signs += "1234567890"
        if self.ui.checkBox_3.isChecked():
            signs += "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?"
        res = ""
        num = random.randint(8,12)
        for i in range(num):
            res += random.choice(signs)
        self.ui.label.setText(res)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()

