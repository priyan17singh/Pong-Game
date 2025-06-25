from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Moves the ball forward"""
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        """Bounces the ball in x direction"""
        self.y_move *= -1
        self.move_speed -= 0.01

    def bounce_x(self):
        """Bounces the ball in y direction"""
        self.x_move *= -1
        self.move_speed -= 0.01

    def refresh(self):
        """Moves the ball to position (0,0)"""
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1
        time.sleep(0.5)
