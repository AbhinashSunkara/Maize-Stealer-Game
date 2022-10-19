#packages to import
import turtle
import time
import random
from tkinter import *

#Player color control window
root=Tk()
root.title("Control")
root.config(background="black")
root.geometry("250x250")

life=2
sc=0
hs=0

#Players Gifs registering
turtle.register_shape("pink.gif")
turtle.register_shape("pink1.gif")
turtle.register_shape("blue.gif")
turtle.register_shape("blue1.gif")
turtle.register_shape("red.gif")
turtle.register_shape("red1.gif")

#Game play window
s=turtle.Screen()
s.bgcolor("black")
s.bgpic("bgpic.gif")
s.title("Maize Stealer")
s.tracer(0)
s.setup(width=700,height=700)

k=turtle.Turtle()
k.color("white")
k.width(3)

#Player object
a=turtle.Turtle()
a.pensize(0)
a.color("orange")
a.shapesize(0.9,0.9,0.9)
a.shape("blue.gif")
a.direction="stop"
a.goto(0,0)
a.speed(0)
delay=0.01
a.penup()

def red():
    a.shape("red.gif")
def blue():
    a.shape("blue.gif")
def pink():
    a.shape("pink.gif")
def exit():
        turtle.Screen().bye()
        root.destroy()
def lock():
    a.goto(0,0)
    x=random.randint(-235,235)
    y=random.randint(-235,235)
    food.goto(x,y)
    
#buttons for player color     
Label(root,text="Select Player Color : ",bg="black",fg="white",font="verdana 12 bold italic").place(relx=0.5,rely=0.3,anchor=CENTER)

Button(root,text="red",command=red,bg="red",fg="black",font="verdana 12 bold").place(relx=0.2,rely=0.5,anchor=CENTER)

Button(root,text="blue",command=blue,bg="light blue",fg="black",font="verdana 12 bold").place(relx=0.5,rely=0.5,anchor=CENTER)

Button(root,text="pink",command=pink,bg="pink",fg="black",font="verdana 12 bold").place(relx=0.8,rely=0.5,anchor=CENTER)

Button(root,text="Exit",command=exit,bg="gold",fg="black",font="verdana 12 bold").place(relx=0.7,rely=0.7,anchor=CENTER)

Button(root,text="Lock!",command=lock,bg="white",fg="black",font="verdana 12 bold").place(relx=0.35,rely=0.7,anchor=CENTER)

#food object    
food=turtle.Turtle()
food.penup()
food.width(1)
shap=random.choice(["circle","square"])
food.pensize(0)
food.shape("circle")
food.shapesize(0.7,0.7,0.7)
food.color("gold")
food.penup()
food.goto(50,0)
food.penup()

#Score-Board object
score=turtle.Turtle()
score.penup()
score.speed(50)
score.color("gold")
score.pensize(0)
score.goto(0,300)
score.write("Score : 0 High Score : {} Life : {}".format(hs,life),align="center",font=("candra",16,"bold"))
score.hideturtle()
score.penup()

#Player direction control
def goup():
        a.direction="up"
def godown():
    
        a.direction="down"
def goright():
        a.direction="right"
def goleft():
    
        a.direction="left"
def stop():
    a.direction="stopp"

def move():
    if (a.direction=="down"):
        y=a.ycor()
        a.sety(y-5)
    if (a.direction=="up"):
        y=a.ycor()
        a.sety(y+5)
    if(a.direction=="stopp"):
        y=a.ycor()
        a.sety(y)
    
 
        
    if (a.direction=="right"):
        x=a.xcor()
        if(a.shape()=="red1.gif"):
            a.shape("red.gif")
        if(a.shape()=="blue1.gif"):
            a.shape("blue.gif")
        if(a.shape()=="pink1.gif"):
            a.shape("pink.gif")
        
        a.setx(x+5)
        
    if (a.direction=="left"):
        x=a.xcor()
        a.setx(x-5)
        if(a.shape()=="red.gif"):
            a.shape("red1.gif")
        if(a.shape()=="pink.gif"):
            a.shape("pink1.gif")
        if(a.shape()=="blue.gif"):
            a.shape("blue1.gif")
        
        a.left(180)
s.listen()

