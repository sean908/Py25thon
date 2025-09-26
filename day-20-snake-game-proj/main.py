import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_SIZE = 600
MOVE_INTERVAL_MS = 120  # milliseconds between frames; lower for faster response

screen = t.Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor("black")
screen.title("a Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


def game_loop():
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

    screen.update()
    screen.ontimer(game_loop, MOVE_INTERVAL_MS)


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
game_loop()
screen.exitonclick()
