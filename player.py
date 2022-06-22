from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.reset_position()
        self.shape("turtle")
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def move_left(self):
        if self.xcor() > -280:
            self.goto(self.xcor()-10, self.ycor())

    def move_right(self):
        if self.xcor() < 280:
            self.goto(self.xcor() + 10, self.ycor())

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


