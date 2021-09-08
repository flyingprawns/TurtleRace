from turtle import Turtle, Screen
import random


def reached_finish_line(a_turtle):
    if a_turtle.xcor() >= 240:
        return True
    else:
        return False


# Create turtles
turtle_count = 6
my_turtles = []
for i in range(turtle_count):
    my_turtles.append(Turtle(shape='turtle'))

# Set turtle colors
colors = ['red', 'orange', 'gold', 'green', 'blue', 'purple']
for i in range(turtle_count):
    my_turtles[i].color(colors[i])

# Setup screen
screen = Screen()
screen.setup(width=500, height=400)

# Get user to place a bet
your_bet = screen.textinput(title='Make your bet!', prompt='Which turtle will win the race? Enter a color: ')

# Move turtles to starting positions
y_position = -135
for turtle in my_turtles:
    turtle.penup()
    turtle.goto(-225, y_position)
    turtle.pendown()
    y_position += 55

# Turtles start racing
winner_color = ''
race_over = False
while not race_over:
    for turtle in my_turtles:
        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)
        if reached_finish_line(turtle):
            winner_color = turtle.pencolor()
            race_over = True
            break

# Display winner
print(f'The {winner_color} turtle has won the game!')
if your_bet == winner_color:
    print('You won!!! Congratulations!')
else:
    print('You lost, sorry :(')

# Exit program on user click
screen.exitonclick()
print('Turtle race is over. Hope you had fun!')
