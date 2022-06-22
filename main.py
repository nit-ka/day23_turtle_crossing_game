import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing game")
screen.tracer(0)


scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_new_car()
    car_manager.move_cars()

    if player.at_finish_line():
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.level_up()
        scoreboard.update_level()

    for car in car_manager.cars:
        collision = abs(car.ycor() - player.ycor()) < 20 and abs(car.xcor() - player.xcor()) < 28
        if collision:
            scoreboard.game_over_msg()
            game_is_on = False

screen.exitonclick()
