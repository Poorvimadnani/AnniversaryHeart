import turtle

# a function to draw a heart
def draw_heart():
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

# a function to write "Happy Anniversary aaz, I love you beyond measure <3" in the center
def write_anniversary():
    turtle.penup()
    turtle.goto(0, -60)  # Adjusted the y-coordinate to center the text
    turtle.pendown()
    turtle.color("white")  # Set the text color to white
    turtle.write("Happy Anniversary aaz,\nI love you beyond measure <3", align="center", font=("Arial", 16, "bold"))

# Setting up the turtle
turtle.speed(2)
turtle.bgcolor("black")  # Set the background color to black
turtle.color("white")  # Set the arrow (turtle cursor) color to white

# Drawing the main heart
draw_heart()

# Function to write the text
write_anniversary()

# Hide the turtle
turtle.hideturtle()

# to help keep the program window open
turtle.done()
