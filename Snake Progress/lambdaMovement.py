# import turtle graphics module
import turtle
import random

# define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 150
FOODSIZE = 10
SCORE = 0

# set direction of snake movement
DIRECTION = "up"
# set how much the snake moves in each direction
offsets = {"up": (0, 20), "down": (0, -20), "left": (-20, 0), "right": (20, 0)}


def bind_direction_keys():
  screen.onkey(lambda: set_direction("up"), "Up")
  screen.onkey(lambda: set_direction("down"), "Down")
  screen.onkey(lambda: set_direction("right"), "Right")
  screen.onkey(lambda: set_direction("left"), "Left")


def set_direction(dir):
  global DIRECTION
  if dir == "up" and DIRECTION != "down":
    DIRECTION = "up"
  if dir == "down" and DIRECTION != "up":
    DIRECTION = "down"
  if dir == "right" and DIRECTION != "left":
    DIRECTION = "right"
  if dir == "left" and DIRECTION != "right":
    DIRECTION = "left"


def game_loop():
  stamper.clearstamps()

  new_head = snake[-1].copy()
  new_head[0] += offsets[DIRECTION][0]
  new_head[1] += offsets[DIRECTION][1]

  # check wall/snake and snake/snake collisions
  if new_head in snake or new_head[0] < -WIDTH/2 or new_head[0] > WIDTH/2 \
    or new_head[1] < -HEIGHT/2 or new_head[1] > HEIGHT/2:
    reset()
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


def reset():
  global SCORE, snake, DIRECTION, food_pos
  SCORE = 0
  # snake representation (list of pairs of coords)
  snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

  food_pos = get_random_food_pos()
  food.goto(food_pos)

  game_loop()


# create window
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("white")
screen.tracer(0)

# event handlers
screen.listen()
bind_direction_keys()

# create turtle
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

food = turtle.Turtle()
food.shape("circle")
food.shapesize(FOODSIZE / 20)
food.color("green")
food.penup()

reset()

# end program
turtle.done()
