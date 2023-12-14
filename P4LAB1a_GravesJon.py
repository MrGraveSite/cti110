#We will be using turtle graphics and while or for loops to command it to draw two different shapes.
#CTI-110
#P4LAB1a
#Jon Graves
#11/8/2023
#

#This will create a turtle window and attributes
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hello, JJ & CC!")

#Creating a turtle, assigning it to jj
jj = turtle.Turtle()
jj.color("blue")
jj.pensize(3)

#Creating another turtle, assigning it to cc
cc = turtle.Turtle()
cc.color("hotpink")
cc.pensize(2)

#Excutes the same actions 4 times for jj
for i in range(4):
    jj.forward(50)
    jj.left(90)

#Seperate 1 time actions
jj.left(180)
jj.forward(50)

#Excutes the same actions 3 times for cc
for i in range(3):
    cc.forward(50)
    cc.left(120)

#Wait for user to close window  
wn.mainloop()
