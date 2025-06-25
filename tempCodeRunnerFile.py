def go_down(self):
        # if self.ycor() > -240:
            new_y=self.ycor()-20
            self.goto(self.xcor(),new_y)
