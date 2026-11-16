import turtle
import random
b = turtle.Turtle()
turtle.colormode(255)
#turtle.tracer(0)
b.speed(0)




def jump(x,y):
    b.penup()
    b.goto(x,y)
    b.pendown()



def polygon(dist, sides, fcolour):
    b.fillcolor(fcolour)
    angle = 360/sides
    b.begin_fill()
    for times in range(sides):
        b.fd(dist)
        b.left(angle)
    b.end_fill()

def rectangle(dist, odist, color):
    b.fillcolor(color)
    b.begin_fill()
    b.fd(dist)
    b.left(90)
    b.fd(odist)
    b.left(90)
    b.fd(dist)
    b.left(90)
    b.fd(odist)
    b.end_fill()
    
def brectangle(color):
    b.setheading(0)
    b.left(40)
    rectangle(4000,100,color)


def background(color):
    b.penup()
    b.home()
    b.setheading(0)
    b.pendown()
    for times in range(15):
        b.penup()      
        b.home()
        b.setheading(0)
        b.left(90)
        b.fd(800)
        b.left(90)
        b.fd(1000)
        b.setheading(270)
        b.fd(3000 - (times * 200))
        brectangle(color)

def eye(rad):
    b.fillcolor((0,0,0))
    b.begin_fill()
    b.circle(rad)
    b.end_fill()

def smiless(color):
    b.setheading(270)
    b.fillcolor(color)
    b.begin_fill()
    b.circle(300,180)
    b.end_fill()

def smilesss(color):
    b.setheading(270)
    b.fillcolor(color)
    b.begin_fill()
    b.circle(280,180)
    b.end_fill()
    
def smiles():
    smiless((0,0,0))
    b.setheading(0)
    
    b.bk(580)

    smilesss('yellow')

def ycircle():
    b.fillcolor('yellow')
    b.begin_fill()
    b.circle(400)
    b.end_fill()

def face(disteye):
    b.penup()
    b.color('black')
    b.home()
    b.pendown()
    b.setheading(0)
    b.penup()
    b.bk(300)
    b.right(90)
    b.fd(70)
    b.pendown()
    ycircle()
    b.penup()
    b.home()
    b.bk(200)
    b.setheading(270)
    b.fd(80)
    b.setheading(0)
    b.pendown()
    smiles()
    b.setheading(90)
    b.penup()
    b.fd(100)
    b.pendown()
    eye(disteye)
    b.setheading(180)
    b.penup()
    b.fd(450)
    b.pendown()
    b.setheading(90)
    eye(disteye)

def rcircles(s):
    for times in range(s):
        x = random.randint(-1000,1000)
        y = random.randint(-1000,1000)
        c = random.randint(0,255)
        cs = random.randint(0,255)
        cd = random.randint(0,255)
        b.fillcolor((c,cs,cd))
        b.begin_fill()
        jump(x,y)
        b.circle(15)
        b.end_fill()
        
def wall():
    jump(-930,510)
    b.seth(180)
    polygon(1010,4,'black')
    jump(-930,510)
    for times in range(35):
        b.seth(270)
        b.fillcolor('black')
        b.begin_fill()
        for tims in range(3):
            b.fd(30)
            b.left(120)
        b.end_fill()
        b.seth(270)
        b.fd(30)

def wallo():
    jump(930,-500)
    b.seth(0)
    polygon(1010,4,'black')
    jump(930,510)
    for times in range(35):
        b.seth(90)
        b.fillcolor('black')
        b.begin_fill()
        for tims in range(3):
            b.fd(30)
            b.left(120)
        b.end_fill()
        b.seth(270)
        b.fd(30)

