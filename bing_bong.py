import turtle

wind = turtle.Screen()
wind.title("Ping Pong by Hassan")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# Score variables
score1 = 0
score2 = 0

# racket1
racket1 = turtle.Turtle()
racket1.speed(0)
racket1.shape("square")
racket1.shapesize(stretch_wid=5, stretch_len=1)
racket1.color("red")
racket1.penup()
racket1.goto(-350, 0)

# racket2
racket2 = turtle.Turtle()
racket2.speed(0)
racket2.shape("square")
racket2.shapesize(stretch_wid=5, stretch_len=1)
racket2.color("blue")
racket2.penup()
racket2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.penup()
score_display.hideturtle()
score_display.color("white")
score_display.goto(0, 260)
score_display.write("Player 1: 0  |  Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def update_score():
    score_display.clear()
    score_display.write(f"Player 1: {score1}  |  Player 2: {score2}", align="center", font=("Courier", 24, "normal"))

def reset_ball():
    ball.goto(0, 0)
    ball.dx *= -1  # send ball toward the player who just scored

def racket1_up():
    y = racket1.ycor()
    if y < 250:  # boundary limit so paddle doesn't go off screen
        racket1.sety(y + 20)

def racket1_down():
    y = racket1.ycor()
    if y > -250:
        racket1.sety(y - 20)

def racket2_up():
    y = racket2.ycor()
    if y < 250:
        racket2.sety(y + 20)

def racket2_down():
    y = racket2.ycor()
    if y > -250:
        racket2.sety(y - 20)

# Keyboard bindings
wind.listen()
wind.onkeypress(racket1_up, "w")
wind.onkeypress(racket1_down, "s")
wind.onkeypress(racket2_up, "Up")
wind.onkeypress(racket2_down, "Down")

# Main game loop
while True:
    wind.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ── Border checks (top / bottom) ──────────────────────────────
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # ── Scoring: ball passes left or right wall ───────────────────
    if ball.xcor() > 390:          # Player 1 missed → Player 2 scores
        score2 += 1
        update_score()
        reset_ball()

    elif ball.xcor() < -390:       # Player 2 missed → Player 1 scores
        score1 += 1
        update_score()
        reset_ball()

    # ── Paddle collisions ─────────────────────────────────────────
    # Right paddle (racket2)
    if (340 < ball.xcor() < 360) and (racket2.ycor() - 50 < ball.ycor() < racket2.ycor() + 50):
        ball.setx(339)
        ball.dx *= -1

    # Left paddle (racket1)
    if (-360 < ball.xcor() < -340) and (racket1.ycor() - 50 < ball.ycor() < racket1.ycor() + 50):
        ball.setx(-339)
        ball.dx *= -1