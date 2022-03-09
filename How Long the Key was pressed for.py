# Libraries
import pygame
pygame.init()

# Window
w = pygame.display.set_mode([100, 100])
w.fill((255, 255, 255))
pygame.display.flip()

# Variables
c = pygame.time.Clock()
down_time = 0
up_time = 0

# Main loop
running = True
last_time = 0
while running:

    # Event loop
    for event in pygame.event.get():

        # Quit event
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print("Key down! ")
            time_start = pygame.time.get_ticks()
        if event.type == pygame.KEYUP:
            print("Key up! ")
            frame_time = ((time_start - c.get_time()) / 1000) - last_time
            print(frame_time)
            last_time = frame_time
    c.tick(30)
