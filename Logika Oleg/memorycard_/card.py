from app import *

win_card = QWidget()
win_card.resize(600,500)
win_card.setWindowTitle("Memory Card")
win_card.move(0,0)

btn_sleep = QPushButton("Відпочити")
box_min = QSpinBox()
box_min.setValues(5)

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

line1 = QVBoxLayout()
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
mainline_btn_ans.addWidget(line_btn_ans1)
mainline_btn_ans.addWidget(line_btn_ans2)
AnswersGroupBox.setLayout(mainline_btn_ans)

mani_line =QVBoxLayout()
mani_line.addWidget(line1)
mani_line.addWidget(lb_ans)
mani_line.addWidget(btn_ans)

win_card.setLayout(mani_line)

win_card.show()
App.exec_()