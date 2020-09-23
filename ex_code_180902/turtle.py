import turtle
turtle.pensize(2)
d = -45
for i in range(4):
    turtle.seth(d)
    d += 90
    turtle.fd(200)