#keys using for player direction
s.onkeypress(goup,"Up")
s.onkeypress(godown,"Down")
s.onkeypress(goleft,"Left")
s.onkeypress(goright,"Right")
s.onkeypress(stop,"p")

#outline for game space and blocks in game
k.speed(500)
k.penup()
k.goto(-248,250)
k.penup()
k.width(5)
k.color("antiquewhite1")
for i in range(4):
    k.pendown()
    k.forward(493)
    k.right(90)
    k.penup()
k.penup()
k.goto(-210,210)
k.pendown()
k.forward(420)
k.penup()

k.goto(-210,-210)
k.pendown()
k.forward(420)
k.penup()


k.goto(-100,170)
k.pendown()
k.width(7)
k.color("red")
k.forward(210)
k.penup()

k.goto(-200,-120)
h=turtle.Turtle()
h.speed(100)
h.penup()
h.shapesize(3,3,3)
h.color("light blue")
h.shape("square")
h.goto(-160,-150)
h.penup()

l=turtle.Turtle()
l.speed(100)
l.penup()
l.shapesize(3,3,3)
l.color("light blue")
l.shape("square")
l.goto(180,-150)

p=turtle.Turtle()
p.speed(100)
p.penup()
p.shapesize(3,3,3)
p.color("light blue")
p.shape("square")
p.goto(180,140)

s.update()
o=turtle.Turtle()
o.speed(100)
o.penup()
o.color("light blue")
o.shape("square")
o.shapesize(3,3,3)
o.goto(-170,140)

s.update()

k.goto(-100,-180)
k.pendown()
k.color("red")
k.width(7)
k.forward(210)
k.penup()

k.goto(-160,60)
k.pendown()
k.width(7)
k.color("red")
k.right(90)
k.forward(140)
k.penup()

k.goto(160,60)
k.pendown()
k.width(7)
k.color("red")
k.forward(140)
k.penup()

k.hideturtle()
a.speed(0.5)

