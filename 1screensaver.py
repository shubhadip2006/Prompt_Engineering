import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Screensaver")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.hideturtle()  # Hide the turtle cursor

# Function to draw a colorful spiral
def draw_spiral():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    t.penup()
    t.goto(0, 0)
    t.pendown()
    for i in range(360):
        t.pencolor(random.choice(colors))
        t.forward(i * 3 / len(colors) + i)
        t.left(59)  # Change the angle for different spiral effects
# Function to clear and restart the screensaver
def reset_screensaver():
    screen.clear()
    screen.bgcolor("black")
    draw_spiral()
# Main loop
while True:
    draw_spiral()
    # Move the turtle to a random position to create a new spiral
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    t.pendown()
    reset_screensaver()
    