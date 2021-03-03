from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)

    def update_scoreboard(self):
        self.write(f"Score : {self.score}   High score : {self.high_score}", align="center", font=("Courier", 20, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
        self.clear()

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER.", align="center", font=("Courier", 20, "normal"))
