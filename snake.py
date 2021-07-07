from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snakes_piece = []
        self.create_snake()
        self.head = self.snakes_piece[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            snake = Turtle()
            snake.shape("square")
            snake.color("black")
            snake.penup()
            snake.goto(i)
            self.snakes_piece.append(snake)

    def move(self):
        for seg_num in range(len(self.snakes_piece) - 1, 0, -1):
            new_x = self.snakes_piece[seg_num - 1].xcor()
            new_y = self.snakes_piece[seg_num - 1].ycor()
            self.snakes_piece[seg_num].goto(new_x, new_y)
        self.snakes_piece[0].forward(MOVE_FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
