from turtle import Turtle, Screen

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
user_bet = screen.textinput(title='Make your bet!', prompt='Which turtle will win the race? Enter a color: ')
print(user_bet)

# Move turtles to starting positions
y_position = -135
for turtle in my_turtles:
    turtle.penup()
    turtle.goto(-225, y_position)
    turtle.pendown()
    y_position += 55

# Exit program on user click
screen.exitonclick()
print('Turtle race is over. Hope you had fun!')
