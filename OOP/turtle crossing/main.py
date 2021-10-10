import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()

screen.listen()

screen.onkey(player.move_turtle, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()
    score = Scoreboard()

    for c in car.all_cars:
        if c.distance(player) < 20:
            game_is_on = False
            score.game_over()
    

    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        score.increment_score()


screen.exitonclick()