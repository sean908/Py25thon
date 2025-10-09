from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.is_moving = False

    def start_moving(self):
        self.is_moving = True

    def stop_moving(self):
        self.is_moving = False

    def move(self):
        if self.is_moving:
            self.forward(MOVE_DISTANCE)

    def go_up(self):
        # 兼容简单的按键移动
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
        self.is_moving = False