# Classic Snake Game
Recreation the classic snake game in Python using Turtle Graphics

**Final game can be found in main.py**

---
## [Turtle Practice](https://github.com/GabiAnderson/Classic-Snake-Game/tree/main/Turtle%20Practice)
Here I will cover the different files found in the folder Turtle Practice.
### [squareTurtlePractice.py](https://github.com/GabiAnderson/Classic-Snake-Game/blob/main/Turtle%20Practice/squareTurtlePractice.py)
Here I implemented a very basic square drawing turtle to get an understanding of how the turtle library works.
### [customTurtlePractice.py](https://github.com/GabiAnderson/Classic-Snake-Game/blob/main/Turtle%20Practice/customTurtlePractice.py)
Building off my previous squareTurtlePractice.py, I implemented a custom turtle that had a custom shape and color.
### [stamperTurtlePractice.py](https://github.com/GabiAnderson/Classic-Snake-Game/blob/main/Turtle%20Practice/stamperTurtlePractice.py)
Building off my customTurtlePractice.py, I turned my custom turtle from a drawing turtle to a stamping turtle.
### [customAnimationTurtlePractice.py](https://github.com/GabiAnderson/Classic-Snake-Game/blob/main/Turtle%20Practice/customAnimationTurtlePractice.py)
Building off my customTurtlePractice.py, I worked with cutom animation updates for my turtle.
### [turtleTemplate.py](https://github.com/GabiAnderson/Classic-Snake-Game/blob/main/Turtle%20Practice/turtleTemplate.py)
I took out the practice components from stamperTurtlePractice.py to create this template that acted as my starting point for my snake game.

---
## [Snake Progress](https://github.com/GabiAnderson/Classic-Snake-Game/tree/main/Snake%20Progress)
Here I will cover my progress from turtleTemplate.py to my final snake game.
### [snakeMoveRightUpdateLook.py](https://github.com/GabiAnderson/Classic-Snake-Game/blob/main/Snake%20Progress/snakeMoveRightUpdateLook.py)
The first step was to create my snake, draw it on the screen, and get it to move/update properly. I stored my snake segments as a list of pairs of coordinates where the first element is the tail of the snake and the last element is the head. I utilized my stamp knowledge to draw my snake segments as stamps. I then started a loop that would move my snake right across the screen. I would clear all my stamps, create a copy of the head, move the copied head to the right one "square", remove the tail of the snake, and finally redraw the snake. I had this in a loop that would call itself again after a delay of 400 milliseconds.
### [controlSnakeMovement.py](https://github.com/GabiAnderson/Classic-Snake-Game/blob/main/Snake%20Progress/controlSnakeMovement.py)
Instead of having my snake move right off the screen, I used key binds and event handling to allow the arrow keys to move the snake. It required stored my offset directions in a dictionary and properly calling the correct offset based on which key was pressed.
### [collisionGameLoop.py](https://github.com/GabiAnderson/Classic-Snake-Game/blob/main/Snake%20Progress/collisionGameLoop.py)
The next step was overhauling the game loop to handle collision. I needed to handle snake-on-snake and snake-on-wall collisions. I updated my game loop to check if the new head was within the height/width constrains of my window and if the head was already and element of the snake. If either of those conditions were true the game would end.
### [foodSpawnAndCollision.py](https://github.com/GabiAnderson/Classic-Snake-Game/blob/main/Snake%20Progress/foodSpawnAndCollision.py)
The next big element of the snake game that was left to be implemented was food. I created a few functions that would spawn food, detect food-on-snake collision, and handle food-on-snake collision. My game was finally able to handle user input to control the snake and the main functionality of the snake game (eating food = growing snake). I also added a global score variable that would increment when a food peice was eaten, the score is displayed and updated in the application title.
### [gameReset.py](https://github.com/GabiAnderson/Classic-Snake-Game/blob/main/Snake%20Progress/gameReset.py)
Instead of closing the game completely when hitting a wall, I adjusted some of the initial statements before my game loop that set up the game. I moved these statements into a function that would allow the game to reset when the player dies. Meaning the game would now play again without requiring rerunning the application.
### [lambdaMovement.py](https://github.com/GabiAnderson/Classic-Snake-Game/blob/main/Snake%20Progress/lambdaMovement.py)
I went back to my key binding and event handling code where I found myself retyping the same code with slight variations (4 functions with essentially the same code). I utilized lambda's to allow for code reusability for my key bindings.
### [main.py](https://github.com/GabiAnderson/Classic-Snake-Game/blob/main/main.py)
This file holds my final game, I have tweaked timings, sizing, colors, etc to make the game as enjoyable to play while still remaining fairly simple.
