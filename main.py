from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Race")
screen.tracer(0)

# Set up player, cars and scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for player input
screen.listen()
screen.onkey(player.move, "Up")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    # Generate new car and move existing cars
    car_manager.create_car()
    car_manager.move()

    # If player contacts car, stop game
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False

    # If player gets to top of screen, increase level (reset player position and increase car speed)
    if player.ycor() > 300:
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.increase_score()

scoreboard.game_over()

screen.exitonclick()
