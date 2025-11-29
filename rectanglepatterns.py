import pgzrun
import random
WIDTH = 800
HEIGHT = 800


def draw():
    w = 800
    h = 600
    r = random.randint(1,255)
    g = random.randint(1,255) 
    b = random.randint(1,255)

    for i in range(20):
        r = random.randint(1,255)
        g = random.randint(1,255) 
        b = random.randint(1,255)
        rectangle1 = Rect((10,10),(w,h))
        rectangle1.center = 400,400
        screen.draw.rect(rectangle1,(r,g,b))
        w -= 20
        h += 20
    
pgzrun.go()