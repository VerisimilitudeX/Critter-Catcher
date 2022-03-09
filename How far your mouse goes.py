import pygame
pygame.init()

window = pygame.display.set_mode([300, 300])
window.fill((255, 255, 255))
pygame.display.flip()

last_x = 0
last_y = 0

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            difference_x = x - last_x
            difference_y = y - last_y

            print("Difference in x " + str(difference_x))
            print("Difference in y " + str(difference_y))            

            last_x = x
            last_y = y
