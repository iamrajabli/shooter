import sys

import pygame

pygame.init()

pygame.display.set_caption("Awesome Shooter Game")

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen_fill_color = (32, 52, 71)

fighter_image = pygame.image.load("images/fighter.png")
fighter_width, fighter_height = fighter_image.get_size()
fighter_x, fighter_y = screen_width / 2 - fighter_width / 2, screen_height - fighter_height
fighter_is_moving_left, fighter_is_moving_right = False, False
FIGHTER_STEP = 0.5

ball_image = pygame.image.load("images/ball.png")
ball_width, ball_height = ball_image.get_size()
ball_x, ball_y = 0, 0
ball_was_fired = False
BALL_STEP = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
            if event.key == pygame.K_SPACE:
                ball_was_fired = True
                ball_x = fighter_x + fighter_width / 2 - ball_width / 2
                ball_y = fighter_y - ball_height

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP

    if fighter_is_moving_right and screen_width - fighter_width >= fighter_x + FIGHTER_STEP:
        fighter_x += FIGHTER_STEP

    if ball_was_fired and ball_y + ball_height < 0:
        ball_was_fired = False

    screen.fill(screen_fill_color)
    screen.blit(fighter_image, (fighter_x, fighter_y))

    if ball_was_fired:
        ball_y -= BALL_STEP
        screen.blit(ball_image, (ball_x, ball_y))

    pygame.display.update()
