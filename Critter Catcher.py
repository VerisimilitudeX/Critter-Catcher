"""
LESSON: Critter Catcher Project
1. Prevent runtime error if 0 critters caught
2. Time limit gets smaller as you play
3. Print best reaction time
"""

#### ---- SET UP ---- ####

# --- Libraries --- #

# D1: Import the random library
import random
import sys
# A1: Import and initialize PYGAME
import pygame
pygame.init()

# --- Window --- #

# A2: Open a window with size 800 x 600
window = pygame.display.set_mode([800, 600])

# A3: Create a variable for whether the game is over
# with value False
game_over = False
best = 2500
# --- Time --- #

# C1: Create a CLOCK
c = pygame.time.Clock()

# C2: Create a variable for the reaction timer with
# value 2000
reaction_timer = 2000

# E1: Create variable for a wait timer with a random
# value between 750 and 1750
wait_timer = random.randint(750, 1750)

# H1: Create variable for the total reaction time with
# value 0
total_reaction_time = 0
time_limit = 3000

# --- Critter --- #

# D2: Create two variables for the x and y position of
# the critter. For the x position a random number
# between 50 and 750. For the y position a random
# number between 50 and 550.
critter_x = random.randint(50, 750)
critter_y = random.randint(50, 550)

# H2: Create a variable to track how many critters have
# been caught starting at 0
critters_caught = 0

#### ---- GAME LOOP ---- ####

# A4: Loop while the game is not over
while game_over != True:

    #### --- EVENT LOOP --- ####

    # A5: Create an EVENT LOOP that checks for the QUIT
    # event TYPE and sets game_over to True
    # ---> TEST AFTER THESE LINES <--- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    #### --- CALCULATE MOUSE --- ####

    # F1: If the wait timer is less than 0
    if wait_timer < 0:

        # --- Distance between mouse and critter --- #

        # F2: Get the position of the mouse and assign
        # it to x, y
        x, y = pygame.mouse.get_pos()
        # F3: Create variables for the difference in
        # horizontal distance and vertical distance
        # between the critter and the mouse
        difference_in_horizontal_distance = critter_x - x
        difference_in_vertical_distance = critter_y - y


        # --- Mouse is over critter --- #

        # F4: If the horizontal distance between the
        # critter and the mouse is less than 25 and
        # greater than -25
        if difference_in_horizontal_distance < 25 and difference_in_horizontal_distance > -25:

            # F5: If the vertical distance between the
            # critter and the mouse is less than 25 and
            # greater than -25
            if difference_in_vertical_distance < 25 and difference_in_vertical_distance > -25:

                # H3: Increment how many critters have
                # been caught by 1
                critters_caught += 1

                # F6: Create a variable for how long it
                # took to catch the critter. Assign it
                # the value
                # (2000 - reaction timer variable) / 1000
                time_took_to_catch_critter = (time_limit - reaction_timer) / 1000
                if time_took_to_catch_critter < best:
                    best = time_took_to_catch_critter
                # F7: Print the reaction time
                print("Reaction time: " + str(time_took_to_catch_critter))

                # H4: Remove or comment out F7

                # H5: Increment the total reaction time
                # by the currect reaction time
                total_reaction_time += time_took_to_catch_critter

                # F8: Set the game over variable to True
 
                # G1: Remove or comment out F8

                # --- Re-set for next round --- #

                # G2: Set the reaction timer to 2000
                # and set the wait timer to a new
                # random value between 750 and 1750
                reaction_timer = time_limit
                wait_timer = random.randint(750, 1750) 

                # G3: Get a new random x and y position
                # for the critter. Random x between
                # 50 and 750, and a Random y between
                # 50 and 550.
                # ---> TEST AFTER THESE LINES <--- #
                critter_x = random.randint(50, 750)
                critter_y = random.randint(50, 550)
                time_limit -= 100
                if time_limit < 500:
                    time_limit = 500
    #### --- DRAW --- ####

    # --- Draw background --- #

    # B1: Fill the window with color (100, 200, 250)
    window.fill((100, 200, 250))
    
    # B2: Create a rectangle for the ground at position
    # 0, 300 with width 800 and height 300. Then draw
    # it with color (150, 255, 150)
    ground = pygame.Rect(0, 300, 800, 300)
    pygame.draw.rect(window, (150, 255, 150), ground)

    # B3: Create a rectangle for the water at position
    # -200, 350, with width 1200 and height 500. Then
    # draw it as an ellipse with color (50, 50, 200)
    water = pygame.Rect(-200, 350, 1200, 500)
    pygame.draw.ellipse(window, (50, 50, 200), water)

    # --- Draw critter if it's time --- #

    # E2: If the wait timer is less than 0
    if wait_timer < 0:

    # D3: Draw the critter as a circle at the random
    # x and y position with the color of your choice
    # and a radius of 25
    # ---> TEST AFTER THIS LINE <--- #
        pygame.draw.circle(window, (113, 42, 121), (critter_x, critter_y), 25)

        # E3: Re-indent D3 above to be inside the block
        # of the E2 if-clause


    #### --- FINISH FRAME --- ####

    # C3: Tick the clock with framerate 60
    c.tick(60)

    # B4: Flip the display
    # ---> TEST AFTER THIS LINE <--- #
    pygame.display.flip()

    #### --- CALCULATE TIMES --- ####

    # --- Time passes --- #

    # E4: Decrement the wait timer by get_time
    wait_timer -= c.get_time()

    # E5: If the wait timer is less than 0
    if wait_timer < 0:

    # C4: Decrement the reaction timer by get_time
        reaction_timer -= c.get_time()

        # E6: Re-indent C4 above to be inside the block
        # of the E5 if-clause
        # ---> TEST AFTER THIS LINE <--- #


    # --- Stop when time runs out --- #

    # C5: If the reaction timer is less than 0, end the
    # game
    # ---> TEST AFTER THESE LINES <--- #
    if reaction_timer < 0:
        game_over = True
        # F9: Print a message that the critter escaped
        # ---> TEST AFTER THIS LINE <--- #
        print("The critter escaped! You lost. ")


#### ---- FINAL OUTPUT ---- ####

# H6: Print a blank line, "FINAL SCORE", and a line
# of dashes

print()
print("FINAL SCORE")
print("-----------------------------")

# H7: Print the total amount of critters caught and the
# average reaction time
# ---> TEST AFTER THESE LINES <--- #
if critters_caught == 0:
    sys.exit()
print("Total amount of critters caught: " + str(critters_caught) + "\nAverage reaction time: " + str(total_reaction_time / critters_caught) + " seconds \nBest time: " + str(best))

# Turn in your Coding Project.
