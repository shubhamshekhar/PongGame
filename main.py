from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def add_partition():
    pointer.color("white")
    pointer.shape("square")
    pointer.width(10)
    pointer.penup()
    pointer.goto(0, 220)
    pointer.right(90)
    for _ in range(15):
        pointer.pendown()
        pointer.forward(10)
        pointer.penup()
        pointer.forward(30)
    pointer.hideturtle()


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
pointer = Turtle()
add_partition()

paddle_right = Paddle(350)
paddle_left = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_right.go_up, "Up")
screen.onkeypress(paddle_right.go_down, "Down")


screen.onkeypress(paddle_left.go_up, "w")
screen.onkeypress(paddle_left.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.update_ball_position()
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    screen.update()

screen.exitonclick()