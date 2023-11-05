import turtle

pen = turtle.Turtle()

# Yellow bus box
pen.pencolor("black")
pen.speed(10)
pen.fillcolor("yellow")

pen.begin_fill()
pen.forward(175)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(350)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(175)
pen.end_fill()

# move pen to draw back bus wheel
pen.penup()
pen.goto(100, -30)
pen.pendown()

# Back bus red wheel
pen.fillcolor("red")
pen.begin_fill()
pen.circle(30)
pen.end_fill()

# move pen to draw front bus wheel
pen.penup()
pen.goto(-100, -30)
pen.pendown()

# Front bus red wheel
pen.fillcolor("red")
pen.begin_fill()
pen.circle(30)
pen.end_fill()

# hide turtle
pen.hideturtle()

# end turtle
turtle.done()
