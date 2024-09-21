from PyQt5.QtWidgets import QApplication,QInputDialog
from PyQt5.QtWidgets import QMainWindow
from notes import Ui_MainWindow
import json


import json
class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_make.clicked.connect(self.add_note)
        self.show_note()


    def save_notes(self):
        self.ui.list_1.clear()
        self.ui.list_2.clear()
        print( notes.keys())
        for note in notes.keys():
            self.ui.list_1.addItem(note)
            self.ui.list_2.addItem(notes[note]["теги"])

    def add_note(self):
        note_name,ok = QInputDialog.getText(self ,"Додати замітку", "Назва замітку")
        if ok and note_name != "":
            notes[note_name] = {"теги":[], "текст": ""}
            self.ui.list_1.addItem(note_name)

    
        
with open("notes/notes.json","r",encoding="utf-8") as file:
    notes = json.load(file)

print(notes)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()