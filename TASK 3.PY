import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Indian Flag")
screen.bgcolor("white")

# Create a turtle object
flag_turtle = turtle.Turtle()
flag_turtle.speed(0)  # Set the drawing speed (0 is fastest)

# Draw the saffron rectangle
flag_turtle.color("#FF9933")  # Saffron color
flag_turtle.begin_fill()
flag_turtle.goto(-300, 200)
for _ in range(2):
    flag_turtle.forward(600)
    flag_turtle.right(90)
    flag_turtle.forward(100)
    flag_turtle.right(90)
flag_turtle.end_fill()

# Draw the white rectangle
flag_turtle.color("white")
flag_turtle.goto(-300, 100)
flag_turtle.begin_fill()
for _ in range(2):
    flag_turtle.forward(600)
    flag_turtle.right(90)
    flag_turtle.forward(100)
    flag_turtle.right(90)
flag_turtle.end_fill()

# Draw the green rectangle
flag_turtle.color("#138808")  # Green color
flag_turtle.goto(-300, 0)
flag_turtle.begin_fill()
for _ in range(2):
    flag_turtle.forward(600)
    flag_turtle.right(90)
    flag_turtle.forward(100)
    flag_turtle.right(90)
flag_turtle.end_fill()

# Draw the Ashoka Chakra (Navy Blue Circle)
flag_turtle.penup()
flag_turtle.goto(0, 50)
flag_turtle.pendown()
flag_turtle.color("#000080")  # Navy blue color
flag_turtle.circle(50)

# Hide the turtle cursor
flag_turtle.hideturtle()

# Keep the window open until manually closed
turtle.done()