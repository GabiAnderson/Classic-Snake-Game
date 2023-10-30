# import turtle graphics module
import turtle

# define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 20  # milliseconds between screen updates


def move_turtle():
  my_turtle.forward(1)
  my_turtle.right(1)
  screen.update()
  screen.ontimer(move_turtle, DELAY)


# create window
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Program Title")
screen.bgcolor("cyan")
screen.tracer(0)  # turns of auto animation

# create turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")

# set animation in motion
move_turtle()

# end program
turtle.done()
