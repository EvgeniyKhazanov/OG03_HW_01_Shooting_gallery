import pygame
import random
import math
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра 'ТИР'")
#icon = pygame.image.load("img/goggame-1240899991.ico")
#pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

target_radius = 50
target_position = (random.randint(target_radius, SCREEN_WIDTH - target_radius),
                   random.randint(target_radius, SCREEN_HEIGHT - target_radius))


def calculate_score(click_position, target_position):
    distance = math.sqrt((click_position[0] - target_position[0]) ** 2 + (click_position[1] - target_position[1]) ** 2)
    score = max(0, round((target_radius - distance) * 2))  # Примерный расчет очков
    return score

running = True
score = 0

# Определение координат центра мишени
target_center_x = target_x + target_width / 2
target_center_y = target_y + target_height / 2

while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверка, попал ли клик в мишень
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Вызываем функцию calculate_score для обновления счета
                score += calculate_score((mouse_x, mouse_y), (target_center_x, target_center_y))
                # Генерируем новое положение мишени
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Обновляем координаты центра мишени после ее перемещения
                target_center_x = target_x + target_width / 2
                target_center_y = target_y + target_height / 2
            
            print(f"Текущий счет: {score}")

    screen.blit(target_img, (target_x, target_y))

    pygame.display.update()

pygame.quit()