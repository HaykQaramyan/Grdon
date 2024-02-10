import pygame, sys

a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
c = a + b
pygame.init()
clock = pygame.time.Clock()
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
BG_COLOR = (255, 255, 255)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill(BG_COLOR)
img1= pygame.image.load("./python_photo.png").convert()
screen.blit(img1, (0, 0))
font = pygame.font.SysFont('freesansbold.ttf', 24)
d = font.render(f"{c}", True, 'red')
screen.blit(d, (20, 20))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)