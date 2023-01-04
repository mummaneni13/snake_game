from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("yellow")
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))



