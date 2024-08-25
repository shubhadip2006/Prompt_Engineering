import turtle

def draw_square(turtle_obj):
    for _ in range(4):
        turtle_obj.forward(100)  # Move forward by 100 units
        turtle_obj.right(90)     # Turn right by 90 degrees

def draw_circle(turtle_obj):
    turtle_obj.circle(100)     # Draw a circle with radius 100

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    turtle_obj = turtle.Turtle()
    turtle_obj.speed(1)        # Set turtle speed (1 is slowest, 10 is fastest)

    # Draw a square
    turtle_obj.penup()
    turtle_obj.goto(-150, 0)   # Move turtle to starting position for square
    turtle_obj.pendown()
    draw_square(turtle_obj)

    # Draw a circle
    turtle_obj.penup()
    turtle_obj.goto(150, 0)    # Move turtle to starting position for circle
    turtle_obj.pendown()
    draw_circle(turtle_obj)

    screen.mainloop()          # Keep the window open

if __name__ == "__main__":
    main()
