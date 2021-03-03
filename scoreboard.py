from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data_file:
            self.high_score = int(data_file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)

    def update_scoreboard(self):
        self.write(f"Score : {self.score}   High score : {self.high_score}", align="center", font=("Courier", 20, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data_file:
                data_file.write(f"{self.high_score}")
            self.score = 0
        self.clear()

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER.", align="center", font=("Courier", 20, "normal"))
