import os
import pygame as pg
from random import choice, randrange


class Symbol:
    def __init__(self, x, y, speed):
        self.x, self.y = x, y
        self.speed = speed
        self.value = choice(green_symbols)
        self.interval = randrange(5, 30)

    def draw(self, color):
        frames = pg.time.get_ticks()
        if not frames % self.interval:
            self.value = choice(green_symbols) if color == 'green' else lightgreen_zero
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE
        surface.blit(self.value, (self.x, self.y))


class SymbolColumn:
    def __init__(self, x, y):
        self.column_height = randrange(MIN_LENGTH, MAX_LENGTH)
        self.speed = randrange(MIN_SPEED, MAX_SPEED)
        self.symbols = [Symbol(x, i, self.speed) for i in range(y, y - FONT_SIZE * self.column_height, -FONT_SIZE)]

    def draw(self):
        [symbol.draw('green') if i else symbol.draw('lightgreen') for i, symbol in enumerate(self.symbols)]


os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 1200, 700
FONT_SIZE = 25
FPS = 60
SPEED_RANGE = MIN_SPEED, MAX_SPEED = 2, 10
LENGTH_RANGE = MIN_LENGTH, MAX_LENGTH = 8, 24

pg.init()
pg.display.set_caption('Matrix screensaver')
screen = pg.display.set_mode(RES)
surface = pg.Surface(RES)
clock = pg.time.Clock()

symbols = '0123456789'
font = pg.font.SysFont('ms mincho', FONT_SIZE, bold=True)
green_symbols = [font.render(char, True, (40, randrange(160, 256), 40)) for char in symbols]
lightgreen_zero = font.render('0', True, pg.Color('lightgreen'))

symbol_columns = [SymbolColumn(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE)]

while True:
    screen.blit(surface, (0, 0))
    surface.fill(pg.Color('black'))

    [symbol_column.draw() for symbol_column in symbol_columns]

    [exit() for i in pg.event.get() if i.type == pg.QUIT]
    pg.display.flip()
    clock.tick(FPS)
