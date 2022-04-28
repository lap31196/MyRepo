import turtle as t
import time 

wn = t.Screen()
wn.title("Pong by laandrad")
wn.bgcolor("black")
wn.setup(width =800, height=600)
wn.tracer(0)

#Paddle A
paddle_a=t.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=8,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B

paddle_b=t.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=8,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball

ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1/6
ball.dy = 1/6

#Function
#Testing commit

def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -=20
    paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#Score
score_a =0
score_b =0

#Pen
pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))



#Main game loop
a = True
while (a):
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if (ball.ycor() > 290):
        ball.sety(290)
        ball.dy *= -1

    if (ball.ycor() < -290):
            ball.sety(-290)
            ball.dy *= -1

    if(ball.xcor() > 390):
        ball.goto(0,0)
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
        ball.dx *=-1

    if(ball.xcor() < -390):
        ball.goto(0,0)
        score_b +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
        ball.dx *=-1

    #Paddle cheching
    if((ball.xcor() > 340 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor() +50 and ball.ycor() > paddle_b.ycor()-50)):
        ball.setx(340)
        ball.dx *=-1
    
    if((ball.xcor() < -340 and ball.xcor() >- 350) and (ball.ycor() < paddle_a.ycor() +50 and ball.ycor() > paddle_a.ycor()-50)):
        ball.setx(-340)
        ball.dx *=-1

    #Ending the loop
    if (score_a ==5):
        msg = t.Turtle()
        wn.clear()
        wn.bgcolor("black")

        msg.speed(0)
        msg.color("white")
        msg.penup()
        msg.hideturtle()
        msg.goto(0,0)
        msg.write("Player A: WINS!!!! \n"+ 
                  "Player B fucking SUCKS!!! \n",align="center",font=("Courier",24,"normal"))
        time.sleep(3)
        a=False

    if (score_b ==5):
        msg = t.Turtle()
        wn.clear()
        wn.bgcolor("black")

        msg.speed(0)
        msg.color("white")
        msg.penup()
        msg.hideturtle()
        msg.goto(0,0)
        msg.write("Player B: WINS!!!! \n"+ 
                  "Player A fucking SUCKS!!! \n",align="center",font=("Courier",24,"normal"))
        time.sleep(3)
        a=False
   