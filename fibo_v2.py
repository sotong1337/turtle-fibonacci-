from turtle import *
import turtle

def square(turtle, size):
    for i in range(0,4):
        turtle.forward(size)
        turtle.left(90)


def fibo(turtle_lst, colour_start, colour_final, times):

    for turtles in turtle_lst:
        turtle_ = turtles[0]
        angle_start = turtles[2]
        turtle_.left(angle_start)
    
    r1, g1, b1 = colour_start
    r2, g2, b2 = colour_final

    r_difference = r2 - r1
    g_difference = g2 - g1
    b_difference = b2 - b1

    r_change = r_difference / times
    g_change = g_difference / times
    b_change = b_difference / times

    screen = Screen()
    screen.colormode(255)

    for i in range(0, times):
        r1 += r_change
        g1 += g_change
        b1 += b_change

        for turtles in turtle_lst:
            turtle_, function, angle_start, angle_rotate, size, rescale = turtles

            turtle_.pencolor(int(r1), int(g1), int(b1))

            if i != 0:
                size = size * (rescale ** i)

            function(turtle_, size)
            turtle_.left(angle_rotate)

fred = Turtle()
fred.shape("turtle")
fred.speed("fastest")

fred2 = Turtle()
fred2.shape("turtle")
fred2.speed("fastest")

fred3 = Turtle()
fred3.shape("turtle")
fred3.speed("fastest")

fred4 = Turtle()
fred4.shape("turtle")
fred4.speed("fastest")


t1 = (fred, square, 0, 10, 200, 0.97)
t2 = (fred2, square, 90, 10, 240, 0.97)
t3 = (fred3, square, 180, 10, 220, 0.96)
t4 = (fred4, square, 270, 10, 230, 0.96)
fibo([t1, t2, t3, t4], (94,35,203), (145,205,254), 69)

ts = turtle.getscreen()
ts.getcanvas().postscript(file = "test3.eps")