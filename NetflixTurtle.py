import turtle

t = turtle
t.bgcolor('black')
t.right(90)
pos = [(-40, 0), (40, 0)]
for x,y in pos:
    t.up()
    t.goto(x,y)
    t.down()
    t.fillcolor('red')
    for i in range(2):
        t.begin_fill()
        t.forward(200)
        t.left(90)
        t.forward(40)
        t.left(90)
        t.end_fill()
t.up()
t.goto(-40,0)
t.down()
t.left(22)
t.begin_fill()
for i in range(2):
    t.forward(217)
    t.left(68)
    t.forward(40)
    t.left(112)
t.end_fill()
t.ht()
t.done()