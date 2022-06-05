import turtle as tx

#window
wn = tx.Screen()
wn.title("PongGame")
wn.bgcolor("white")
wn.setup(width=900, height=700)
wn.tracer(0)


#Paddle A
pad_a = tx.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("yellow")
pad_a.shapesize(stretch_wid=6, stretch_len=0.6)
pad_a.penup()
pad_a.goto(-370, 0)

#Paddle B
pad_b = tx.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("green")
pad_b.shapesize(stretch_wid=6, stretch_len=0.6)
pad_b.penup()
pad_b.goto(370, 0)



#ball
ball = tx.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

#Scoreboard
score_a = 0
score_b = 0

pen = tx.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 280)
pen.write("Player A: {} |   Player B: {}".format(score_a, score_b), align= "center", font=("Verdana", 16, "bold"))


#Function
def pad_a_up():
    y = pad_a.ycor()
    y+=20
    pad_a.sety(y)
def pad_a_down():
    y = pad_a.ycor()
    y-=20
    pad_a.sety(y)
def pad_b_up():
    y = pad_b.ycor()
    y+=20
    pad_b.sety(y)
def pad_b_down():
    y = pad_b.ycor()
    y-=20
    pad_b.sety(y)



#Keyboards

wn.listen()
wn.onkeypress(pad_a_up, "w")
wn.onkeypress(pad_a_down, "s")
wn.onkeypress(pad_b_up, "Up")
wn.onkeypress(pad_b_down, "Down")


while True:
    wn.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Collision
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor()<-390:
        score_b += 1
        pen.clear()
        pen.write("Player A: {} |   Player B: {}".format(score_a, score_b), align="center", font=("Verdana", 16, "bold"))
        ball.goto(0 , 0)
        ball.dx *= -1
    if ball.xcor()>390:
        score_a+= 1
        pen.clear()
        pen.write("Player A: {} |   Player B: {}".format(score_a, score_b), align= "center", font=("Verdana", 16, "bold"))
        ball.goto(0, 0)
        ball.dx *= -1

    #Paddle Collision
    if ball.xcor()<-340 and ball.xcor()>-350 and ball.ycor()>pad_a.ycor()-50 and ball.ycor()<pad_a.ycor()+50:
        ball.setx(-340)
        ball.dx *= -1
    if ball.xcor() >340 and ball.xcor() <350 and ball.ycor() > pad_b.ycor() - 50 and ball.ycor() < pad_b.ycor() + 50:
        ball.setx(340)
        ball.dx *= -1




