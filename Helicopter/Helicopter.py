import pygame 

# initiat Pygame
pygame.init()

# set display
surface = pygame.display.set_mode((800,400))

pygame.display.set_caption('Helicopter')

# set Clock for frame per second
clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
    pygame.display.update()
    # 60 Frames Per Second
    clock.tick(60)

pygame.guit()
quit()
