from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication,QInputDialog,QMessageBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PyQt5.QtWidgets import QFileDialog
import os

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.image = None
        self.ui.btn_right.clicked.connect(self.rotate_left)
        self.ui.btn_left.clicked.connect(self.rotate_right)
        self.ui.btn_flip.clicked.connect(self.flip_image)
        self.ui.btn_sharp.clicked.connect(self.sharpen_image)
        self.ui.QPushButton_6.clicked.connect(self.bw_image)
        self.ui.btn_dir.clicked.connect(self.show_files)


        self.ui.listWidget.itemClicked.connect(self.show_picture)
        self.image = None

    def update_image(self,image = None):
        self.ui.label.hide()
        if image:
            pixmap = QPixmap(image)
            self.image.save("copy.png")
            pixmap = QPixmap("copy.png")
            w, h = self.ui.label.width(), self.ui.label.height()
            pixmap = pixmap.scaled(w, h)
            self.ui.label.setPixmap(pixmap)
            self.ui.label.show()
        
    def rotate_left(self):
        self.image = self.image.rotate(90)
        self.image.save("copy.png")
        self.update_image("copy.png")
    
    def rotate_right(self):
        self.image = self.image.rotate(-90)
        self.image.save("copy.png")
        self.update_image("copy.png")

    def  flip_image(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.update_image()

    def bw_image(self):
        self.image = self.image.convert(L)
        self.update_image()
    
    def sharpen_image(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.update_image() 

    def choose_dir(self):
        global workdir
        workdir = QFileDialog.getExistingDirectory(self)

        print(workdir)
    def filter(self,files,ext):
        res = []
        for file in files:
            for e in ext:
                if file.endswith(e):
                    res.append(file)
        return res
    
    def show_files(self):
        ext = ["png", "jpg", "PNG", "JPG"]
        self.choose_dir()
        if workdir:
            all_files = os.listdir(workdir)
            print(all_files)
            filter_files = self.filter(all_files,ext)
            print(filter_files)
            self.ui.listWidget.clear()
            for file in filter_files:
                self.ui.listWidget.addItem(file)

    def  show_picture(self):
        if self.ui.listWidget.currentRow() >= 0:
            filename = self.ui.listWidget.currentItem().text()
            image_path = os.path.join(workdir, filename)
            self.image = Image.open(image_path)
            self.update_image(self.image)

    def save_image(self): 
        if self.image:
            save_path, _ = QFileDialog.getSaveFileNames(self, "Зберегти файл", 
                        self.workdir, "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
            if save_path:
                self.image.save(save_path)
                QMessageBox.information(self, "Успіх", "Зображення успішню збережено!")
            else:
                QMessageBox.warning(self, "Увага", "Файл для збереження не обрфно.")
        else:
            QMessageBox.warning(self, "Увага", "Немає зображення для збереження.")

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
