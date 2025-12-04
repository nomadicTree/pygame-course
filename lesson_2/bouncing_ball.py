import pygame
import sys

WIDTH = 600
HEIGHT = 400
CLOCK = 60


class Ball:
    def __init__(self, p_color, p_radius, p_x, p_y, p_vx, p_vy):
        self.color = p_color
        self.radius = p_radius
        self.vx = p_vx
        self.vy = p_vy
        self.x = p_x
        self.y = p_y

    def get_coords(self):
        return (self.x, self.y)

    def _get_left(self):
        return self.x - self.radius

    def _get_right(self):
        return self.x + self.radius

    def _get_top(self):
        return self.y - self.radius

    def _get_bottom(self):
        return self.y + self.radius

    def _draw(self, screen):
        pygame.draw.circle(screen, self.color, self.get_coords(), self.radius)

    def _move(self, x_bounds, y_bounds):
        # Check if the ball is out of bounds
        if self._get_left() < x_bounds[0]:
            self.vx = -self.vx
            self.x = x_bounds[0] + self.radius
        elif self._get_right() > x_bounds[1]:
            self.vx = -self.vx
            self.x = x_bounds[1] - self.radius
        if self._get_top() < y_bounds[0]:
            self.vy = -self.vy
            self.y = y_bounds[0] + self.radius
        elif self._get_bottom() > y_bounds[1]:
            self.vy = -self.vy
            self.y = y_bounds[1] - self.radius

        self.x = self.x + self.vx
        self.y = self.y + self.vy

    def update(self, screen, x_bounds, y_bounds):
        self._move(x_bounds, y_bounds)
        self._draw(screen)


pygame.init()


def main():
    running = True
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    ball = Ball((255, 0, 0), 40, (WIDTH // 2), (HEIGHT // 2), 5, 5)
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        ball.update(screen, (0, WIDTH), (0, HEIGHT))
        pygame.display.flip()
        clock.tick(CLOCK)

    pygame.quit()
    sys.exit()


main()
