import pygame
from random import randint

class Ball:
    def __init__(self, screen, pos):
        self.screen = screen
        self.x = pos[0]
        self.y = pos[1]
        self.color = randint(0, 255), randint(0, 255), randint(0, 255)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), 10)

    def move(self, t):
        self.y += v * t / 1000

balls = []

pygame.init()
size = width, height = 400, 300
screen = pygame.display.set_mode(size)

v = 100
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                ball = Ball(screen, event.pos)
                balls.append(ball)
                
    screen.fill((0, 0, 0))
    t = clock.tick()
    for ball in balls:
        if ball.y < 290:
            ball.move(t)
        ball.draw()

    pygame.display.flip()

pygame.quit()
