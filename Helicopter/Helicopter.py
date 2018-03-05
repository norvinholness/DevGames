import pygame

# Colors
black = (0,0,0)
white = (255,255,255)

# initiate Pygame
pygame.init()

# set display 800 wide x 400 long
surface = pygame.display.set_mode((800,400))
pygame.display.set_caption('Helicopter')
# set Clock for frame per second
clock = pygame.time.Clock()

def helicopter(x, y, image):
    # blit - draw one image onto another
    surface.blit(img, (x,y))

# Load Helicopter sprite
img = pygame.image.load('helicopter.png')
# Starting position of Helicopter
x = 150
y = 200

game_over = False
# Game Loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    
    surface.fill(black)
    helicopter(x,y,img)
            
    pygame.display.update()
    # 60 Frames Per Second
    clock.tick(60)

pygame.guit()
quit()
