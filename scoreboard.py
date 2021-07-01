from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setpos(-290, 265)
        self.write(f"Level: {self.level}", False, align="left", font=('Courier', 20, 'bold'))

    def increase_score(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", False, align="center", font=('Courier', 20, 'bold'))
