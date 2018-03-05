import pygame

# Colors
black = (0,0,0)
white = (255,255,255)

# Initiate Pygame
pygame.init()

surfaceWidth = 800
surfaceHeight = 500

# Set display 800 wide x 400 long
surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption('Helicopter')
# Set Clock for frame per second
clock = pygame.time.Clock()

# Load Helicopter sprite
img = pygame.image.load('helicopter.png')

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        return event.key
    return None

def makeTextObjs (text, font):
    textSurface =  font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def msgSurface(text):
    smallText  = pygame.font.Font('freesansbold.ttf',20)
    largeText  = pygame.font.Font('freesansbold.ttf',150)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    # Center
    titleTextRect.center = surfaceWidth/2, surfaceHeight/2
    surface.blit(titleTextSurf,titleTextRect)

    typeTextSurf, typeTextRect = makeTextObjs('Press any key to continue', smallText)
    titleTextRect.center = surfaceWidth/2, ((surfaceHeight/2) + 100 )
    surface.blit(typeTextSurf, typeTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()

    main()

def gameOver():
    msgSurface('Kaboom!')

def helicopter(x, y, image):
    # blit - draw one image onto another
    surface.blit(img, (x,y))

def main():
    # Starting position of Helicopter
    x = 150
    y = 200
    y_move = 5
    
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

        # If Helicopter touches Lower or Upward Boundary
        # Game Over 
        if y > surfaceHeight - 40 or y < 0:
            gameOver()
                
        pygame.display.update()
        # 60 Frames Per Second
        clock.tick(60)

# Start
main()
pygame.guit()
quit()
