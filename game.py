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
