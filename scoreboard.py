from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align="center" ,font=("Courier", 20, "normal"))

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=("Courier", 20, "normal"))

