from turtle import Turtle

MOVE_SPEED = 10
STARTING_POSITION = (0, -280)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move(self):
        new_y = self.ycor() + MOVE_SPEED
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(STARTING_POSITION)
