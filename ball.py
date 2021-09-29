from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 20
        self.y_move = 20
        self.move_speed = 0.1

    def update_ball_position(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.detect_ball_collision(new_y)
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1

    def detect_ball_collision(self, new_y):
        if new_y > 260 or new_y < -260:
            self.bounce_y()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
