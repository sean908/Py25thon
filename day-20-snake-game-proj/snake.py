from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SELF_COLLISION_DISTANCE = 10

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

OPPOSITE_DIRECTIONS = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT,
}


class Snake:
    def __init__(self):
        self.segments: list[Turtle] = []
        self.direction_change_allowed = True
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self._add_segment(position)

    def _add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        for seg_idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_idx - 1].xcor()
            new_y = self.segments[seg_idx - 1].ycor()
            self.segments[seg_idx].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        self.direction_change_allowed = True

    def up(self):
        self._change_heading(UP)

    def down(self):
        self._change_heading(DOWN)

    def left(self):
        self._change_heading(LEFT)

    def right(self):
        self._change_heading(RIGHT)

    def _change_heading(self, new_heading):
        if not self.direction_change_allowed:
            return
        if self.head.heading() == OPPOSITE_DIRECTIONS[new_heading]:
            return
        if self.head.heading() == new_heading:
            return
        self.head.setheading(new_heading)
        self.direction_change_allowed = False

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

    def grow(self):
        tail_position = self.segments[-1].position()
        self._add_segment(tail_position)

    def hide(self):
        for segment in self.segments:
            segment.hideturtle()

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.direction_change_allowed = True
        self.create_snake()
        self.head = self.segments[0]
        for segment in self.segments:
            segment.showturtle()
