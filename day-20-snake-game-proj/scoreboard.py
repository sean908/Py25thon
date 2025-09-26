from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 20, 'bold')
SCORE_POSITION_Y = 270


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, SCORE_POSITION_Y)
        self._draw_score()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(0, SCORE_POSITION_Y)
        self._draw_score()

    def _draw_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def display_game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
