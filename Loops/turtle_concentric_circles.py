import turtle
# Named constants
NUM_CIRCLES = 20
STARTING_RADIUS = 20
OFFSET = 10
ANIMATION_SPEED = 0

# setup the turtle
turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

# set the radioud of circle
radius = STARTING_RADIUS

# Draw the circles
for count in range(NUM_CIRCLES):
    # Draw the circle
    turtle.circle(radius)

    # Get the coordinates for the next circle
    x = turtle.xcor()
    x = turtle.ycor() - OFFSET

    # Calculate radius fpr the next circle
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
