import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_SIZE = 600
BOUNDARY_LIMIT = (SCREEN_SIZE // 2) - 20
MOVE_INTERVAL_MS = 120  # milliseconds between frames; lower for faster response

screen = t.Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor("black")
screen.title("a Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


GAME_ACTIVE = False

def trigger_game_over():
    global GAME_ACTIVE
    GAME_ACTIVE = False
    snake.hide()
    food.hideturtle()
    scoreboard.display_end_menu()
    screen.update()


def game_loop():
    if not GAME_ACTIVE:
        return

    snake.move()

    if snake.head.distance(food) < 15:
        snake.grow()
        food.refresh()
        scoreboard.increase_score()

    if snake.hit_wall(BOUNDARY_LIMIT) or snake.collided_with_self():
        trigger_game_over()
        return

    screen.update()
    screen.ontimer(game_loop, MOVE_INTERVAL_MS)


def start_new_game():
    global GAME_ACTIVE
    scoreboard.reset()
    snake.reset()
    food.showturtle()
    food.refresh()
    GAME_ACTIVE = True
    screen.update()
    game_loop()


def restart_game():
    if GAME_ACTIVE:
        return
    start_new_game()


def exit_game():
    screen.bye()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(restart_game, "r")
screen.onkey(restart_game, "R")
screen.onkey(exit_game, "q")
screen.onkey(exit_game, "Q")

screen.update()
start_new_game()
screen.exitonclick()
