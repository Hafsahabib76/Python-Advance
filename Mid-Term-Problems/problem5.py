# Import Turtle Library
import turtle


# function to draw a flower at the center of the screen
# It should take parameters:
# number of petals, the length of each petal, and the color of the flower.
def draw_flower(num_petals, length, color):
    # Create a Turtle Screen
    window = turtle.Screen()
    # Set the screen background color to white
    window.bgcolor("white")

    # Create a flower turtle
    flower = turtle.Turtle()
    # Set the speed of flower turtle
    flower.speed(10)
    # Set the color of the flower turtle
    flower.color(color)

    # For loop to draw the petals defined by the user
    for _ in range(num_petals):
        flower.forward(length)
        flower.left(45)
        flower.forward(length)
        flower.left(135)
        flower.forward(length)
        flower.left(45)
        flower.forward(length)
        flower.left(135 - 360 / num_petals)

    # Hide the Turtle
    flower.hideturtle()
    # Display the window
    window.mainloop()


# Call draw_flower function and specify the values in parameter
draw_flower(6, 80, "red")
