# This program will create a simple shooter game

import pygame
import sys

# Initialize the game window
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Shooter Game")

# Define the player's position
player_x = 350
player_y = 500
player_speed = 5

# Define the enemy's position
enemy_x = 500
enemy_y = 250
enemy_speed = 2

# Define the bullet's position
bullet_x = 0
bullet_y = 500
bullet_speed = 10

# Define the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Move the enemy
    enemy_x -= enemy_speed

    # Draw the background
    window.fill(white)

    # Draw the player
    pygame.draw.rect(window, black, (player_x, player_y, 50, 50))

    # Draw the enemy
    pygame.draw.rect(window, red, (enemy_x, enemy_y, 50, 50))

    # Draw the bullet
    pygame.draw.rect(window, black, (bullet_x, bullet_y, 10, 10))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()