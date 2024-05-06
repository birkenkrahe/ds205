import turtle

def draw_spiral():
  screen = turtle.Screen()  # this is the screen
  screen.bgcolor("black")

  sp = turtle.Turtle() # this is the sprite
  sp.speed(0)
  sp.width(2)

  colors = ['red', 'magenta', 'blue', 'cyan', 'green', 'yellow', 'white']
  radius = 300 # spiral radius

  for i in range(360): # in the loop, cycle through colors, move forward and right
    sp.pencolor(colors[i % len(colors)])
    sp.forward(i * 3 / len(colors) + 1)
    sp.right(59)

  sp.hideturtle()
  turtle.done()

draw_spiral()  
