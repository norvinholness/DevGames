import pygame

# Colors
black = (0,0,0)
white = (255,255,255)

# Initiate Pygame
pygame.init()

# Set display 800 wide x 400 long
surface = pygame.display.set_mode((800,400))
pygame.display.set_caption('Helicopter')
# Set Clock for frame per second
clock = pygame.time.Clock()

# Load Helicopter sprite
img = pygame.image.load('helicopter.png')
# Starting position of Helicopter
x = 150
y = 200

y_move = 5

def helicopter(x, y, image):
    # blit - draw one image onto another
    surface.blit(img, (x,y))

game_over = False
# Game Loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Set User Events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_move = -5 # -5 Move Up in Y Direction
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_move = 5  # 5 Move Down in Y Direction

    y += y_move
    
    surface.fill(black)
    helicopter(x,y,img)
            
    pygame.display.update()
    # 60 Frames Per Second
    clock.tick(60)

pygame.guit()
quit()
