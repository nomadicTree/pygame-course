import pygame
import sys

pygame.init()

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Window")

clock = pygame.time.Clock()

x = 300  # shape's starting x-position

running = True
while running:
    # --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- UPDATE WORLD ---
    x = x + 1

    # --- DRAW WORLD ---
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (x, 200), 40)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
