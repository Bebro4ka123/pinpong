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
            self.rect.y -= 10
            
        if keys_pressed[K_DOWN]and self.rect.y < 395:
            self.rect.y += 10
class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
            
        if keys_pressed[K_s]and self.rect.y < 395:
            self.rect.y += 10
            
speed_x = 3
speed_y = 3    
points = 0


ball = GameSprite('ball.png',150,100,40,40,10)
                 



#СДЕЛАЙ ШРИФТ СИСТЕМНЫМ - СМ. 7ОЙ СЛАЙД В ТЕОРИИ
font.init()
font1 = font.SysFont('Arial', 50)
ladno = font.SysFont('Arial',50)
okay = font.SysFont('Arial',50)
score = font1.render(
    'Счёт:',True, (100,100,0)
)

lose = font1.render(
    'ты проиграл',True, (100,100,0)
)






igrok = Player('pp.png',0,200,40,100,10)
igrok2 = Player2('pp.png',660,200,40,100,10)

mixer.init()
mixer.music.load('space.ogg')
mixer.music.load('fire.ogg')
mixer.music.play()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 470 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x > 665 or ball.rect.x < 0:
            speed_x *= -1 
        if ball.rect.igrok:
            speed_y *= -1        
       


 

          
  


    if not finish:
        window.blit(background,(0,0))
        igrok.update()
        igrok.reset()
        igrok2.update()
        igrok2.reset()
        ball.update()
        ball.reset()
        
            
            
        kk = ladno.render( str(score),True,(10,10,0))
        window.blit(score,(10,10))

    
        
 

    clock.tick(fps)
    display.update()    
       
         