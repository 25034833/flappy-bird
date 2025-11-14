import turtle
import random
import time

# Game setup
screen = turtle.Screen()
screen.title("Flappy Bird 🐦")
screen.bgcolor("skyblue")
screen.setup(width=800, height=600)
screen.tracer(0)

# Game variables
score = 0
game_over = False
gravity = -0.3
bird_velocity = 0
game_started = False
# Bird
bird = turtle.Turtle()
bird.speed(0)
bird.shape("circle")
bird.color("yellow")
bird.shapesize(1.5, 1.5)
bird.penup()
bird.goto(-200, 0)
# Pipes list
pipes = []

# Ground
ground = turtle.Turtle()
ground.speed(0)
ground.shape("square")
ground.color("brown")
ground.shapesize(stretch_wid=2, stretch_len=50)
ground.penup()
ground.goto(0, -280)

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 250)
score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))

# Game over display
game_over_display = turtle.Turtle()
game_over_display.speed(0)
game_over_display.color("red")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)

# Instructions
instructions = turtle.Turtle()
instructions.speed(0)
instructions.color("white")
instructions.penup()
instructions.hideturtle()
instructions.goto(0, 200)
instructions.write("Press SPACE to flap!", align="center", font=("Arial", 18, "normal"))
# Create pipe pair
def create_pipe():
    gap = 150
    height = random.randint(-150, 150)
    
    # Top pipe
    top_pipe = turtle.Turtle()
    top_pipe.speed(0)
    top_pipe.shape("square")
    top_pipe.color("green")
    top_pipe.shapesize(stretch_wid=15, stretch_len=3)
    top_pipe.penup()
    top_pipe.goto(400, height + gap + 150)
    
    # Bottom pipe
    bottom_pipe = turtle.Turtle()
    bottom_pipe.speed(0)
    bottom_pipe.shape("square")
    bottom_pipe.color("green")
    bottom_pipe.shapesize(stretch_wid=15, stretch_len=3)
    bottom_pipe.penup()
    bottom_pipe.goto(400, height - 150)
    
    pipes.append({
        'top': top_pipe,
        'bottom': bottom_pipe,
        'x': 400,
        'scored': False
    })
