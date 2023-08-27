from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height= 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles =[]

y_cor = 0
for i in range (0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + y_cor)
    y_cor+=30
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            if (turtle.color()==user_bet):
                print(f"Correct! The turtle that has won the race is {user_bet}.")
            else:
                print(f"Wrong! The turtle that has won the race is {turtle.pencolor()}.")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()