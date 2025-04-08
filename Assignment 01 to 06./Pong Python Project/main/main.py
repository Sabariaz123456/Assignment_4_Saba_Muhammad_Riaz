import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Disable automatic screen updates for smoother animation

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)  # Make the paddle longer
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)  # Make the paddle longer
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = -0.15

# Paddle movement functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
        paddle_b.sety(y)

# Keyboard bindings
screen.listen()
screen.onkey(paddle_a_up, "w")
screen.onkey(paddle_a_down, "s")
screen.onkey(paddle_b_up, "Up")
screen.onkey(paddle_b_down, "Down")

# Score variables
score_a = 0
score_b = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball collision with top and bottom walls
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reflect the ball

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # Reflect the ball

    # Ball collision with paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.color("blue")
        ball.setx(340)
        ball.dx *= -1  # Reflect the ball

    elif (ball.xcor() < -340 and ball.xcor() > -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.color("red")
        ball.setx(-340)
        ball.dx *= -1  # Reflect the ball

    # Ball out of bounds (Player A or Player B scores)
    if ball.xcor() > 390:
        score_a += 1
        score_display.clear()
        score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -390:
        score_b += 1
        score_display.clear()
        score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
