# import turtle graphics module
import turtle
import random

# define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 200
FOODSIZE = 5
SCORE = 0

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

    # check for food collision
    if not food_collision():
      snake.pop(0)  # snake does not grow bc no food

    # draw snake
    for segment in snake:
      stamper.goto(segment[0], segment[1])
      stamper.stamp()

    screen.title(f"Snake Game. Score: {SCORE}")
    screen.update()

    turtle.ontimer(game_loop, DELAY)


def get_distance(pos1, pos2):
  x1, y1 = pos1
  x2, y2 = pos2
  distance = ((y2 - y1)**2 + (x2 - x1)**2)**0.5  # pythagorean theorem
  return distance


def food_collision():
  global food_pos
  global SCORE
  if get_distance(snake[-1], food_pos) < 20:
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    SCORE += 1
    return True
  return False


def get_random_food_pos():
  x = random.randint(-WIDTH / 2 + FOODSIZE, WIDTH / 2 - FOODSIZE)
  y = random.randint(-HEIGHT / 2 + FOODSIZE, HEIGHT / 2 - FOODSIZE)
  return (x, y)


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

food = turtle.Turtle()
food.shape("circle")
food.shapesize(FOODSIZE / 20)
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)

game_loop()

# end program
turtle.done()