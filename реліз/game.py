#Створи власний Шутер!

from pygame import *
from random import *
from time import time as timer
wn =  display.set_mode((1100,700))
display.set_caption("Shooter")

fon = transform.scale(image.load("sf.png"),(1100,700))
menu_fon = transform.scale(image.load("sf.png"),(1100,700))
level_1_fon = transform.scale(image.load("cort.png"),(1100,700))

finish = False

menu = 0
level_1=1

fps = 60
clock = time.Clock()

font.init()
font1 = font.Font(None,30)
font2 = font.Font(None,80)





class Player(sprite.Sprite):
    def __init__(self, image_player,x,y,size_x,size_y,life,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.life = life
        self.is_jumping = False
        self.jump_speed = 20
        self.gravity = 1
    
    def show(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
    def process_jump(self):
        if self.is_jumping: 
            self.rect.y -= self.jump_speed
            self.jump_speed -= self.gravity
            if self.jump_speed <= -10:
                self.is_jumping = False
                self.jump_speed = 20

    def move_1(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
                self.rect.x += self.speed
        if keys[K_w]:
                self.jump()
    def move_2(self):
            keys = key.get_pressed()
            if keys[K_j]:
                self.rect.x -= self.speed
            if keys[K_l]:
                self.rect.x += self.speed
            if keys[K_i]:
                self.jump()
                
game = 1

sf = Player("sf.png", 210,450,120,130,0,2)
pf = Player("pf.png", 770,450,120,130,0,2)

while game:
    wn.blit(fon,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = 0
    
                        
    if not finish:
        if menu:
            wn.blit(menu_fon,(0,0))
            
        if level_1:
            wn.blit(level_1_fon,(0,0))
            sf.show()
            sf.move_1()
            pf.show()
            pf.move_2()

            if pf.rect.y < 500:
                pf.rect.y += 2            
                 
            if sf.rect.y < 500:
                sf.rect.y += 2
    sf.process_jump()
    pf.process_jump()




    display.update()
    clock.tick(fps)

