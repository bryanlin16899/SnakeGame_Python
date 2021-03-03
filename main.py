from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My first snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")


is_on = True
while is_on:
    screen.update()
    scoreboard.update_scoreboard()
    time.sleep(0.1)
    snake.move()

#Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.refresh_score()
        snake.extend_body()

#Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_score()
        snake.reset_body()

#Detect collision with tail
    for seg in snake.body[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset_score()
            snake.reset_body()


screen.exitonclick()