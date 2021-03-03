from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def add_body(self, position):
        new_snake_body = Turtle("square")
        new_snake_body.color("white")
        new_snake_body.penup()
        new_snake_body.goto(position)
        self.body.append(new_snake_body)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body(position)

    def move(self):
        for seg in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg - 1].xcor()
            new_y = self.body[seg - 1].ycor()
            self.body[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset_body(self):
        for seg in self.body:
            seg.goto(1000, 1000)
        self.body = []
        self.create_snake()
        self.head = self.body[0]


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend_body(self):
        self.add_body(self.body[-1].position())
