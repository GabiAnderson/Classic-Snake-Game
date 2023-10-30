# import turtle graphics module
import turtle

# define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 400

# set direction of snake movement
DIRECTION = "up"
# set how much the snake moves in each direction
offsets = {"up": (0, 20), "down": (0, -20), "left": (-20, 0), "right": (20, 0)}


# event callback
def go_up():
  global DIRECTION
  if DIRECTION != "down":
    DIRECTION = "up"


# event callback
def go_down():
  global DIRECTION
  if DIRECTION != "up":
    DIRECTION = "down"


# event callback
def go_right():
  global DIRECTION
  if DIRECTION != "left":
    DIRECTION = "right"


# event callback
def go_left():
  global DIRECTION
  if DIRECTION != "right":
    DIRECTION = "left"


def game_loop():
  stamper.clearstamps()

  new_head = snake[-1].copy()
  new_head[0] += offsets[DIRECTION][0]
  new_head[1] += offsets[DIRECTION][1]

  # check wall/snake and snake/snake collisions
  if new_head in snake or new_head[0] < -WIDTH/2 or new_head[0] > WIDTH/2 \
    or new_head[1] < -HEIGHT/2 or new_head[1] > HEIGHT/2:
    turtle.bye()  # end program
  else:
    snake.append(new_head)

    snake.pop(0)

    # draw snake
    for segment in snake:
      stamper.goto(segment[0], segment[1])
      stamper.stamp()

    screen.update()

    turtle.ontimer(game_loop, DELAY)


# create window
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("white")
screen.tracer(0)

# event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

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

game_loop()

# end program
turtle.done()
