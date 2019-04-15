# Concave Ray Diagrams

# Initial Setup Stuff
import turtle
from math import sqrt
SCREEN_X = 100
SCREEN_Y = 100
SCREEN_SUM = SCREEN_X + SCREEN_Y
turtle.screensize(SCREEN_X, SCREEN_Y)

mirror_points = []

centre_of_curvature = 0
focal_point = centre_of_curvature * 2

first = 0

object_points = []
image_points = []

# Conscription of turtles
worker = turtle.Turtle()
ray = turtle.Turtle()


def setup(radius=SCREEN_X * 3, extent=SCREEN_SUM//4, dot_size=(SCREEN_SUM)//20):
    global focal_point, centre_of_curvature, mirror_points, principal_line_points

    # Sicko mode
    worker.speed(0)

    # Drawing Principal Line
    worker.penup()
    worker.setpos((worker.screen.window_height()/2) + 21, 0)
    worker.pendown()
    worker.setpos(-1 * ((worker.screen.window_height()/2) + 21), 0)
    worker.penup()
    worker.setpos(0, 0)
    worker.pendown()

    # Drawing Concave Mirror
    worker.left(90)
    worker.pensize(10)

    worker.circle(radius, extent)
    
    worker.penup()
    worker.setpos(0, 0)
    
    worker.pendown()
    worker.setheading(270)
    
    worker.circle(-1 * radius, extent)

    worker.penup()
    

    # Labelling & Drawing Points

    focal_point = radius // 2
    centre_of_curvature = radius

    worker.setpos(-1 * centre_of_curvature, 0)
    worker.pendown()
    worker.dot(dot_size)
    worker.penup()
    worker.sety(SCREEN_SUM / -6.6)
    worker.write("C", False, "center", ("Comic Sans", 18, "normal"))

    worker.setpos(-1 * focal_point, 0)
    worker.pendown()
    worker.dot(dot_size)
    worker.penup()
    worker.sety(SCREEN_SUM / -6.6)
    worker.write("F", False, "center", ("Comic Sans", 18, "normal"))

    # Resetting pensize
    worker.pensize(1)
    worker.hideturtle()


def draw_object(x_pos, height=SCREEN_Y//6):
    global object_points

    x_pos = -1 * x_pos

    object_points = [[x_pos, 0], [x_pos, height]]

    worker.pencolor("violet")
    worker.pensize(3)

    worker.penup()
    worker.setpos(x_pos, 0)
    worker.setheading(90)
    worker.pendown()
    worker.forward(height)
                                
    worker.right(45)
    worker.backward(height//3)
    worker.penup()
    worker.forward(height//3)
                                
    worker.left(90)
    worker.pendown()
    worker.backward(height//3)
    worker.penup()
    worker.forward(height//3)
                                
    worker.setheading(90)
    worker.home()

    worker.pencolor("black")
    worker.pensize(1)

setup()

while True:
    # distance = input("How far from mirror? (Range: 0 - {}): ".format(int(SCREEN_SUM * 1.75)))
    distance = 200
    try:
        distance = int(distance)
        if distance > SCREEN_SUM * 1.75:
            0/0
        break
    except:
        print("Please provide an integer in the range")
    
draw_object(distance)

# I'm done

"""
More to do:

Adding lines to reflect off concave surface
Making the image

"""





