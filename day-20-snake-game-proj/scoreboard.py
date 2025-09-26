from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")
MENU_FONT = ("Arial", 18, "bold")
SCORE_POSITION_Y = 270


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, SCORE_POSITION_Y)
        self._draw_score()

        self.message_writer = Turtle()
        self.message_writer.hideturtle()
        self.message_writer.color("white")
        self.message_writer.penup()

    def increase_score(self):
        self.score += 1
        self._draw_score()

    def _draw_score(self):
        self.clear()
        self.goto(0, SCORE_POSITION_Y)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.score = 0
        self.clear_messages()
        self._draw_score()

    def clear_messages(self):
        self.message_writer.clear()

    def display_end_menu(self):
        self.clear_messages()
        self.message_writer.goto(0, 40)
        self.message_writer.write("Game Over", align=ALIGNMENT, font=FONT)
        self.message_writer.goto(0, -10)
        self.message_writer.write("R - \u91cd\u65b0\u5f00\u59cb", align=ALIGNMENT, font=MENU_FONT)
        self.message_writer.goto(0, -50)
        self.message_writer.write("Q - \u9000\u51fa", align=ALIGNMENT, font=MENU_FONT)
