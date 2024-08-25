import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 600
screen_height = 400

# Create game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rock Paper Scissors")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)

# Load images
rock_img = pygame.image.load("rock.jpg")
paper_img = pygame.image.load("paper.jpg")
scissors_img = pygame.image.load("scissor.jpg")

# Resize images
rock_img = pygame.transform.scale(rock_img, (100, 100))
paper_img = pygame.transform.scale(paper_img, (100, 100))
scissors_img = pygame.transform.scale(scissors_img, (100, 100))

# Font for text
font = pygame.font.SysFont(None, 50)

# Choices
choices = ["rock", "paper", "scissors"]

# Function to display text
def display_message(msg, color, y_displace=0):
    text_surf = font.render(msg, True, color)
    text_rect = text_surf.get_rect(center=(screen_width / 2, screen_height / 2 + y_displace))
    screen.blit(text_surf, text_rect)

def game_loop():
    game_exit = False
    player_choice = None
    computer_choice = None
    result = None

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 50 <= mouse_x <= 150 and 150 <= mouse_y <= 250:
                    player_choice = "rock"
                elif 250 <= mouse_x <= 350 and 150 <= mouse_y <= 250:
                    player_choice = "paper"
                elif 450 <= mouse_x <= 550 and 150 <= mouse_y <= 250:
                    player_choice = "scissors"

                if player_choice:
                    computer_choice = random.choice(choices)
                    if player_choice == computer_choice:
                        result = "It's a draw!"
                    elif (player_choice == "rock" and computer_choice == "scissors") or \
                         (player_choice == "paper" and computer_choice == "rock") or \
                         (player_choice == "scissors" and computer_choice == "paper"):
                        result = "You win!"
                    else:
                        result = "You lose!"

        screen.fill(white)

        # Display images for player choices
        screen.blit(rock_img, (50, 150))
        screen.blit(paper_img, (250, 150))
        screen.blit(scissors_img, (450, 150))

        if player_choice:
            display_message(f"Player: {player_choice}", black, -50)
            display_message(f"Computer: {computer_choice}", black, 50)
            display_message(result, red, 100)

        pygame.display.update()

    pygame.quit()
    quit()

game_loop()
