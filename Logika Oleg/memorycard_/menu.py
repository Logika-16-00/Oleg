from PyQt5.QtWidgets import QLineEdit, QPushButton, QListWidget, QWidget, QVBoxLayout,     QFormLayout

line_ans = QLineEdit("")
line_correct = QLineEdit("")
line_false1 = QLineEdit("")
line_false2 = QLineEdit("")
line_false3 = QLineEdit("")

form = QFormLayout()
form.addRow("Введіть запитаня" ,line_ans)
form.addRow("Введіть правильну відповіть" ,line_correct)
form.addRow("Введіть неправильний варіант" ,line_false1)
form.addRow("Введіть неправильний варіант" ,line_false2)
form.addRow("Введіть неправильний варіант" ,line_false3)

list_q = QListWidget()

btn_add = QPushButton("Додати запитання")
but_clorer = QPushButton("Очистити")
btn_back = QPushButton("Назад")

wdgt_edit = QWidget()
wdgt_edit.setLayout(form)

line1 = QVBoxLayout()
line1.addWidget(list_q)
line1.addWidget(btn_add)

line2 = QVBoxLayout()
line2.addWidget(wdgt_edit)
line2.addWidget(but_clorer)

line3 = QVBoxLayout()
line3.addLayout(line1)
line3.addLayout(line2)

line4 = QVBoxLayout()
line4.addWidget(btn_back, stretch=2)

mein_menu_line = QVBoxLayout()
mein_menu_line.addLayout(line3)
mein_menu_line.addLayout(line4)
