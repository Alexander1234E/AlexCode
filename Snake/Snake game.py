import pygame as pg

board = 500


pg.init()
b = pg.display.set_mode((500, 500))
print("Board size is 500 by 500. Do not put numbers higher than 100.")
print("NOTE: You can use 125 but the squares will be tiny.")
print("Please don't use numbers that can not be divided by 500. 25 is recommended")
n = int(input('put in a number: '))
#num = int(n)``
for i in range(1, n):
    pg.draw.line(b, (255, 255, 255), (500//n*i, 0), (500//n*i, 500))
for i in range(1, n):
    pg.draw.line(b, (255, 255, 255), (0, 500//n*i), (500, 500//n*i))

#pg.draw.rect(screen, (0, 255, 0), (20, 20, 20, 20))



def draw_snake(x, y):
    gw = 500//n
    pg.draw.rect(b, (0, 255, 30), (gw*x, gw*y, gw, gw))


x = int(input("where do you want the snake to be? (X)"))
y = int(input("where do you want the snake to be? (Y)"))
draw_snake(x, y)
pg.display.flip()
input("(><)")

