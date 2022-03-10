# Libraries
import pygame
pygame.init()

# Variables
w = pygame.display.set_mode([300, 300])
w.fill((255, 255, 255))
c = pygame.time.Clock()

# Main loop
running = True
while running:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if  pygame.time.get_ticks() % 1000:
        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(w, (23, 234, 127), (x, y), 5)
        pygame.display.flip()
    c.tick(60)
