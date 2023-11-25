import turtle
colors = ['pink', 'light blue', 'pink', 'light blue', 'pink', 'light blue']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 2)
    t.forward(x)
    t.left(59)

