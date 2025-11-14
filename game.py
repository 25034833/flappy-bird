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
# Bird flap
def flap():
    global bird_velocity, game_started
    if not game_over:
        bird_velocity = 5
        game_started = True
# Reset game
def restart_game():
    global score, game_over, bird_velocity, pipes, loop_count, game_started
    
    # Reset variables
    score = 0
    game_over = False
    bird_velocity = 0
    loop_count = 0
    game_started = False
    
    # Reset bird position
    bird.goto(-200, 0)
    
    # Clear all pipes
    for pipe in pipes:
        pipe['top'].hideturtle()
        pipe['bottom'].hideturtle()
    pipes.clear()
    
    # Create initial pipe
    create_pipe()
    
    # Clear displays
    game_over_display.clear()
    instructions.clear()
    instructions.goto(0, 200)
    instructions.write("Press SPACE to flap!", align="center", font=("Arial", 18, "normal"))
    
    # Reset score display
    update_score()
# Collision detection
def check_collision():
    # Check ground and ceiling
    if bird.ycor() > 270 or bird.ycor() < -250:
        return True
    
    # Check pipes
    for pipe in pipes:
        pipe_x = pipe['x']
        if -220 < pipe_x < -180:
            top_y = pipe['top'].ycor()
            bottom_y = pipe['bottom'].ycor()
            bird_y = bird.ycor()
            
            # Check if bird hits pipe
            if bird_y > top_y - 135 or bird_y < bottom_y + 135:
                return True
    
    return False
# Update score
def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))

# Keyboard binding
screen.listen()
screen.onkey(flap, "space")
screen.onkey(restart_game, "r")

# Create initial pipes
create_pipe()

# Game loop counter
loop_count = 0
# Main game loop
while True:
    screen.update()
    time.sleep(0.02)
    
    if not game_started:
        continue
    
    if game_over:
        continue
    
    loop_count += 1
    
    # Apply gravity
    bird_velocity += gravity
    bird.sety(bird.ycor() + bird_velocity)
    
    # Move pipes
    for pipe in pipes:
        pipe['x'] -= 3
        pipe['top'].setx(pipe['x'])
        pipe['bottom'].setx(pipe['x'])
        
        # Score when passing pipe
        if pipe['x'] < -200 and not pipe['scored']:
            pipe['scored'] = True
            score += 1
            update_score()
    
    # Remove off-screen pipes
    if pipes and pipes[0]['x'] < -450:
        pipes[0]['top'].hideturtle()
        pipes[0]['bottom'].hideturtle()
        pipes.pop(0)
    
    # Create new pipes
    if loop_count % 90 == 0:
        create_pipe()
    
    # Check collision
    if check_collision():
        game_over = True
        instructions.clear()
        game_over_display.write(
            f"GAME OVER!\n\nFinal Score: {score}\n\nPress 'R' to Restart",
            align="center", font=("Arial", 28, "bold")
        )
