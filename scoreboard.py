from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.updateScoreboard()
        

    def updateScoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()

    def gameOver(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=("Courier", 24, "normal"))
        self.goto(0, 260)
    
