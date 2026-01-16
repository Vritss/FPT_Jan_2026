# Ninja Frog Jump Game
# Name: Vritika
# Course: ICSUI
# Date: Jan 2026
# Simple pygame jumping game using images, collision detection, and the game ends when the score reaches the target. 
import pygame
import random

# SETUP 
pygame.init()
WIDTH = 1000
HEIGHT = 667
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #creates a 1000 x 667 game window 
pygame.display.set_caption("Ninja Frog")

clock = pygame.time.Clock()

#LOAD IMAGES 
frog_img = pygame.image.load("run01.png")
frog_img = pygame.transform.scale(frog_img, (96, 96))  # resize frog

saw_img = pygame.image.load("saw01.png")

# GAME STATES 
MENU = 0
PLAY = 1
GAME_OVER = 2
game_state = MENU

# FROG VARIABLES 
frog_x = 150
frog_y = 450
frog_y_speed = 0
gravity = 1
jump_power = -15

#  SAW VARIABLES 
saw_x = WIDTH
saw_y = 500
saw_size = random.randint(32, 50)
saw_speed = 5

# SCORE 
score = 0
font = pygame.font.SysFont(None, 36)

#  FUNCTIONS 
def reset_saw():
    """Resets saw position and size"""
    global saw_x, saw_size
    saw_x = WIDTH + random.randint(100, 300)
    saw_size = random.randint(30, 40)

#  MAIN LOOP
running = True
while running:
    clock.tick(60)

    # EVENTS 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse click for menu & restart
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == MENU:
                game_state = PLAY
                score = 0
                reset_saw()
            elif game_state == GAME_OVER:
                game_state = MENU

        # Jump when space is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_state == PLAY:
                if frog_y >= 450:
                    frog_y_speed = jump_power

    # DRAW BACKGROUND 
    screen.fill((200, 200, 200))  # simple background

    # MENU 
    if game_state == MENU:
        title = font.render("NINJA FROG", True, (0, 0, 0))
        instructions = font.render("Click to Start | Space to Jump", True, (0, 0, 0))
        screen.blit(title, (WIDTH // 2 - 80, HEIGHT // 2 - 40))
        screen.blit(instructions, (WIDTH // 2 - 160, HEIGHT // 2 + 10))

    # GAME 
    if game_state == PLAY:

        # Gravity effect
        frog_y_speed += gravity
        frog_y += frog_y_speed

        # Stop frog on ground
        if frog_y > 450:
            frog_y = 450
            frog_y_speed = 0

        # Move saw
        saw_x -= saw_speed

        # Reset saw when off screen
        if saw_x < -50:
            reset_saw()
            score += 1

        # Collision detection
        frog_rect = pygame.Rect(frog_x, frog_y, 96, 96)
        saw_rect = pygame.Rect(saw_x, saw_y, saw_size, saw_size)

        if frog_rect.colliderect(saw_rect):
            game_state = GAME_OVER

        # Draw frog and saw
        screen.blit(frog_img, (frog_x, frog_y))
        screen.blit(pygame.transform.scale(saw_img, (saw_size, saw_size)), (saw_x, saw_y))

        # Draw score
        score_text = font.render("Score: " + str(score), True, (0, 0, 0))
        screen.blit(score_text, (20, 20))

    # GAME OVER 
    if game_state == GAME_OVER:
        over_text = font.render("GAME OVER", True, (0, 0, 0))
        restart_text = font.render("Click to return to menu", True, (0, 0, 0))
        screen.blit(over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 30))
        screen.blit(restart_text, (WIDTH // 2 - 160, HEIGHT // 2 + 20))

    pygame.display.update()

pygame.quit()
