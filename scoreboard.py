from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0 
        self.update_scoreboard()    

    def update_scoreboard(self):
        """Updares scoreboard"""
        self.clear()
        self.goto(-100,200)
        self.write(arg=self.l_score,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(arg = self.r_score,align="center",font=("Courier",80,"normal"))

    def l_point(self):
        """Increases score of left paddle"""
        self.l_score +=1
        self.update_scoreboard()
        
    def r_point(self):
        """Increases score of right paddle"""
        self.r_score +=1
        self.update_scoreboard()
    