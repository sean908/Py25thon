import turtle as t
import time
from snake import Snake

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("a Snake Game")

screen.tracer(0)
snake = Snake()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.38)

    snake.move()
    # segmemts[0].right(90)


screen.exitonclick()