#Entire game logic
while True :
    s.update()
    
    if sc>50:
            delay=0.1
    if sc>150:
            a.speed(8)
    a.speed(0.6)
    if a.xcor()>230 or a.xcor()<-230 or a.ycor()>230 or a.ycor()<-230 :
        time.sleep(1)
        a.speed(10)
        a.goto(0,0)
        a.direction="stop"
        delay=0.001
        life=life-1
        score.clear()
        food.goto(50,0)
        
        score.write("Score : {} High Score : {} Life: {} ".format(sc,hs,life),align="center",font=("candra",16,"bold"))
    
        if(life<=0):
            life=2
            score.clear()
            food.goto(50,0)
            sc=0
            score.write("Score : 0 High Score : {} Life: {} ".format(hs,life),align="center",font=("candra",16,"bold"))
        
    if  (a.ycor()>190 and a.ycor()<230 and a.xcor()>-220 and a.xcor()<220):
        if a.direction=="down":
                a.direction="stop"
        if a.direction=="up" :
                a.direction="stop"
                
    if (a.ycor()>=205 and a.ycor()<=215 and a.xcor()<-210 and a.xcor()>-230):
        if a.direction=="right":
            a.direction="stop"
            
    if (a.ycor()>=205 and a.ycor()<=215 and a.xcor()>210 and a.xcor()<230):
        if a.direction=="left":
            a.direction="stop"
        delay=0.01
        
    if(a.ycor()>=55 and a.xcor()>=165 and a.ycor()<=65 and a.xcor()<=170 ):
            if a.direction=="down":
                a.direction="stop"
                
    if (a.ycor()>=150 and a.ycor()<=180 and a.xcor()>-110 and a.xcor()<125):
        if a.direction=="down":
                a.direction="stop"
        if a.direction=="up" :
                a.direction="stop"
    if (a.ycor()<=-170 and a.ycor()>=-190 and a.xcor()>-110 and a.xcor()<125):
        if a.direction=="down":
                a.direction="stop"
        if a.direction=="up" :
                a.direction="stop"
                
    if(a.ycor()>=160 and a.ycor()<=180 and a.xcor()>110 and a.xcor()<130):
        if a.direction=="left":
            a.direction="stop"
            
    if(a.ycor()>=160 and a.ycor()<=180 and a.xcor()<-100 and a.xcor()>-120):
        if a.direction=="right":
            a.direction="stop"
            
    if(a.ycor()<=-170 and a.ycor()>=-190 and a.xcor()>110 and a.xcor()<130):
        if a.direction=="left":
            a.direction="stop"
            
    if(a.ycor()<=-170 and a.ycor()>=-190 and a.xcor()<-100 and a.xcor()>-120):
        if a.direction=="right":
            a.direction="stop"
            
    if  (a.ycor()<-190 and a.ycor()>-230 and a.xcor()>-220 and a.xcor()<210):
        if a.direction=="down":
                a.direction="stop"
        if a.direction=="up" :
                a.direction="stop"
                
    if  (a.ycor()<-205 and a.ycor()>-215 and a.xcor()<-200 and a.xcor()>-230):
        if a.direction=="right":
            a.direction="stop"
            
    if  (a.ycor()<-200 and a.ycor()>-220 and a.xcor()>210 and a.xcor()<230):
        if a.direction=="left":
            a.direction="stop"
        delay=0.01
        
    if (a.ycor()>=-190 and a.ycor()<=-160 and a.xcor()>-100 and a.xcor()<120):
        if a.direction=="down":
                a.direction="stop"
        if a.direction=="up" :
                a.direction="stop"
                
    if (a.ycor()>=-90 and a.ycor()<=70 and a.xcor()<-140 and a.xcor()>-175):
        if a.direction=="left":
                a.direction="stop"
        if a.direction=="right" :
                a.direction="stop"
                
    if (a.ycor()<=-80 and a.ycor()>=-90 and a.xcor()<-150 and a.xcor()>-175):
        if a.direction=="up":
            a.direction="stop"
            
    if (a.ycor()>60 and a.ycor()<=70 and a.xcor()<-150 and a.xcor()>-175):
        if a.direction=="down":
            a.direction="stop"
            
    if (a.ycor()>=-90 and a.ycor()<=70 and a.xcor()>140 and a.xcor()<175):
        if a.direction=="left":
                a.direction="stop"
        if a.direction=="right" :
                a.direction="stop"
                
    if (a.ycor()<=-80 and a.ycor()>=-90 and a.xcor()>150 and a.xcor()<175):
       if a.direction=="up":
            a.direction="stop"
            
    if (a.ycor()>60 and a.ycor()<=70 and a.xcor()>150 and a.xcor()<175):
       if a.direction=="down":
            a.direction="stop"
            
    if (a.distance(l)<=42):
            if a.direction=="right":
                    a.direction="stop"
                    x=a.xcor()
                    a.setx(x-8)
                    s.listen()
                    
                    move()
                    time.sleep(0.097)
                    a.speed(0.5)
            if a.direction=="left":
                    a.direction="stop"
                    x=a.xcor()
                    a.setx(x+8)
                    s.listen()
                    move()
                    time.sleep(0.097)
                    a.speed(0.5)
            if a.direction=="down":
                    a.direction="stop"
                    y=a.ycor()
                    a.sety(y+8)
                    s.listen()
                    move()
                    time.sleep(0.097)
                    a.speed(0.5)
            if a.direction=="up":
                    a.direction="stop"
                    y=a.ycor()
                    a.sety(y-8)
                    s.listen()
                    move()
                    a.speed(0.5)
                    time.sleep(0.097)
                    
    if (a.distance(p)<=42):
            if a.direction=="right":
                    a.direction="stop"
                    x=a.xcor()
                    a.setx(x-8)
                    s.listen()
                    move()
                    a.speed(0.5)
                    time.sleep(0.097)
            if a.direction=="left":
                    a.direction="stop"
                    x=a.xcor()
                    a.setx(x+8)
                    s.listen()
                    move()
                    a.speed(0.5)
                    time.sleep(0.097)
            if a.direction=="down":
                    a.direction="stop"
                    y=a.ycor()
                    a.sety(y+8)
                    s.listen()
                    move()
                    a.speed(0.5)
                    time.sleep(0.097)
            if a.direction=="up":
                    a.direction="stop"
                    y=a.ycor()
                    a.sety(y-8)
                    s.listen()
                    move()
                    a.speed(0.5)
                    time.sleep(0.097)
                    
    if (a.distance(h)<=42):
            if a.direction=="right":
                    a.direction="stop"
                    x=a.xcor()
                    a.setx(x-8)
                    s.listen()
                    move()
                    a.speed(0.5)
                    time.sleep(0.097)
            if a.direction=="left":
                    a.direction="stop"
                    x=a.xcor()
                    a.setx(x+8)
                    s.listen()
                    move()
                    a.speed(0.5)
                    time.sleep(0.097)
            if a.direction=="down":
                    a.direction="stop"
                    y=a.ycor()
                    a.sety(y+8)
                    s.listen()
                    move()
                    a.speed(0.5)
                    time.sleep(0.097)
            if a.direction=="up":
                    a.direction="stop"
                    y=a.ycor()
                    a.sety(y-8)
                    s.listen()
                    move()
                    a.speed(0.5)
                    time.sleep(0.097)
    if ((food).distance(o)<20):
        x=random.randint(-235,235)
        y=random.randint(-235,235)
        food.goto(x,y)
    if (food).distance(h)<20:
        x=random.randint(-235,235)
        y=random.randint(-235,235)
        food.goto(x,y)
    if (food).distance(p)<20:
        x=random.randint(-235,235)
        y=random.randint(-235,235)
        food.goto(x,y)
    if (food).distance(l)<20:
        x=random.randint(-235,235)
        y=random.randint(-235,235)
        food.goto(x,y)
    if a.distance(food)<20:
        
        x=random.randint(-235,235)
                    
    if (a.distance(o)<=42):
            if a.direction=="right":
                    a.direction="stop"
                    x=a.xcor()
                    a.setx(x-8)
                    s.listen()
                    move()
                    a.speed(0.5)
                    time.sleep(0.097)
            if a.direction=="left":
                    a.direction="stop"
                    x=a.xcor()
                    a.setx(x+8)
                    s.listen()
                    move()
                    a.speed(0.5)
                    time.sleep(0.097)
            if a.direction=="down":
                    a.direction="stop"
                    y=a.ycor()
                    a.sety(y+8)
                    s.listen()
                    move()
                    a.speed(0.5)
                    time.sleep(0.097)
            if a.direction=="up":
                    a.direction="stop"
                    y=a.ycor()
                    a.sety(y-8)
                    s.listen()
                    move()
                    a.speed(0.5)
                    time.sleep(0.097)
            
    if a.distance(food)<15:
        x=random.randint(-235,235)
        y=random.randint(-235,235)
        food.speed(50)
        if(x>=200 and x<=205):
                x=random.randint(-150,150)
                y=random.randint(-150,150)
        
        if(x>=-100 and x<=110):
                x=random.randint(-100,100)
                y=random.randint(-100,100)
        if(y>=-180 and y<=-170):
                x=random.randint(-100,100)
                y=random.randint(-100,100)
        if(y==205):
                x=random.randint(-100,100)
                y=random.randint(-100,100)
        if(y==-205):
                x=random.randint(-100,100)
                y=random.randint(-100,100)
        if(x<-180 and x>-120):
                x=random.randint(-200,200)
                y=random.randint(-200,200)
        if(x<200 and x>140):
                x=random.randint(-200,200)
                y=random.randint(-200,200)
        if(y>-180 and y<-120):
                x=random.randint(-200,200)
                y=random.randint(-200,200)
        if(y>120 and y<180):
                x=random.randint(-200,200)
                y=random.randint(-200,200)
        if(y>=205 and y<=220 and x>-200 and x<200):
                x=random.randint(-200,200)
                y=random.randint(-200,200)
        if  (y<=-205 and y>=-210 and x>-200 and x<200):
                x=random.randint(-200,200)
                y=random.randint(-200,200)

        food.goto(x,y)
        sc+=10
        
        if (sc>hs):
            hs=sc
        score.clear()
        score.write("Score : {} High Score : {} Life : {}".format(sc,hs,life),align="center",font=("candra",16,"bold"))
        
        delay=0.01
        
    move()
    if(sc<50):
            
            time.sleep(0.097)
    if(sc>=50 and sc<150):
            time.sleep(0.05)
    if(sc>=150):
            time.sleep(0.025)
    
    
turtle.done()
