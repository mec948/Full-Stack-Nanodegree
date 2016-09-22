import turtle

def draw_shape():
    
    window = turtle.Screen()
    window.bgcolor('black')
    
    brad = turtle.Turtle() #initializes a new instance of a turtle object from the class Turtle called brad
    brad.shape('turtle')
    brad.color('pink')
    brad.speed(2)

    for x in range(0,4):
        x = x + 1
        brad.forward(100)
        brad.right(90) #degree of the turn
    
    angie = turtle.Turtle()
    angie.shape('circle')
    angie.color('purple')
    angie.circle(100)
    angie.speed(2)

    pat = turtle.Turtle()
    pat.shape('arrow')
    pat.color('blue')
    pat.speed(2)

    for x in range(0,3):
        x = x + 1
        pat.forward(320)
        pat.left(120)

    window.exitonclick()
    
draw_shape()
