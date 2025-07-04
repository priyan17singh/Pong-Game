from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.color("white")
        self.goto(position)

    def go_up(self):
        if self.ycor() < 240:
            new_y=self.ycor()+20
            self.goto(self.xcor(),new_y)
    
    def go_down(self):
        if self.ycor() > -240:
            new_y=self.ycor()-20
            self.goto(self.xcor(),new_y)

    



