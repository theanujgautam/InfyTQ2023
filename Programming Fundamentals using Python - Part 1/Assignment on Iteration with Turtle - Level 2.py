import turtle
wn = turtle.Screen()    # creates a graphics window
wn.setup(500,500)       # set window dimension

alex = turtle.Turtle()  # create a turtle named alex
alex.shape("turtle")    # alex looks like a turtle
radius = 50
'''
alex.color("black")    # alex has a color
alex.right(60)         # alex turns 60 degrees right
alex.left(60)          # alex turns 60 degrees left
alex.circle(50)        # draws a circle of radius 50
#draws circles
for counter in range(1,3):
    alex.circle(20*counter)
'''

#Write the logic to create the given pattern
#Refer the statements given above to draw the pattern

for i in range(4):
    alex.color('Green')
    alex.circle(radius)
    radius -= 10
radius += 10
alex.right(120)
for i in range(4):
    alex.color('Blue')
    alex.circle(radius)
    radius += 10

radius -= 10
alex.left(240)
for i in range(4):
    alex.color('Red')
    alex.circle(radius)
    radius -= 10