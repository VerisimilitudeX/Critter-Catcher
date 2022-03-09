#### ---- SET UP ---- ####

# --- Libraries --- #
import random
import pygame
pygame.init()

# --- Window --- #
window = pygame.display.set_mode([800, 600])
game_over = False

# --- Time --- #
c = pygame.time.Clock()
reaction_timer = 2000
wait_timer = random.randint(750, 1750)
total_reaction_time = 0

# --- Critter --- #
critter_x = random.randint(50, 750)
critter_y = random.randint(50, 550)
critters_caught = 0

#### ---- GAME LOOP ---- ####
while game_over != True:

    #### --- EVENT LOOP --- ####
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    #### --- CALCULATE MOUSE --- ####
    if wait_timer < 0:
        x, y = pygame.mouse.get_pos()
        difference_in_horizontal_distance = critter_x - x
        difference_in_vertical_distance = critter_y - y

        # --- Mouse is over critter --- #
        if difference_in_horizontal_distance < 25 and difference_in_horizontal_distance > -25:
            if difference_in_vertical_distance < 25 and difference_in_vertical_distance > -25:
                critters_caught += 1
                time_took_to_catch_critter = (2000 - reaction_timer) / 1000
                print("Reaction time: " + str(time_took_to_catch_critter))
                total_reaction_time += time_took_to_catch_critter
                reaction_timer = 2000
                wait_timer = random.randint(750, 1750) 
                critter_x = random.randint(50, 750)
                critter_y = random.randint(50, 550)

    #### --- DRAW --- ####

    # --- Draw background --- #
    window.fill((100, 200, 250))
    ground = pygame.Rect(0, 300, 800, 300)
    pygame.draw.rect(window, (150, 255, 150), ground)
    water = pygame.Rect(-200, 350, 1200, 500)
    pygame.draw.ellipse(window, (50, 50, 200), water)

    # --- Draw critter if it's time --- #
    if wait_timer < 0:
        pygame.draw.circle(window, (113, 42, 121), (critter_x, critter_y), 25)

    #### --- FINISH FRAME --- ####
    c.tick(60)
    pygame.display.flip()

    #### --- CALCULATE TIMES --- ####

    # --- Time passes --- #
    wait_timer -= c.get_time()
    if wait_timer < 0:
        reaction_timer -= c.get_time()
    if reaction_timer < 0:
        game_over = True
        print("The critter escaped! You lost. ")

#### ---- FINAL OUTPUT ---- ####
print()
print("FINAL SCORE")
print("-----------------------------")
print("Total amount of critters caught: " + str(critters_caught) + "\nAverage reaction time: " + str(total_reaction_time / 1000))
'''
fortnite
'''
