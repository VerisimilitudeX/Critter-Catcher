import pygame
pygame.init()
window = pygame.display.set_mode([100, 100])
c = pygame.time.Clock()
wait_timer = 1000
circle_timer = 2000
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    wait_timer -= c.get_time()
    if wait_timer < 0:
        circle_timer -= c.get_time()
    if circle_timer < 0:
        runing = False
    window.fill((255, 255, 255))
    if wait_timer < 0:
        pygame.draw.circle(window, (0, 0, 0), (50, 50), 10)
    c.tick(30)
    pygame.display.flip()
