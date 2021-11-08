from turtle import *
import turtle

def square(turtle, size):
    for i in range(0,4):
        turtle.forward(size)
        turtle.left(90)

def colour_diff(colour_start, colour_final, steps):
    r1, g1, b1 = colour_start
    r2, g2, b2 = colour_final

    r_difference = r2 - r1
    g_difference = g2 - g1
    b_difference = b2 - b1

    r_change = r_difference / steps
    g_change = g_difference / steps
    b_change = b_difference / steps

    return (r_change, g_change, b_change)

def fibo(turtle_lst, times, width_, height):

    for turtles in turtle_lst:
        turtle_ = turtles[0]
        angle_start = turtles[2]
        turtle_.left(angle_start)

    screen = Screen()
    screen.colormode(255)
    turtle.screensize(width_, height)
    turtle.title("I was forced to do this lol")

    for i in range(0, times):

        for turtles in turtle_lst:
            turtle_, function, angle_start, angle_rotate, size, rescale, colour_start, colour_final = turtles
            
            r1, g1, b1 = colour_start
            r_change, g_change, b_change = colour_diff(colour_start, colour_final, times)
            
            r1 += r_change * i
            g1 += g_change * i
            b1 += b_change * i

            turtle_.pencolor(int(r1), int(g1), int(b1))

            if i != 0:
                size = size * (rescale ** i)

            function(turtle_, size)
            turtle_.left(angle_rotate)

###editing starts here if you want

sk = Turtle()
sk.shape("turtle")
sk.speed("fastest")

sk2 = Turtle()
sk2.shape("turtle")
sk2.speed("fastest")

jp = Turtle()
jp.shape("turtle")
jp.speed("fastest")

ran = Turtle()
ran.shape("turtle")
ran.speed("fastest")

out = Turtle()
out.shape("turtle")
out.speed("fastest")

of = Turtle()
of.shape("turtle")
of.speed("fastest")

variable = Turtle()
variable.shape("turtle")
variable.speed("fastest")

names = Turtle()
names.shape("turtle")
names.speed("fastest")

#turtle_, function, angle_start, angle_rotate, size, rescale, colour_start, colour_final
#original_plalatte: start-(94,35,203) final-(145,205,254)
dark = (119,162,211) 
dark_3_4 = (120,173,209)
mid = (120,182,206)
bright_1_4 = (120,193,204)
bright = (121,202,202  )  
end = (225,136,176)

sk.penup()
sk.goto(0, 120)   #0, 30
sk.showturtle()          
sk.pendown()
t1 = (sk, square, 0, 10, 180, 0.98, mid, end) #mid top

sk2.penup()
sk2.goto(-40, -60)   #-10, 10
sk2.showturtle()          
sk2.pendown()
t2 = (sk2, square, 45, 10, 220, 0.96, bright, end) #(203,171,109) #bright up right


jp.penup()
jp.goto(-120, 0)   #-30, 0
jp.showturtle()          
jp.pendown()
t3 = (jp, square, 90, 10, 200, 0.97, dark_3_4, end) #(74,159,157) #3/4 mid right

ran.penup()
ran.goto(40, -80)   #0, -20
ran.showturtle()          
ran.pendown()
t4 = (ran, square, 135, 10, 220, 0.96, bright_1_4, end) #(252,227,123) #1/4 bot right

out.penup()
out.goto(0, -120)   #0, 30
out.showturtle()          
out.pendown()
t5 = (out, square, 180, 10, 180, 0.98, dark, end) #dark bot


of.penup()
of.goto(-40, 80)   #-10, 20
of.showturtle()          
of.pendown()
t6 = (of, square, 225, 10, 220, 0.96, bright_1_4, end) #1/4 bot left


variable.penup()
variable.goto(120, 0)   #30, 0
variable.showturtle()          
variable.pendown()
t7 = (variable, square, 270, 10, 200, 0.97, mid, end) #3/4 mid left


names.penup()
names.goto(-40, 60)   #-10, 10
names.showturtle()          
names.pendown()
t8 = (names, square, 315, 10, 220, 0.96, bright, end) #bright up left
fibo([t1, t2, t3, t4, t5, t6, t7, t8], 42, 800, 800)

sk.hideturtle()
sk2.hideturtle()
jp.hideturtle()
ran.hideturtle()
out.hideturtle()
of.hideturtle()
variable.hideturtle()
names.hideturtle()

ts = turtle.getscreen()
ts.getcanvas().postscript(file = "test7.eps")