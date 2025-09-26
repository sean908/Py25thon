from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SELF_COLLISION_DISTANCE = 10

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def hit_wall(self, boundary_limit: int) -> bool:
        x_cor = self.head.xcor()
        y_cor = self.head.ycor()
        return (
            x_cor > boundary_limit
            or x_cor < -boundary_limit
            or y_cor > boundary_limit
            or y_cor < -boundary_limit
        )

    def collided_with_self(self) -> bool:
        return any(
            self.head.distance(segment) < SELF_COLLISION_DISTANCE
            for segment in self.segments[1:]
        )

    def hide(self):
        for segment in self.segments:
            segment.hideturtle()
