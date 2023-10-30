# import turtle graphics module
import turtle

# define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 400


def move_snake():
  stamper.clearstamps()

  new_head = snake[-1].copy()
  new_head[0] += 20

  snake.append(new_head)

  snake.pop(0)

  # draw snake
  for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

  screen.update()

  turtle.ontimer(move_snake, DELAY)


# create window
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("white")
screen.tracer(0)

# create turtle
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# snake representation (list of pairs of coords)
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

# draw snake
for segment in snake:
  stamper.goto(segment[0], segment[1])
  stamper.stamp()

move_snake()

# end program
turtle.done()
