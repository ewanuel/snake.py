import pygame
import sys
import random

pygame.init()

x = 800
y = 600
backg = (0, 0, 0)
v_base = 15

screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Snake game")

snake_p = [100, 50]
snake_rgb = (255, 255, 255)
snake_size = 1
snake_c = [[100, 50]]

food_p = [random.randrange(1, (x // 10)) * 10, random.randrange(1, (y // 10)) * 10]
food_rgb = (255, 0, 0)

move_direction = (0, 0)  

score = 0

loopgame = True

while loopgame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loopgame = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        move_direction = (0, -10)
    elif keys[pygame.K_s]:
        move_direction = (0, 10)
    elif keys[pygame.K_a]:
        move_direction = (-10, 0)
    elif keys[pygame.K_d]:
        move_direction = (10, 0)

    # Atualiza a posição da cobra com base na direção atual
    snake_p[0] += move_direction[0]
    snake_p[1] += move_direction[1]

    snake_c.insert(0, list(snake_p))
    if snake_p[0] == food_p[0] and snake_p[1] == food_p[1]:
        food_p = [random.randrange(1, (x // 10)) * 10, random.randrange(1, (y // 10)) * 10]
        snake_size += 1

    while len(snake_c) > snake_size:
        if snake_c:
            del snake_c[-1]
        else:
            break
        

    # Verifica colisão da cabeça com o corpo
    if snake_p in snake_c[1:]:
        loopgame = False 

    # Verifica colisão com as bordas
    if snake_p[0] < 0 or snake_p[0] >= x or snake_p[1] < 0 or snake_p[1] >= y:
        loopgame = False  

    screen.fill(backg)
    pygame.draw.rect(screen, snake_rgb, pygame.Rect(snake_p[0], snake_p[1], 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_p[0], food_p[1], 10, 10))
    for pos in snake_c:
        pygame.draw.rect(screen, snake_rgb, pygame.Rect(pos[0], pos[1], 10, 10))

    font = pygame.font.SysFont("Arial", 36)
    score_text = font.render("Score: {}".format(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(v_base)

pygame.quit()
sys.exit()