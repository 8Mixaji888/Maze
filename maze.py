#создай игру "Лабиринт"!
from re import S
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, ppicture, xcor, ycor, speed=0):
        super().__init__()
        self.ppicture = transform.scale(image.load(ppicture), (65, 65))
        self.rect = self.ppicture.get_rect()
        self.rect.x = xcor
        self.rect.y = ycor
        self.speed = speed

    def reset(self):
        mw.blit(self.ppicture, (self.rect.x, self.rect.y))

mixer.init()
display.init()
font.init()

mwWidth = 700
mwHeight = 500
finish = False

mw = display.set_mode((700,500))
display.set_caption('Maze')

background = transform.scale(image.load('background.jpg'),(mwWidth,mwHeight))

class Player(GameSprite):
    def go(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < mwWidth-65:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < mwHeight-65:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, ppicture, xcor, ycor, speed=0):
        super().__init__(ppicture, xcor, ycor, speed)
        self.direction = 'left'

    def go(self):       
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 635:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, width, height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

game_over = False
clock = time.Clock()
mixer.music.load('jungles.ogg')
win_sound = mixer.Sound('kick.ogg')
end_sound = mixer.Sound('money.ogg')
mixer.music.play()

player = Player('hero.png', 10, 400, 5)
cyborg = Enemy('cyborg.png', 625, 280, 5)
gold = GameSprite('treasure.png', 625, 425)
w1 = Wall(154, 205, 50, 100, 20 , 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20 , 10, 380)
w4 = Wall(154, 205, 50, 200, 130, 10, 350)
w5 = Wall(154, 205, 50, 450, 130, 10, 360)
w6 = Wall(154, 205, 50, 300, 20, 10, 350)
w7 = Wall(154, 205, 50, 390, 120, 130, 10)

while not game_over:
    for e in event.get():
        if e.type == QUIT:
            game_over = True
    if finish != True:
        player.go()
        cyborg.go()

        mw.blit(background, (0,0))
        player.reset()
        cyborg.reset()
        gold.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()

        if sprite.collide_rect(player, gold):
            end_sound.play()
            win_win = font.Font(None, 100).render('YOU WIN', False, (255,255,0))
            finish = True
            mw.blit(win_win, (200, 240))
        
        if (sprite.collide_rect(player, cyborg) or
            sprite.collide_rect(player, w1) or
            sprite.collide_rect(player, w2) or
            sprite.collide_rect(player, w3) or
            sprite.collide_rect(player, w4) or
            sprite.collide_rect(player, w5) or
            sprite.collide_rect(player, w6) or
            sprite.collide_rect(player, w7)):
            win_sound.play()
            win_lose = font.Font(None, 100).render('YOU LOSE', False, (255,255,0))
            finish = True
            mw.blit(win_lose, (200, 240))

    display.update()
    clock.tick(60)