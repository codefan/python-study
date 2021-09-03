import pgzrun

r = 1
def draw():
    screen.fill('white')
    screen.draw.filled_circle((400,300), r, 'red')

def update():
    global r
    if r < 9998:
        r = r + 1/10

pgzrun.go()