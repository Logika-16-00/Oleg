from app import App
from PyQt5.QtWidgets import QRadioButton,QLabel,QSpinBox,QPushButton,QGroupBox,QHBoxLayout,QVBoxLayout,QButtonGroup
from PyQt5.QtCore import Qt



btn_sleep = QPushButton("Відпочити")
box_min = QSpinBox()
box_min.setValue(5)

lb_ans = QLabel("Запитаня")
ld_min = QLabel("Мню")


btn_menu = QPushButton("Меню")
btn_ans = QPushButton("Відповісти")

btn_ans1 = QRadioButton("1")
btn_ans2 = QRadioButton("2")
btn_ans3 = QRadioButton("3")
btn_ans4 = QRadioButton("4")

AnswersGroupBox = QGroupBox("Віріант відповіді")
RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_ans1)
RadioGroup.addButton(btn_ans2)
RadioGroup.addButton(btn_ans3)
RadioGroup.addButton(btn_ans4)

line1 = QHBoxLayout()
line2 = QVBoxLayout()
line1.addWidget(btn_menu)
line1.addWidget(btn_sleep)
line1.addWidget(box_min)
line1.addWidget(lb_ans)

line_btn_ans1 = QVBoxLayout()
line_btn_ans2 = QVBoxLayout()
line_btn_ans1.addWidget(btn_ans1)
line_btn_ans1.addWidget(btn_ans2)
line_btn_ans2.addWidget(btn_ans3)
line_btn_ans2.addWidget(btn_ans4)
mainline_btn_ans = QHBoxLayout()
mainline_btn_ans.addLayout(line_btn_ans1)
mainline_btn_ans.addLayout(line_btn_ans2)
AnswersGroupBox.setLayout(mainline_btn_ans)
mani_line =QVBoxLayout()
mani_line.addLayout(line1)
mani_line.addWidget(lb_ans)

ResGroupBox = QGroupBox("Результат")
lb_res = QLabel("Правильність")
lb_correct = QLabel("Правильна відповідь")
line_res = QVBoxLayout()
line_res.addWidget(lb_res)
line_res.addWidget(lb_correct)
ResGroupBox.setLayout(line_res)
mani_line.addWidget(AnswersGroupBox,stretch=8)

mani_line.addWidget(ResGroupBox,stretch=8)
ResGroupBox.hide()
mani_line.addWidget(btn_ans)

def show_res():
    if btn_ans.text() == "Відоповісти":
        AnswersGroupBox.hide()
        ResGroupBox.show()
        btn_ans.setText("Наступине питаня")
def show_ans():
    AnswersGroupBox.show()
    ResGroupBox.hide()
    btn_ans.setText("Відповісти")
    btn_ans1.setChecked(False)
    btn_ans2.setChecked(False)
    btn_ans3.setChecked(False)
    btn_ans4.setChecked(False)
btn_ans.clicked.connect(show_res)
