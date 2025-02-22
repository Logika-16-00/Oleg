class Widget():
    def __init__(self,text,x, y):
        self.x = x
        self.y = y
        self.text = text

    def print_text(self):
        print("Інформація про віджет")
        print(self.text,self.x,self.y)
class Button(Widget):
    def __init__(self, text, x, y, is_click):
        super().__init__(text, x, y)
        self.is_click = is_click

    def click(self):
        print("молодець")
        self.is_click = True
adolf = Button("I Adolf" , 56,14, False)
adolf.print_info()
a= input("???")
if a == "так":
    adolf.click()

    