#Создай собственный Шутер!

from pygame import *
from random import randint
window = display.set_mode((700,500))
display.set_caption('пинг-понг')
background = transform.scale(image.load('bg.png'),(700,500))
window.blit(background,(0,0))
clock = time.Clock()
fps = 60
game = True
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.x -= 10
            
        if keys_pressed[K_DOWN]and self.rect.y < 605:
            self.rect.x += 10
            
    
points = 0
lost = 0             
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(50,650)
            self.rect.y = 0
            global lost
            lost += 1
monsters = sprite.Group()
font.init()
#СДЕЛАЙ ШРИФТ СИСТЕМНЫМ - СМ. 7ОЙ СЛАЙД В ТЕОРИИ
font1 = font.SysFont('Arial', 50)
ladno = font.SysFont('Arial',50)
okay = font.SysFont('Arial',50)
score = font1.render(
    'Счёт:',True, (100,100,0)
)

lose = font1.render(
    'ты проиграл',True, (100,100,0)
)






igrok = Player('pp.png',350,450,80,100,10)
sprites_list = sprite.spritecollide(
    igrok, monsters, False
)

mixer.init()
mixer.music.load('space.ogg')
mixer.music.load('fire.ogg')
mixer.music.play()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
       


    if lost >=10:
        window.blit(lose,(100,200))
        finish = True
    if sprite.spritecollide(igrok,monsters, False):
        window.blit(lose,(100,200))
        finish = True

  


    if not finish:
        window.blit(background,(0,0))
        igrok.update()
        igrok.reset()
        
            
            
        kk = ladno.render( str(points),True,(100,100,0))
        gg = okay.render( str(lost),True,(100,100,0))
        monsters.draw(window)
        monsters.update()

 

        window.blit(gg,(230,50))
    
        window.blit(score,(20,20))
 

    clock.tick(fps)
    display.update()    
       
         