from turtle import Turtle
from arts import logo

FONT = ("Courier", 16, "normal")
TITLE_FONT = ("Courier", 20, "bold")

class StartScreen:
    def __init__(self):
        self.logo_turtle = Turtle()
        self.logo_turtle.hideturtle()
        self.logo_turtle.penup()
        self.logo_turtle.color("white")

        self.instruction_turtle = Turtle()
        self.instruction_turtle.hideturtle()
        self.instruction_turtle.penup()
        self.instruction_turtle.color("white")

        self.logo_x = 300
        self.logo_speed = 5

    def show_instructions(self):
        self.instruction_turtle.goto(0, -200)
        instructions = [
            "游戏玩法:",
            "",
            "↑ 或 空格键 - 向前移动",
            "按住按键可持续移动",
            "Esc - 暂停/继续游戏",
            "",
            "按任意键开始游戏..."
        ]
        y_pos = -150
        for line in instructions:
            self.instruction_turtle.goto(0, y_pos)
            self.instruction_turtle.write(line, align="center", font=FONT)
            y_pos -= 30

    def animate_logo(self):
        self.logo_turtle.clear()
        self.logo_turtle.goto(self.logo_x, 100)
        self.logo_turtle.write(logo, align="center", font=("Courier", 10, "normal"))

        self.logo_x -= self.logo_speed
        if self.logo_x < -300:
            self.logo_x = 300

    def clear(self):
        self.logo_turtle.clear()
        self.instruction_turtle.clear()
