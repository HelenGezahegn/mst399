import pygame
import sys

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("MakeyMakey Click Detector")

font = pygame.font.SysFont("Arial", 24)

def display_message(message):
    screen.fill((30, 30, 30))
    text_surface = font.render(message, True, (255, 255, 255))
    screen.blit(text_surface, (50, 130))
    pygame.display.flip()

display_message("Touch the robot hands!")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse buttons
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("🖱️ Left click detected from robot hand")
                display_message("🖱️ Left click!")
            elif event.button == 3:
                print("👉 Right click detected from robot hand")
                display_message("👉 Right click!")

        # Keyboard (for remapped SPACE)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("👉 Right click detected via SPACE key")
                display_message("👉 SPACE (Right Click)")

pygame.quit()
sys.exit()