from turtle import Turtle
# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):  # Setting up our snake
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):  # Adding segments to create our snake
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        '''
        Setting segments and adding them up. we got a list of segments ready to be filled
        3 initial segments are made back to back at the starting coordinates
        '''
        new_segment = Turtle("square")
        new_segment.color("cyan")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):  # Extending the snake by adding one to the tail
        self.add_segment(self.segments[-1].position())

    def move(self):
        '''
        We create 3 main segments the last segments goes over the center one, then the center one moves over the first one
        after that the first one moves. a bit complicated but a really efficient looking snake is the result (took some help for this one)
        this way of movement is why we do the checking for the head collision in main.py.
        If we don't the game will end right at the start so this is an exception which we will check
        '''
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Moving from the end to head and getting new coordinates
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Movement functions are here
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
