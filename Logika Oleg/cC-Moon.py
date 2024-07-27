class Title():
    def __init__(self,title,x,y,view):
        self.title = title
        self.x = x
        self.y = y
        self.view = view
    def info(self):
        print("інформація",self.title,self.x,self.y)
    def show(self):
        self.view = True
    def hide(self):
        self.view = False
        