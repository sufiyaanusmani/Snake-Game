from turtle import Turtle
STARTINGPOSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEDISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]
    
    def createSnake(self):
        for position in STARTINGPOSITIONS:
            self.addSegment(position)
            
    def addSegment(self, position):
        newSegment = Turtle("square")
        newSegment.penup()
        newSegment.color("white")
        newSegment.goto(position)
        self.segments.append(newSegment)

    def extend(self):
        self.addSegment(self.segments[-1].position())


    def move(self):
        for segmentNum in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[segmentNum - 1].xcor()
            newY = self.segments[segmentNum - 1].ycor()
            self.segments[segmentNum].goto(newX, newY)
        self.segments[0].forward(MOVEDISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)