# Board Legend

import pygame
import os
import random
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Minesweeper")

block = pygame.image.load(os.path.join('assets/block.png'))
flag = pygame.image.load(os.path.join('assets/flag.png'))
bombs = [pygame.image.load(os.path.join('assets/bomb1.png')),
         pygame.image.load(os.path.join('assets/bomb2.png')),
         pygame.image.load(os.path.join('assets/bomb3.png'))]
numbers = [pygame.image.load(os.path.join('assets/swept.png')),
           pygame.image.load(os.path.join('assets/1.png')),
           pygame.image.load(os.path.join('assets/2.png')),
           pygame.image.load(os.path.join('assets/3.png')),
           pygame.image.load(os.path.join('assets/4.png')),
           pygame.image.load(os.path.join('assets/5.png')),
           pygame.image.load(os.path.join('assets/6.png')),
           pygame.image.load(os.path.join('assets/7.png')),
           pygame.image.load(os.path.join('assets/8.png'))]
smiles = [pygame.image.load(os.path.join('assets/smile1.png')),
          pygame.image.load(os.path.join('assets/smile2.png')),
          pygame.image.load(os.path.join('assets/smile3.png')),
          pygame.image.load(os.path.join('assets/smile4.png')),
          pygame.image.load(os.path.join('assets/smile5.png'))]


def generate_new_board():
    game = []
    visual = []

    for row in range(BOARD_WIDTH):
        game.append([])
        visual.append([])
        for column in range(BOARD_HEIGHT):
            game[row].append(0)
            visual[row].append(10)

    bombCount = 0
    while True:
        row = random.randint(0, BOARD_WIDTH - 1)
        col = random.randint(0, BOARD_HEIGHT - 1)
        if game[row][col] != 10:
            game[row][col] = 10
            bombCount += 1
            if bombCount > MINES:
                break

    for row in range(BOARD_WIDTH):
        for col in range(BOARD_HEIGHT):
            if game[row][col] >= 10:
                for x in range(row - 1, row + 2):
                    for y in range(col - 1, col + 2):
                        if (x != row or y != col) and x in range(BOARD_WIDTH) and y in range(BOARD_HEIGHT):
                            game[x][y] += 1

    return game, visual


def drawBoard():

    if GAME_MODE == 4:
        window.blit(smiles[5], (50, 20))
    else:
        window.blit(smiles[0], (50, 20))

    for row in range(BOARD_WIDTH):
        for col in range(BOARD_HEIGHT):
            if VISUAL_BOARD[row][col] == 10:
                window.blit(block, ((row * size) + x_offset, (col * size) + y_offset))
            elif VISUAL_BOARD[row][col] == 11:
                window.blit(flag, ((row * size) + x_offset, (col * size) + y_offset))
            elif VISUAL_BOARD[row][col] == 101:
                window.blit(bombs[0], ((row * size) + x_offset, (col * size) + y_offset))
            elif VISUAL_BOARD[row][col] == 102:
                window.blit(bombs[1], ((row * size) + x_offset, (col * size) + y_offset))
            elif VISUAL_BOARD[row][col] == 103:
                window.blit(bombs[2], ((row * size) + x_offset, (col * size) + y_offset))
            elif VISUAL_BOARD[row][col] == 0:
                window.blit(numbers[0], ((row * size) + x_offset, (col * size) + y_offset))
            elif VISUAL_BOARD[row][col] == 1:
                window.blit(numbers[1], ((row * size) + x_offset, (col * size) + y_offset))
            elif VISUAL_BOARD[row][col] == 2:
                window.blit(numbers[2], ((row * size) + x_offset, (col * size) + y_offset))
            elif VISUAL_BOARD[row][col] == 3:
                window.blit(numbers[3], ((row * size) + x_offset, (col * size) + y_offset))
            elif VISUAL_BOARD[row][col] == 4:
                window.blit(numbers[4], ((row * size) + x_offset, (col * size) + y_offset))
            elif VISUAL_BOARD[row][col] == 5:
                window.blit(numbers[5], ((row * size) + x_offset, (col * size) + y_offset))
            elif VISUAL_BOARD[row][col] == 6:
                window.blit(numbers[6], ((row * size) + x_offset, (col * size) + y_offset))
            elif VISUAL_BOARD[row][col] == 7:
                window.blit(numbers[7], ((row * size) + x_offset, (col * size) + y_offset))
            elif VISUAL_BOARD[row][col] == 8:
                window.blit(numbers[8], ((row * size) + x_offset, (col * size) + y_offset))

def get_clicked_cell():
    x, y = pygame.mouse.get_pos()
    row = (x - x_offset) // 16
    col = (y - y_offset) // 16
    print(row, col)
    return row, col


def flag_board(row, col):
    if VISUAL_BOARD[row][col] == 10:
        VISUAL_BOARD[row][col] = 11
    elif VISUAL_BOARD[row][col] == 11:
        VISUAL_BOARD[row][col] = 10


def update_board(row, col):
    if VISUAL_BOARD[row][col] == 10:
        if GAME_GRID[row][col] == 0:
            VISUAL_BOARD[row][col] = 0
            for x in range(row - 1, row + 2):
                for y in range(col - 1, col + 2):
                    if (x != row or y != col) and x in range(BOARD_WIDTH) and y in range(BOARD_HEIGHT):
                        update_board(x, y)

        elif GAME_GRID[row][col] in range(1, 9):
            VISUAL_BOARD[row][col] = GAME_GRID[row][col]

        elif GAME_GRID[row][col] >= 10:
            VISUAL_BOARD[row][col] = 103
            GAME_MODE = 4


size = 16
x_offset = 20
y_offset = 70
GAME_MODE = 0  # 0 - beginner, 1 - intermediate, 2 - expert, 3 - Win, 4 - Gameover
BOARD_WIDTH = 9
BOARD_HEIGHT = 9
MINES = 10
run = True
GAME_GRID, VISUAL_BOARD = generate_new_board()

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        mbs = pygame.mouse.get_pressed()
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            row, col = get_clicked_cell()
            if row in range(BOARD_WIDTH) and col in range(BOARD_HEIGHT):
                if event.button == 1:
                    update_board(row, col)
                if event.button == 3:
                    flag_board(row, col)

            drawBoard()

    pygame.display.update()

pygame.quit()
