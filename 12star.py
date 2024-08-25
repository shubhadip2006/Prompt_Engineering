import turtle

star_turtle = turtle.Turtle()
star_turtle.speed(2)  

for _ in range(5):
    star_turtle.forward(100)  
    star_turtle.right(144)    

star_turtle.hideturtle()
turtle.done()