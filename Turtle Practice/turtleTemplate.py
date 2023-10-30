# import turtle graphics module
import turtle

# define program constants
WIDTH = 500
HEIGHT = 500

# create window
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Program Title")
screen.bgcolor("cyan")

# create turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")

# sample command
my_turtle.forward(100)

# end program
turtle.done()
