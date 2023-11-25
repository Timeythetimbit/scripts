import turtle

screen = turtle.getscreen()
screen.bgcolor("orange")

speedyTurtle = turtle.Turtle()

speedyTurtle.pencolor("magenta")
speedyTurtle.forward(55) 
speedyTurtle.fillcolor("pink")
speedyTurtle.begin_fill()
def PentagonDrawing(side):
    for i in range(0,5):
        speedyTurtle.forward(side)
        speedyTurtle.left(72)

PentagonDrawing(50)
speedyTurtle.end_fill()
turtle.done()