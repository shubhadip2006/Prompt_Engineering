import turtle

screen = turtle.Screen()
screen.title("Turtle Test")


t = turtle.Turtle()
t.speed(1)  

for _ in range(3):
    t.forward(100) 
    t.left(120)   

  
turtle.done()


