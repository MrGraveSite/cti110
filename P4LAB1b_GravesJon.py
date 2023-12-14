#We will be using turtle graphics to draw my initials.
#CTI-110
#P4LAB1b
#Jon Graves
#11/8/2023
#

#This will create a turtle window and attributes
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("My intials")

#Creating a turtle, assigning it to jg
jg = turtle.Turtle()
jg.color("blue")
jg.pensize(3)

#Sequence of actions that create the J
jg.right(90)
jg.forward(25)
jg.left(90)
jg.forward(50)
jg.left(90)
jg.forward(100)
jg.left(90)
jg.forward(50)
jg.right(180)
jg.forward(100)

#Picks up the pen and drops it in a new location
jg.penup()
jg.forward(125)
jg.pendown()

#Sequence of actions that create the G
jg.left(180)
jg.forward(75)
jg.left(90)
jg.forward(100)
jg.left(90)
jg.forward(75)
jg.left(90)
jg.forward(50)
jg.left(90)
jg.forward(40)
jg.penup()

#Wait for user to close window  
wn.mainloop()
