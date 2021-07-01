from turtle import Turtle
import random

CAR_COLOURS = ["red", "yellow", "pink", "green", "orange", "purple", "blue"]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = 5

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(CAR_COLOURS))
            random_y = random.randint(-240, 240)
            new_car.goto(320, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.back(self.move_speed)

    def increase_speed(self):
        self.move_speed += 5
