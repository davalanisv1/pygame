import pygame
pygame.init()

screen = pygame.display.set_mode([600, 600]) 
bg_image = pygame.image.load('images/back.jpg').convert()
bg_image = pygame.transform.scale(bg_image, (600, 600))

red = (255, 0, 0)
darkred = (80, 0, 0)
green = (0, 255, 0)
darkgreen = (0, 99, 15)
playercolor = (148, 16, 69)
white = (255,255,255)
black = (0,0,0)
darktint = pygame.Surface((600, 600))
darktint.fill((0,0,0))
darktint.set_alpha(180) 

timer = pygame.time.Clock()
framerate = 60

circle_x = 300
circle_y = 300

player_width = 50
player_height = 50
player_x = 300
player_y = 500
player_x_direction = 0
player_y_direction = 0
player_speed = 7


'''
Changing either x or y direction changes the speed in that axis
'''
circle_x_direction = 20
circle_y_direction = 16

score = 0

font = pygame.font.Font('fonts/Redaction70-Bold.ttf', 30)
game_over_font = pygame.font.Font('fonts/Redaction70-Bold.ttf', 60) 

running = True 

def check_coll(playerx, playery, circlex, circley):
    if abs(playerx - circlex) < 45 and abs(playery - circley) < 45:
        global player_x_direction
        global player_y_direction
        global circle_x_direction
        global circle_y_direction 
        player_x_direction = 0
        player_y_direction = 0
        circle_x_direction = 0
        circle_y_direction = 0
        game_over()

def game_over():
    display_game_over = game_over_font.render("Game Over", True, (200, 0, 0), black) 
    screen.blit(display_game_over, (150,150))

def update_player_position():
    global player_x
    global player_y
    global player_x_direction
    global player_y_direction

    if player_x_direction > 0:
        if player_x < 585 - player_width:
            player_x += player_x_direction * player_speed
    if player_x_direction < 0:
        if player_x > 15:
            player_x += player_x_direction * player_speed

    if player_y_direction > 0:
        if player_y < 585 - player_height:
            player_y += player_y_direction * player_speed
    if player_y_direction < 0:
        if player_y > 15:
            player_y += player_y_direction * player_speed

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



while running: 
    timer.tick(framerate)
    update_ball_position()
    update_player_position()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_x_direction = -1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_x_direction = 1
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player_y_direction = -1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_y_direction = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_x_direction = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_x_direction = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player_y_direction = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_y_direction = 0
    
    screen.blit(bg_image, (0,0)) 
    screen.blit(darktint, (0,0)) #

    '''
    Draws borders on the screen
    '''
    pygame.draw.rect(screen, darkred, (0, 0, 15, 600))
    pygame.draw.rect(screen, darkred, (585, 0, 15, 600))
    pygame.draw.rect(screen, darkred, (0, 0, 600, 15))
    pygame.draw.rect(screen, darkred, (0, 585, 600, 15))


    display_score = font.render("Score: " + str(score), True, white, black) 
    screen.blit(display_score, (15,15))
    circle = pygame.draw.circle(screen, (150, 0, 0), (circle_x, circle_y), 30) #Killer ball
    player = pygame.draw.rect(screen, playercolor, (player_x, player_y, player_width, player_height))  #Player
    check_coll(player.centerx, player.centery, circle.centerx, circle.centery)
    pygame.display.flip()

pygame.quit()

