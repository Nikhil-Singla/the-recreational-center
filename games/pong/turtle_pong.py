## import time

import turtle as t ## Game creation

from random import randint ## Importing for random start.


window = t.Screen() ## Main screen
window.title("Pong Practice") ## Title
window.bgcolor("black") 
window.setup(width=800, height=600)
window.tracer(0) ## Stops window from updating

def dec_global(): ## Declaration of global variables to be used later
    global scoreA
    scoreA = 0
    global scoreB
    scoreB = 0
    global swap_side
    swap_side = 1
    global gameState
    gameState = True

# Pen
pen = t.Turtle() ## Created to write the score
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 230)
pen.write("Player A: 0     Player B: 0", align = "center", font=("Comic-Sans", 24, "normal")) ## Initial Score

#A Bar
padA = t.Turtle() ## Create Turtle Item
padA.speed(0) ## Speed of the object
padA.shape("square")
padA.color("red")
padA.shapesize(stretch_wid=4, stretch_len=1) ## Multiple the dimensions to strech
padA.penup() ## Prevent drawing while the object is being moved
padA.goto(-375, 0) ## Move the object to this point at the start of the game.

#B Bar
padB = t.Turtle() 
padB.speed(0)
padB.shape("square")
padB.color("red")
padB.shapesize(stretch_wid=4, stretch_len=1)
padB.penup()
padB.goto(375, 0) ## Start object to the other side of Paddle A

#Ball
ball = t.Turtle() ## Ball Object
ball.speed(0)
ball.shape("circle") ## Different Ball Shape
ball.color("blue")
ball.penup() ## So that the ball doesn't trace path by drawing
ball.goto(0, 0)

def ball_start():
    global swap_side ## Randomize the side to which the ball begins
    a = randint(1,2)
    b = randint(1,2)
    ball.dx = 2.5*(swap_side if a%2==0 else swap_side*-1) ## !! Note separatation from the change in y
    ball.dy = 2.5*(swap_side if b%2==0 else swap_side*-1) 
    swap_side *= -1 ## Alternating swap_side value

#Function 
def padA_up():
    y = padA.ycor() ## Getting the y coordinate of turtle object
    if y >= 250: ## The paddle has center of 40 pixels and window size is 300 pixels either direction
        return
    y += 20 ## Add 20 pixels to y
    padA.sety(y) ## Sets the y coordinate to 20 above

def padA_down():
    y = padA.ycor() ## Getting the y coordinate of turtle object
    if y <= -250: ## The paddle has center of 40 pixels and window size is 300 pixels either direction
        return
    y -= 20 ## Removes 20 pixels to y
    padA.sety(y) ## Sets the y coordinate to 20 below

def padB_up():
    y = padB.ycor() ## Getting the y coordinate of turtle object
    if y >= 250: ## The paddle has center of 40 pixels and window size is 300 pixels either direction
        return
    y += 20 ## Add 20 pixels to y
    padB.sety(y) ## Sets the y coordinate to 20 below

def padB_down():
    y = padB.ycor() ## Getting the y coordinate of turtle object
    if y <= -250: ## The paddle has center of 40 pixels and window size is 300 pixels either direction
        return
    y -= 20 ## Removes 20 pixels to y
    padB.sety(y) ## Sets the y coordinate to 20 below

def ball_move():
    if ball.ycor() > 285: ## Boundary Check
        ball.sety(285) ## Ball Correction ## Note: Don't make the mistake of ".ycor =" and "sety()"
        ball.dy *= -1 ## Reverse Ball Speed
    if ball.ycor() < -285: ## Bottom Correction
        ball.sety(-285)
        ball.dy *= -1
    ball.setx(ball.xcor() + ball.dx) ## Ball's constant speed
    ball.sety(ball.ycor() + ball.dy) ## Ball's constant speed in y direction

def win_check():
    global scoreA 
    global scoreB ## Calling the predefined global variables to take prio this local

    if ball.xcor() > 385:
        ball.goto(randint(-50, 50), randint(-200, 200))
        ball_start()
        ball.dx *= -1
        pen.clear() 
        scoreA += 1 
        pen.write("Player A: {}     Player B: {}".format(scoreA, scoreB), align = "center", font=("Comic-Sans", 24, "normal"))
    if ball.xcor() < -385:
        ball.goto(randint(-50, 50), randint(-200, 200))
        ball_start()
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(scoreA, scoreB), align = "center", font=("Comic-Sans", 24, "normal"))

def check_col():
    if ((ball.xcor() > 350) and (ball.xcor() < 370) and (ball.ycor() > padB.ycor() - 60) and (ball.ycor() < padB.ycor()+60)): ## Tried using range function here, did not work out lol
        ball.dx *= -1
        ball.setx(ball.xcor() + ball.dx - 3)
    if ((ball.xcor() < -350) and (ball.xcor() > -370) and (ball.ycor() > padA.ycor() - 60) and (ball.ycor() < padA.ycor()+60)):
        ball.dx *= -1 ## Change the direction of ball
        ball.setx(ball.xcor() + ball.dx + 3)

##def Shoot():
  ##  bullet = t.Turtle()
  ##  x = padA.xcor()
  ##  x += 20
  ##  y = padA.ycor()
  ##  y += 20
  ##  bullet.speed(2)
  ##  bullet.shape("circle")
  ##  bullet.color("white")
  ##  bullet.penup()
  ##  bullet.goto(x,y)
## Will define this later when doing own update

def exit():
    global gameState ## For the exit loop. Needs to be declared before
    gameState = not gameState ## Change the game state
    return gameState ## Function return


#Keybinding
window.listen()
window.onkeypress(padA_up, "w") ## Left side Paddle UP
window.onkeypress(padA_down, "s") ## Left down
window.onkeypress(padB_up, "Up") ## Right Up
window.onkeypress(padB_down, "Down") ## Right down
window.onkeypress(exit, "Escape") ## Exit Menu

def game():
    if not gameState:
        return  # Stop the loop if gameState has been toggled off (e.g., Escape key pressed)
    
    window.update()       # Refresh the screen once per loop
    ball_move()           # Move the ball according to current dx/dy
    win_check()           # Check if a player scored, reset ball if so
    check_col()           # Handle paddle collision logic

    t.ontimer(game, 10)   # Re-schedule `game` to run again after 10ms
                          # Keeps the game loop running at ~100 FPS
                          # Crucially, we’re passing the *function object* `game`, not calling it immediately
                          # This prevents the runaway high-speed loop you were experiencing

def inc_speed():
    ball.dx *= 1.0005     # Gradually increase horizontal ball speed
    ball.dy *= 1.0005     # Gradually increase vertical ball speed

    if gameState:         # Continue scheduling speed-ups only if the game is running
        t.ontimer(inc_speed, 3000)  # Increase speed every 10 seconds (3000 ms) or (3s)


# Start the game and speed-up loop correctly with function references

dec_global()       # Declare global state variables
ball_start()       # Start ball with initial randomized direction
game()             # Kick off the main game loop
inc_speed()        # Start the periodic speed increment loop
window.mainloop()  # Let turtle take over the event loop (key events, updates, timers, etc.)
