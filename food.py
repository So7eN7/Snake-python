from turtle import Turtle
import random


class Food(Turtle):  # Inheriting from Turtle
    def __init__(self):
        super().__init__() # Setting up our food
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):  # Generating the food
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)