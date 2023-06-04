import turtle
from turtle import*

# Screen for output
scren = turtle.Screen()

# Defining a turtle Instance
t = turtle.Turtle()

# Initially penup()
t.penup()
t.goto(-400, 200)
t.pendown()

# Red Rectangle
t.color("red")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()
t.left(90)
t.color("black")
t.forward(167)

# White rectangle
t.left(90)
t.forward(800)
t.left(90)
t.forward(167)
t.left(90)
t.forward(800)

# menulis huruf
t.setpos(-400, -250)
t.write("HAPPY INDEPENDENCE DAY \n code by: habibi :) ", font=("Verdana", 20, "normal"))
# to hold the output window
turtle.done()
