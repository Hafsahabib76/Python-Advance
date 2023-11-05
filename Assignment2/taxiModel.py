import turtle

# turtle object
pen = turtle.Turtle()

# pen settings
pen.pencolor("#000000")
pen.speed(50)
pen.pensize(2)

# Yellow taxi box
pen.fillcolor("#FDE166")

pen.begin_fill()
pen.forward(175)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(350)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(175)
pen.end_fill()

# move pen to draw back taxi wheel
pen.penup()
pen.goto(100, -30)
pen.pendown()

# Back taxi red wheel
pen.fillcolor("#8E7C6E")
pen.begin_fill()
pen.circle(30)
pen.end_fill()

# move pen to draw front taxi wheel
pen.penup()
pen.goto(-100, -30)
pen.pendown()

# Front taxi red wheel
pen.begin_fill()
pen.circle(30)
pen.end_fill()

# move pen to draw taxi top
pen.penup()
pen.goto(-100, 100)
pen.pendown()
pen.fillcolor("#BEDDF1")

# draw taxi top
pen.begin_fill()
pen.left(65)
pen.forward(80)
pen.right(65)
pen.forward(130)
pen.right(65)
pen.forward(80)
pen.left(65)
pen.left(180)
pen.forward(100)
pen.right(90)
pen.forward(72)
pen.left(180)
pen.forward(72)
pen.right(90)
pen.forward(105)
pen.end_fill()

# move pen to draw taxi headlight
pen.penup()
pen.goto(-175, 45)
pen.pendown()
pen.fillcolor("#FFFABF")

# draw taxi headlight
pen.begin_fill()
pen.forward(10)
pen.right(90)
pen.forward(25)
pen.right(90)
pen.forward(10)
pen.end_fill()

# move pen to draw taxi backlight
pen.penup()
pen.goto(175, 45)
pen.pendown()
pen.fillcolor("#D50606")

# draw taxi backlight
pen.begin_fill()
pen.forward(10)
pen.left(90)
pen.forward(25)
pen.left(90)
pen.forward(10)
pen.end_fill()

# draw line
pen.penup()
pen.goto(175, 32)
pen.pendown()
pen.fillcolor("#FE353F")

pen.begin_fill()
pen.forward(350)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(350)
pen.right(90)
pen.forward(20)
pen.end_fill()

# draw center line
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.left(180)
pen.forward(100)

# draw first gate holders
pen.penup()
pen.goto(-10, 70)
pen.pendown()
pen.left(90)
pen.pensize(3)
pen.forward(15)

# draw second gate holders
pen.penup()
pen.goto(70, 70)
pen.pendown()
pen.right(180)
pen.pensize(3)
pen.forward(15)

# draw taxi top board
pen.penup()
pen.pensize(2)
pen.goto(30, 174)
pen.pendown()
pen.fillcolor("#000000")
pen.begin_fill()
pen.left(90)
pen.forward(15)
pen.left(90)
pen.forward(70)
pen.left(90)
pen.forward(15)
pen.end_fill()

# hide turtle
pen.hideturtle()

# close window by click
turtle.exitonclick()
