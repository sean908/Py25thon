import turtle as t
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("a Snake Game")

screen.tracer(0)

# segment_1 = t.Turtle("square")
# segment_1.color("white")
#
# segment_2 = t.Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
#
# segment_3 = t.Turtle("square")
# segment_3.color("white")
# segment_3.goto(20, 0)

#starting_positions = [(-20, 0), (0, 0), (20, 0)]
starting_positions = [(20, 0), (0, 0), (-20, 0)]
# starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segmemts = []

for position in starting_positions:
    new_segment = t.Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segmemts.append(new_segment)

screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.38)
    # for seg in segmemts:
    #     seg.forward(20)
        #screen.update()
        #time.sleep(0.38)
    for seg_num in range(len(segmemts) - 1, 0, -1):
        new_x = segmemts[seg_num - 1].xcor()
        new_y = segmemts[seg_num - 1].ycor()
        segmemts[seg_num].goto(new_x, new_y)
    segmemts[0].forward(20)
    segmemts[0].right(90)


screen.exitonclick()