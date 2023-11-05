import turtle

# turtle object
pen = turtle.Turtle()

# set speed
pen.speed(20)

# set pen size
pen.pensize(6)

# head
pen.circle(50)

# neck
pen.right(90)
pen.forward(150)

# right leg
pen.left(45)
pen.forward(80)

# left leg
pen.penup()
pen.goto(0, -150)
pen.pendown()
pen.right(90)
pen.forward(80)

# right shoulder
pen.penup()
pen.goto(0, -10)
pen.pendown()
pen.left(90)
pen.forward(80)

# left shoulder
pen.penup()
pen.goto(0, -10)
pen.pendown()
pen.right(90)
pen.forward(80)

# hide turtle
pen.hideturtle()

# close the turtle graphics window on click
turtle.exitonclick()
