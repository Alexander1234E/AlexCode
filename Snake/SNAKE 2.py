import pygame as pg
from pygame import QUIT

pg.init()


def draw_snake(x, y):
    gw = c//n
    pg.draw.rect(screen, (255, 215, 0), (gw * x, gw * y, gw, gw))


c = int(input("What board do you want?: "))
screen = pg.display.set_mode((c, c))
print(f"Board size is {c}  by {c}. Do not put numbers not divisible by {c}.")
print("NOTE: If you do it too big the pixels will be tiny.")
n = int(input('How many grids do you want?: '))
o = input("What color do you want red, green, white, blueish, aqua, blueviolet, brown, or blue?: ")


x = n//2
y = n//2

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            break
        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_LEFT:
    screen.fill(0)
    if o == "green":
        for i in range(1, n):
            pg.draw.line(screen, (0, 255, 0), (c // n * i, 0), (c // n * i, c))
        for i in range(1, n):
            pg.draw.line(screen, (0, 255, 0), (0, c // n * i), (c, c // n * i))
    if o == "red":
        for i in range(1, n):
            pg.draw.line(screen, (255, 0, 0), (c // n * i, 0), (c // n * i, c))
        for i in range(1, n):
            pg.draw.line(screen, (255, 0, 0), (0, c // n * i), (c, c // n * i))
    if o == "white":
        for i in range(1, n):
            pg.draw.line(screen, (255, 255, 255), (c // n * i, 0), (c // n * i, c))
        for i in range(1, n):
            pg.draw.line(screen, (255, 255, 255), (0, c // n * i), (c, c // n * i))
    if o == "blueish":
        for i in range(1, n):
            pg.draw.line(screen, (150, 255, 255), (c // n * i, 0), (c // n * i, c))
        for i in range(1, n):
            pg.draw.line(screen, (150, 255, 255), (0, c // n * i), (c, c // n * i))
    if o == "aqua":
        for i in range(1, n):
            pg.draw.line(screen, (0, 255, 255), (c // n * i, 0), (c // n * i, c))
        for i in range(1, n):
            pg.draw.line(screen, (0, 255, 255), (0, c // n * i), (c, c // n * i))
    if o == "blueviolet":
        for i in range(1, n):
            pg.draw.line(screen, (138, 43, 226), (c // n * i, 0), (c // n * i, c))
        for i in range(1, n):
            pg.draw.line(screen, (138, 43, 226), (0, c // n * i), (c, c // n * i))
    if o == "brown":
        for i in range(1, n):
            pg.draw.line(screen, (165, 42, 42), (c // n * i, 0), (c // n * i, c))
        for i in range(1, n):
            pg.draw.line(screen, (165, 42, 42), (0, c // n * i), (c, c // n * i))
    if o == "blue":
        for i in range(1, n):
            pg.draw.line(screen, (0, 0, 255), (c // n * i, 0), (c // n * i, c))
        for i in range(1, n):
            pg.draw.line(screen, (0, 0, 255), (0, c // n * i), (c, c // n * i))
    draw_snake(x, y)
    pg.display.flip()
    pg.time.wait(500)
    x = (x+1) % n
    y = (y-1) % n


