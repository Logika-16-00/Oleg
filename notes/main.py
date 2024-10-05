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
        self.ui.list_1.itemClicked.connect(self.show_notes)
        for note in notes.keys():
            self.ui.list_1.addItem(note)
        self.ui.bnt_save.clicked.connect(self.save_note)
        self.ui.btn_add.clicked.connect(self.add_tag)
        self.ui.bnt_delete.clicked.connect(self.delete_notes)



    def show_notes(self,item):
        self.ui.list_2.clear()
        note_name= item.text()
        if note_name in notes:
            self.ui.list_2.addItems(notes[note_name]["теги"])
            self.ui.textEdit.setText(notes[note_name]["текст"])

    def save_note(self):
        if self.ui.list_1.currentItem():
            key = self.ui.list_1.currentItem().text()
            notes[key]["текст"] = self.ui.textEdit.toPlainText()
        self.write_to_file()

    def add_tag(self):
        if self.ui.list_1.currentItem():
            tag_name,ok =QInputDialog.getText(self,"Додати тег","Введіть тег")
            note_name = self.ui.list_1.currentItem().text()
            if tag_name and ok:
                if tag_name not in notes[note_name]["теги"]:
                    self.ui.list_2.addItem(tag_name)
                    notes[note_name]["теги"].append(tag_name)
                self.write_to_file()

    def delete_note(self):
        if self.ui.list_1.currentItem():
            note_name = self.ui.list_1.currentItem().text()
            del notes[note_name]
            self.ui.list_1.takeItem(self.ui.list_1.currentRow())
        self.write_to_file()

    def delete_tag(self):
        if self.ui.list_1.currentItem() and self.ui.list_2.currentItem():
            note_name = self.ui.list_1.currentItem().text()
            tag_name = self.ui.list_2.currentItem().text()
            self.ui.list_2.takeItem(self.ui.list_2.currentRow())
            notes[note_name]["теги"].remove(tag_name)
        self.write_to_file()


    def add_note(self):
        note_name,ok = QInputDialog.getText(self ,"Додати замітку", "Назва замітку")
        if ok and note_name != "":
            notes[note_name] = {"теги":[], "текст": ""}
            self.ui.list_1.addItem(note_name)
        self.write_to_file()


    def write_to_file(self):
        with open("notes/notes.json","w",encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)

        
with open("notes/notes.json","r",encoding="utf-8") as file:
    notes = json.load(file)

print(notes)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()