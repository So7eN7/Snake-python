from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Constants
FOOD_COLLISION = 15

# Setting up our screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.bgcolor("dark blue")
screen.tracer(0)  # Updating it later

# Creating our game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Getting user inputs
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game logic
is_game_running = True
while is_game_running:
    screen.update()  # Updating the screen
    time.sleep(0.1)  # 0.1 seconds of sleep
    snake.move()     # Snake moving based on inputs

    # Food collision
    if snake.head.distance(food) < FOOD_COLLISION:
        food.refresh()  # If the snake has reached the food then generate another one
        snake.extend()  # Extend the snake
        scoreboard.increase_score()  # Increase the score
    # Border/Wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_running = False  # If the snake has hit the border
        scoreboard.gameover()    # Game is done
    # Snake colliding with itself
    for segment in snake.segments:
        if segment == snake.head:  # Making sure the game is not over from the start (check snake.py move function)
            pass
        elif snake.head.distance(segment) < 10:  # If the body comes in contact with the head commence gameover
            is_game_running = False
            scoreboard.gameover()

screen.exitonclick()