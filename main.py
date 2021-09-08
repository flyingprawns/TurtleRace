from turtle import Turtle, Screen


# Create turtles and screen
turtle_count = 6
my_turtles = []
for i in range(turtle_count):
    my_turtles.append(Turtle(shape='turtle'))
screen = Screen()

# Set turtle colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for i in range(turtle_count):
    my_turtles[i].color(colors[i])

# Setup screen
screen.setup(width=500, height=400)

# Get user to place a bet
user_bet = screen.textinput(title='Make your bet!', prompt='Which turtle will win the race? Enter a color: ')
print(user_bet)


# Move some turtles



# Exit program on user click
screen.exitonclick()
print('Turtle race is over. Hope you had fun!')
