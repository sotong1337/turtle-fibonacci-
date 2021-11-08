from turtle import *
import turtle

def square(turtle, size):
    for i in range(0,4):
        turtle.forward(size)
        turtle.left(90)

def repeat(turtle, function, times, angle_start, angle_rotate, size, rescale):
    
    turtle.left(angle_start)
    for i in range(0, times):
        function(turtle, size)
        turtle.left(angle_rotate)
        size = rescale * size


fred = Turtle()
fred.shape("turtle")
fred.speed("fastest")

fred2 = Turtle()
fred2.shape("turtle")
fred2.pencolor("red")
fred2.speed("fastest")

fred3 = Turtle()
fred3.shape("turtle")
fred3.pencolor("silver")
fred3.speed("fastest")

fred4 = Turtle()
fred4.shape("turtle")
fred4.pencolor("blue")
fred4.speed("fastest")

repeat(fred, square, 69, 0, 10, 200, 0.97)
repeat(fred2, square, 69, 90, 10, 240, 0.97)
repeat(fred2, square, 69, 180, 10, 220, 0.96)
repeat(fred4, square, 69, 270, 10, 230, 0.96)

ts = turtle.getscreen()
ts.getcanvas().postscript(file = "test.eps")