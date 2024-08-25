import turtle

screen = turtle.Screen()
screen.bgcolor("red")

pen = turtle.Turtle()
pen.color("white")
pen.width(3)
pen.speed(4)

pen.begin_fill()
pen.left(50)
pen.forward(133)
pen.circle(50, 200)
pen.right(140)
pen.circle(50, 200)
pen.forward(133)
pen.end_fill()     

pen.hideturtle()
turtle.done() 
