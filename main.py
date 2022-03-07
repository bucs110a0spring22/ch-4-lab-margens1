import turtle
import math

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def drawSineCurve(turtle):
  for angle in range(-360, 360):
    y = math.sin(math.radians(angle))
    turtle.goto(angle,y)
    turtle.down()

def drawCosineCurve(turtle):
  turtle.down()
  turtle.up()
  for angle in range(-360, 360):
    y = math.cos(math.radians(angle))
    turtle.goto(angle,y)
    turtle.down()

def drawTangentCurve(turtle):
  turtle.down()
  turtle.up()
  for angle in range(-360, 360):
    y = math.tan(math.radians(angle))
    turtle.goto(angle,y)
    turtle.down()
  
def setupWindow(turtle):
  turtle.bgcolor("orange")
  turtle.setworldcoordinates(-360,-1.5,360,1.5)

def setupAxis(turtle):
  turtle.speed(10)
  turtle.goto(-360,0)
  turtle.goto(360,0)
  turtle.goto(0,0)
  turtle.goto(0,1.5)
  turtle.goto(0,-1.5)
  turtle.up()
  
##########  Do Not Alter Any Code Past Here ########
def main():

    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()

  
main()
