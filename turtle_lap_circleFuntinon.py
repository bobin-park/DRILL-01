import turtle
def draw_circle(x,y,z):
    turtle.penup()
    turtle.goto(x,y)
    turtle.stamp()
    turtle.goto(x,y-z)
    turtle.pendown()
    turtle.circle(z)

turtle.shape("turtle")
draw_circle(0,0,50)

turtle.exitonclick()