import pgzrun
WIDTH = 800
HEIGHT = 800

def draw():
    screen.clear()
    screen.fill('blue') 
    
    rectangle2 = Rect((300,400),(300,200))
    screen.draw.filled_rect(rectangle2,'brown')
    screen.draw.line((450,250),(600,400),color = 'brown')
    screen.draw.line((450,250),(600,400),color = 'brown')

pgzrun.go()