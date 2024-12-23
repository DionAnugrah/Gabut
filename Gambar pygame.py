import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Atur layar
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Happy Birthday Animation")
font = pygame.font.Font(None, 74)
text = "Happy Birthday!"

# Warna
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Variabel animasi
x = 50
y = 200
index = 0
clock = pygame.time.Clock()

# Loop utama
running = True
while running:
    screen.fill(WHITE)

    # Animasi menulis teks huruf per huruf
    if index <= len(text):
        displayed_text = text[:index]
        rendered_text = font.render(displayed_text, True, BLUE)
        screen.blit(rendered_text, (x, y))
        index += 1

    pygame.display.flip()
    clock.tick(5)  # Kecepatan animasi (huruf per detik)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
