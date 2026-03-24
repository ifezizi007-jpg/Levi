import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

WHITE = (255,255,255)
GREEN = (0,200,0)
RED = (200,0,0)
BLACK = (0,0,0)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK, BLOCK])

def message(text, color):
    msg = font.render(text, True, color)
    screen.blit(msg, [WIDTH/6, HEIGHT/3])

def game_loop():

    game_over = False
    game_close = False

    x = WIDTH//2
    y = HEIGHT//2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = random.randrange(0, WIDTH-BLOCK, BLOCK)
    food_y = random.randrange(0, HEIGHT-BLOCK, BLOCK)

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("Game Over! Press C or Q", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK
                    y_change = 0

                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK
                    y_change = 0

                elif event.key == pygame.K_UP:
                    y_change = -BLOCK
                    x_change = 0

                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK
                    x_change = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change

        screen.fill(BLACK)

        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK, BLOCK])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_list)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH-BLOCK, BLOCK)
            food_y = random.randrange(0, HEIGHT-BLOCK, BLOCK)
            snake_length += 1

        clock.tick(4)

    pygame.quit()
    sys.exit()

game_loop()