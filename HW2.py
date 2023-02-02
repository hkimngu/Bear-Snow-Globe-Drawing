# Your name: Kim Nguyen
# Your student id: 98652556
# Your email: hkimngu@umich.edi
# List who you worked with on this homework: n/a

from turtle import *

### write all new functions here ###
def draw_circle(turtle, color, radius, x_pos, y_pos):
    turtle.penup()
    turtle.goto(x_pos, y_pos)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_triangle(turtle, color, length, x_pos, y_pos):
    turtle.penup()
    turtle.goto(x_pos, y_pos)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color(color)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(length)
        turtle.right(120)
    turtle.end_fill()

def draw_rectangle(turtle, color, length, height, x_pos, y_pos):
    turtle.penup()
    turtle.goto(x_pos, y_pos)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_snowflake(turtle, color, length, x_pos, y_pos):
    turtle.penup()
    turtle.goto(x_pos, y_pos)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color(color)
    for i in range(8):
        if i % 2 == 0:
            turtle.forward(length)
            turtle.left(25)
            turtle.forward(length / 4)
            turtle.backward(length / 4)
            turtle.right(50)
            turtle.forward(length / 4)
            turtle.backward(length / 4)
            turtle.left(25)
            turtle.backward(length)
            turtle.left(45)
        else:
            turtle.forward(length / 2)
            turtle.left(25)
            turtle.forward(length / 4)
            turtle.backward(length / 4)
            turtle.right(50)
            turtle.forward(length / 4)
            turtle.backward(length / 4)
            turtle.left(25)
            turtle.backward(length / 2)
            turtle.left(45)

def draw_k(turtle):
    draw_rectangle(turtle, "firebrick", 20, 90, -90, -120)
    turtle.setheading(310)
    draw_rectangle(turtle, "firebrick", 20, 70, -30, -110)
    turtle.setheading(50)
    draw_rectangle(turtle, "firebrick", 20, 70, -80, -170)

def draw_n(turtle):
    turtle.setheading(0)
    draw_rectangle(turtle, "firebrick", 20, 90, 10, -120)
    turtle.setheading(32)
    draw_rectangle(turtle, "firebrick", 20, 90, 13, -133)
    turtle.setheading(0)
    draw_rectangle(turtle, "firebrick", 20, 90, 63, -120)


def draw_globe(turtle):
    """
    Write a function to draw a snow globe scene.

    Feel free to modify the arguments of this function as you like,
    but you should pass in the turtle object at the very least.

    You can earn extra credit for including you initials in your drawing.
    See the instructions for more details.
    """
    # draw globe
    draw_circle(turtle, "light blue", 200, 0, -160)

    # draw snowflakes
    draw_snowflake(turtle, "lavender", 10, -160, 25)
    draw_snowflake(turtle, "lavender", 10, -130, 60)
    draw_snowflake(turtle, "lavender", 10, -70, 0)
    draw_snowflake(turtle, "lavender", 10, 80, -20)
    draw_snowflake(turtle, "lavender", 10, 140, 40)
    draw_snowflake(turtle, "lavender", 10, 160, 10)
    draw_snowflake(turtle, "white", 20, -130, -30)
    draw_snowflake(turtle, "white", 20, -100, 30)
    draw_snowflake(turtle, "white", 20, 90, 30)
    draw_snowflake(turtle, "white", 20, 130, -35)

    # background snow
    draw_circle(turtle, "lavender", 45, -80, -150)
    draw_circle(turtle, "lavender", 60, -40, -150)
    draw_circle(turtle, "lavender", 50, 50, -150)
    draw_circle(turtle, "lavender", 35, 90, -150)

    # draw bear body
    draw_circle(turtle, "peru", 60, 0, -100)
    draw_circle(turtle, "peru", 60, 0, -120)
    draw_circle(turtle, "peachpuff", 40, -10, -80)
    draw_circle(turtle, "peachpuff", 40, -10, -90)

    # draw foreground snow
    draw_circle(turtle, "white", 20, -80, -130)
    draw_circle(turtle, "white", 35, -40, -130)
    draw_circle(turtle, "white", 25, 10, -130)
    draw_circle(turtle, "white", 30, 50, -130)
    draw_circle(turtle, "white", 20, 90, -130)

    # draw background clouds
    draw_circle(turtle, "lavender", 38, -80, 110)
    draw_circle(turtle, "lavender", 54, -40, 110)
    draw_circle(turtle, "lavender", 44, 50, 110)
    draw_circle(turtle, "lavender", 26, 90, 110)

    # draw foreground clouds
    draw_circle(turtle, "white", 20, -150, 90)
    draw_circle(turtle, "white", 35, -110, 90)
    draw_circle(turtle, "white", 25, -60, 90)
    draw_circle(turtle, "white", 40, -20, 90)
    draw_circle(turtle, "white", 30, 20, 90)
    draw_circle(turtle, "white", 20, 80, 70)
    draw_circle(turtle, "white", 35, 110, 70)
    draw_circle(turtle, "white", 20, 150, 70)

    # draw ears
    draw_circle(turtle, "peru", 17, -30, 75)
    draw_circle(turtle, "peru", 17, 35, 70)
    draw_circle(turtle, "peachpuff", 6, -30, 85)
    draw_circle(turtle, "peachpuff", 6, 35, 80)

    # draw bear head
    draw_circle(turtle, "peru", 50, 0, 0)
    draw_circle(turtle, "peachpuff", 20, -10, 15)
    draw_circle(turtle, "pink", 6, -38, 38)
    draw_circle(turtle, "pink", 6, 18, 38)
    draw_triangle(turtle, "black", 10, -20, 45)
    turtle.setheading(300)
    turtle.forward(20)
    turtle.backward(10)
    turtle.right(70)
    turtle.forward(10)

    # draw scarf
    turtle.setheading(0)
    draw_rectangle(turtle, "dark red", 90, 23, -45, 20)
    draw_rectangle(turtle, "firebrick", 35, 80, 0, 20)

    # draw eyes
    draw_circle(turtle, "black", 7, -30, 50)
    draw_circle(turtle, "black", 7, 10, 50)
    draw_circle(turtle, "lavender", 2, -26, 58)
    draw_circle(turtle, "lavender", 2, 14, 58)
    draw_circle(turtle, "white", 3, -31, 50)
    draw_circle(turtle, "white", 3, 8, 50)

    # draw base
    draw_rectangle(turtle, "dark red", 280, 100, -140, -110)
    draw_k(turtle)
    draw_n(turtle)
    draw_rectangle(turtle, "firebrick", 290, 10, -145, -105)
    draw_rectangle(turtle, "firebrick", 300, 10, -150, -210)    


def main():
    """
    Make sure to create a Screen object, a Turtle object,
    and call draw_globe.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting until you close the drawing window.

    TIP: You can call the .bgcolor() method on your Screen instance to change
    the background color.
    """

    background = Screen()
    background.bgcolor("light sky blue")
    t1 = Turtle()
    t1.speed(11)
    draw_globe(t1)
    background.exitonclick()


if __name__ == '__main__':
    main()
