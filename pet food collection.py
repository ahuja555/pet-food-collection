import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pet Food Collection Game")
clock = pygame.time.Clock()

# 1. Background & Font
bg = pygame.transform.scale(pygame.image.load("background.png"), (WIDTH, HEIGHT))
font = pygame.font.SysFont("comicsansms", 48)

# 2. Sprite Classes
class Pet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("pet.png"), (60, 60))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("food.png"), (35, 35))
        self.rect = self.image.get_rect(
            topleft=(random.randint(20, WIDTH - 55), random.randint(20, HEIGHT - 55))
        )

# 3. Sprite Setup
pet = Pet()
food_group = pygame.sprite.Group(Food() for _ in range(8))

# 4. Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pet.update()
    pygame.sprite.spritecollide(pet, food_group, True)

    screen.blit(bg, (0, 0))
    food_group.draw(screen)
    screen.blit(pet.image, pet.rect)

    # Check if all food is collected
    if len(food_group) == 0:
        msg = font.render("All Food Collected! You Win!", True, (255, 255, 255))
        msg_rect = msg.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(msg, msg_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()