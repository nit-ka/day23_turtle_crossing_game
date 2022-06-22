from turtle import Turtle

FONT = ("Courier", 18, "normal")
LEVEL_POS = (-280, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.update_level()

    def level_up(self):
        self.level += 1

    def update_level(self):
        self.clear()
        self.goto(LEVEL_POS)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over_msg(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)

    def start_game_msg(self):
        self.goto(0, -50)
        self.write("Press space if you want to start game", align="center", font=FONT)

    def play_again_msg(self):
        self.goto(0, -50)
        self.write("Press space if you want to play again", align="center", font=FONT)
