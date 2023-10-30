# import turtle graphics module
import turtle

# define program constants
WIDTH = 500
HEIGHT = 500

# create window
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Stamping")
screen.bgcolor("cyan")

# create turtle
stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("blue")
stamper.shapesize(50 / 20)  # sets pixel control to 50 pixels
stamper.stamp()
stamper.penup()
stamper.shapesize(10 / 20)
stamper.goto(100, 100)
stamper.stamp()

# end program
turtle.done()
