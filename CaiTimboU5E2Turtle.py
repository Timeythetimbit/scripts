import turtle

speedyTurtle = turtle.Turtle()

def PentagonDrawing(side):
    for i in range(0,5):
        speedyTurtle.forward(side)
        speedyTurtle.left(72)

PentagonDrawing(50)
PentagonDrawing(100)
PentagonDrawing(150)

turtle.done()