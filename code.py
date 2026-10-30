'''This weeks theme is: ANTIQUE!!

Make something with just a terminal , an 8-bit game, or anything else that makes you think "wow this is really old"'''

import pygame
pygame.init() #initializes pygame

screen = pygame.display.set_mode([600, 600]) #defines size of the screen

#Defines basic colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
background = blue

timer = pygame.time.Clock()
framerate = 60

circle_x = 300
circle_y = 300

'''
Changing either x or y direction changes the speed in that axis
'''
circle_x_direction = 7 
circle_y_direction = 5

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

    if circle_x_direction > 0:
        if circle_x < 570:
            circle_x += circle_x_direction
        else:
            circle_x_direction *= -1

    elif circle_x_direction < 0:
        if circle_x > 30:
            circle_x += circle_x_direction
        else:
            circle_x_direction *= -1

    '''
    Hypothetically, the code SHOULD be the same, but instead of using x direction, we could use y direction...
    '''
    if circle_y_direction > 0:
        if circle_y < 570:
            circle_y += circle_y_direction
        else:
            circle_y_direction *= -1

    elif circle_y_direction < 0:
        if circle_y > 30:
            circle_y += circle_y_direction
        else:
            circle_y_direction *= -1
    

while running: #Python automatically treats this variable as a boolean with value of True
    timer.tick(framerate)
    update_ball_position()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Checks if the user has quit
            running = False

    screen.fill((background)) #Fill screen with background

    pygame.draw.circle(screen, red, (circle_x, circle_y), 30, 5) #draws a circle, obviously

    pygame.display.flip()

pygame.quit()

