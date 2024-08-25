import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FONT_SIZE = 24

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lottery Game")

# Set up fonts
font = pygame.font.SysFont(None, FONT_SIZE)

def draw_text(surface, text, color, rect, font, align_center=True):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    if align_center:
        textrect.center = rect.center
    else:
        textrect.topleft = rect.topleft
    surface.blit(textobj, textrect)

def main():
    # Variables
    win_number = random.randint(0, 10)
    user_number = None
    message = ""
    input_box = pygame.Rect(150, 100, 100, 30)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        try:
                            user_number = int(text)
                            if user_number == win_number:
                                message = "Congratulations! You Won!"
                            else:
                                message = f"Sorry, You Lost... The Winning number was = {win_number}"
                        except ValueError:
                            message = "Invalid input! Enter a number between 0 and 10."
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(WHITE)
        draw_text(screen, "Enter your number between 0 to 10:", BLACK, pygame.Rect(0, 50, WIDTH, 50), font, align_center=True)
        draw_text(screen, "Press Enter to Submit", BLACK, pygame.Rect(0, 150, WIDTH, 50), font, align_center=True)
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

        if message:
            draw_text(screen, message, GREEN if "Congratulations" in message else RED, pygame.Rect(0, 200, WIDTH, 50), font, align_center=True)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
