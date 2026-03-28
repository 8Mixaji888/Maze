#создай игру "Лабиринт"!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, ppicture, xcor, ycor, speed):
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

mw = display.set_mode((700,500))
display.set_caption('Maze')

background = transform.scale(image.load('background.jpg'),(700,500))

game_over = False
clock = time.Clock()
mixer.music.load('jungles.ogg')
mixer.music.play()

player = GameSprite('hero.png', 10, 422, 5)
cyborg = GameSprite('cyborg.png', 625, 280, 5)

while not game_over:
    for e in event.get():
        if e.type == QUIT:
            game_over = True

    mw.blit(background, (0,0))
    player.reset()
    cyborg.reset()

    display.update()
    clock.tick(60)