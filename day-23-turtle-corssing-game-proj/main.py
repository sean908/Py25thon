import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from start_screen import StartScreen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing Game")
screen.tracer(0)

# 显示开始画面
start_screen = StartScreen()
start_screen.show_instructions()

# 动画显示logo直到用户按键
waiting_for_start = True
def start_game():
    global waiting_for_start
    waiting_for_start = False

screen.listen()
screen.onkey(start_game, "space")
screen.onkey(start_game, "Up")

while waiting_for_start:
    start_screen.animate_logo()
    screen.update()
    time.sleep(0.05)

# 清除开始画面
start_screen.clear()

# 初始化游戏对象
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# 设置按键控制 - 支持持续移动
screen.listen()
screen.onkeypress(player.start_moving, "Up")
screen.onkeyrelease(player.stop_moving, "Up")
screen.onkeypress(player.start_moving, "space")
screen.onkeyrelease(player.stop_moving, "space")

# 暂停功能
game_is_paused = False
def toggle_pause():
    global game_is_paused
    game_is_paused = not game_is_paused

screen.onkey(toggle_pause, "Escape")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if not game_is_paused:
        # 移动玩家
        player.move()

        car_manager.create_car()
        car_manager.move_cars()

        # 检测碰撞
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        # 检测是否到达终点
        if player.ycor() > 280:
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()

screen.exitonclick()
