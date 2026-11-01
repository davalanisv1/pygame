'''This weeks theme is: ANTIQUE!!

Make something with just a terminal , an 8-bit game, or anything else that makes you think "wow this is really old"'''

import pygame
pygame.init() #initializes pygame

screen = pygame.display.set_mode([600, 600]) #defines size of the screen

#Defines basic colors
red = (255, 0, 0)
darkred = (80, 0, 0)
green = (0, 255, 0)
darkgreen = (0, 99, 15)
blue = (0, 0, 255)
white = (255,255,255)
black = (0,0,0)
darktint = pygame.Surface((600, 600))
darktint.fill((0,0,0))
darktint.set_alpha(180) #Transparency value, 0 is invisible, 255 is solid, 128 is 50%
'''
Changed the plane background for an image that fits the ANTIQUE theme
'''
bg_image = pygame.image.load('images/back.jpg').convert()
bg_image = pygame.transform.scale(bg_image, (600, 600))

timer = pygame.time.Clock()
framerate = 60

circle_x = 300
circle_y = 300

'''
Changing either x or y direction changes the speed in that axis
'''
circle_x_direction = 7 
circle_y_direction = 5

score = 0

font = pygame.font.Font('fonts/Redaction70-Bold.ttf', 30) #In pygame you can't just put text on the screen, you gotta define a font and then render it.
running = True #Can be any variable, just needs to create a game loop

'''
At this point in the video LeMaster says that this tutorial was made and thinked for
people with an intermediate level, who already know basics of Python, such as globals... which I don't.
I'll have to do another Tutorial Series called "Python Basics" after I'm done with this one. Or I could just keep doing pygame and hope for the best.
'''
def update_ball_position():
    global circle_x
    global circle_y 
    global circle_x_direction
    global circle_y_direction
    global score

    if circle_x_direction > 0:
        if circle_x < 555:
            circle_x += circle_x_direction
        else:
            circle_x_direction *= -1
            score += 1

    elif circle_x_direction < 0:
        if circle_x > 45:
            circle_x += circle_x_direction
        else:
            circle_x_direction *= -1
            score += 1

    '''
    Hypothetically, the code SHOULD be the same, but instead of using x direction, we could use y direction...
    '''
    if circle_y_direction > 0:
        if circle_y < 555:
            circle_y += circle_y_direction
        else:
            circle_y_direction *= -1
            score += 1

    elif circle_y_direction < 0:
        if circle_y > 45:
            circle_y += circle_y_direction
        else:
            circle_y_direction *= -1
            score += 1
    

while running: #Python automatically treats this variable as a boolean with value of True
    timer.tick(framerate)
    update_ball_position()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Checks if the user has quit
            running = False
    
    screen.blit(bg_image, (0,0)) #Fill screen with background
    screen.blit(darktint, (0,0)) #Adds a dark tint
    '''
    Draws borders on the screen
    '''
    pygame.draw.rect(screen, darkred, (0, 0, 15, 600))
    pygame.draw.rect(screen, darkred, (585, 0, 15, 600))
    pygame.draw.rect(screen, darkred, (0, 0, 600, 15))
    pygame.draw.rect(screen, darkred, (0, 585, 600, 15))
    display_score = font.render("Score: " + str(score), True, white, black)
    screen.blit(display_score, (15,15))
    pygame.draw.circle(screen, (150, 0, 0), (circle_x, circle_y), 30) #draws a circle, obviously

    pygame.display.flip()

pygame.quit()

