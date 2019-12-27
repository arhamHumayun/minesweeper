# Board Legend

import pygame
import os
import random
pygame.init()
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)

window = pygame.display.set_mode((640, 480))
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


def generate_new_board(cx, cy):
    game = []

    for row in range(BOARD_WIDTH):
        game.append([])
        for column in range(BOARD_HEIGHT):
            game[row].append(0)

    bombCount = 0
    while True:
        row = random.randint(0, BOARD_WIDTH - 1)
        col = random.randint(0, BOARD_HEIGHT - 1)
        if game[row][col] != 10 and (row != cx or col != cy):
            game[row][col] = 10
            bombCount += 1
            if bombCount == MINES:
                break

    for row in range(BOARD_WIDTH):
        for col in range(BOARD_HEIGHT):
            if game[row][col] >= 10:
                for x in range(row - 1, row + 2):
                    for y in range(col - 1, col + 2):
                        if (x != row or y != col) and x in range(BOARD_WIDTH) and y in range(BOARD_HEIGHT):
                            game[x][y] += 1

    return game, 1


def draw_board():

    if GAME_MODE in [0, 1]:
        window.blit(smiles[0], (50, 20))
    elif GAME_MODE == 2:
        window.blit(smiles[4], (50, 20))
    elif GAME_MODE == 3:
        window.blit(smiles[3], (50, 20))

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

    if x in range(50, 77) and y in range (20, 47):
        return -1, -1
    elif x in range(30, 130) and y in range (420, 470):
        return -1, 0
    elif x in range(150, 250) and y in range (420, 470):
        return -2, 0
    elif x in range(270, 370) and y in range(420, 470):
        return -3, 0
    elif x in range(390, 490) and y in range(420, 470):
        return -4, 0
    elif x in range(510, 610) and y in range(420, 470):
        return -5, 0


    else:
        row = (x - x_offset) // 16
        col = (y - y_offset) // 16
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
            return 2
        else:
            return 1

def generate_visual():
    visual = []
    for row in range(BOARD_WIDTH):
        visual.append([])
        for column in range(BOARD_HEIGHT):
            visual[row].append(10)

    pygame.draw.rect(window, (100, 100, 100), ((30,  420), (100, 50)))
    pygame.draw.rect(window, (100, 100, 100), ((150, 420), (100, 50)))
    pygame.draw.rect(window, (100, 100, 100), ((270, 420), (100, 50)))
    pygame.draw.rect(window, (100, 100, 100), ((390, 420), (100, 50)))
    pygame.draw.rect(window, (100, 100, 100), ((510, 420), (100, 50)))

    myfont = pygame.font.SysFont('', 25)
    textsurface = myfont.render('Easy', False, (0, 0, 0))
    window.blit(textsurface, (35, 435))
    textsurface = myfont.render('Medium', False, (0, 0, 0))
    window.blit(textsurface, (155, 435))
    textsurface = myfont.render('Hard', False, (0, 0, 0))
    window.blit(textsurface, (275, 435))
    textsurface = myfont.render('Expert', False, (0, 0, 0))
    window.blit(textsurface, (395, 435))
    textsurface = myfont.render('Master', False, (0, 0, 0))
    window.blit(textsurface, (515, 435))

    return visual


def clear_space(row, col):
    flag_count = 0
    if GAME_GRID[row][col] in range(1, 9):
        for x in range(row - 1, row + 2):
            for y in range(col - 1, col + 2):
                if (x != row or y != col) and x in range(BOARD_WIDTH) and y in range(BOARD_HEIGHT) \
                        and (VISUAL_BOARD[x][y] == 11):
                    flag_count += 1

    if flag_count == GAME_GRID[row][col]:
        for x in range(row - 1, row + 2):
            for y in range(col - 1, col + 2):
                if (x != row or y != col) and x in range(BOARD_WIDTH) and y in range(BOARD_HEIGHT)\
                        and (VISUAL_BOARD[x][y] != 11):
                    update_board(x, y)


def check_win(vb):
    clears = 0
    for row in range(BOARD_WIDTH):
        for col in range(BOARD_HEIGHT):
            if vb[row][col] in range(0, 9):
                clears += 1
    if clears == ((BOARD_HEIGHT * BOARD_WIDTH) - MINES):
        return 3
    else:
        return 1

def mode(x):
    if x == 0:
        return 9, 9, 10
    if x == 1:
        return 16, 16, 40
    if x == 2:
        return 16, 30, 99
    if x == 3:
        return 20, 30, 145
    if x == 3:
        return 25, 35, 200

size = 16
x_offset = 20
y_offset = 70
GAME_MODE = 0 # 0 - fresh start, 1 - playing, 2 - gameover, 3 - win
DIFFICULTY = 1
BOARD_HEIGHT, BOARD_WIDTH, MINES = mode(DIFFICULTY)
run = True
GAME_GRID = []
VISUAL_BOARD = generate_visual()
draw_board()

while run:
    pygame.time.delay(1)
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        mbs = pygame.mouse.get_pressed()
        if event.type == pygame.QUIT:
            run = False

        if GAME_MODE == 0:
            draw_board()
            VISUAL_BOARD = generate_visual()

        if event.type == pygame.MOUSEBUTTONUP:
            row, col = get_clicked_cell()
            if (row, col) ==   (-1, -1):
                GAME_MODE = 0
            elif (row, col) == (-1, 0):
                print('easy')
                DIFFICULTY = 1
                GAME_MODE = 0
                BOARD_HEIGHT, BOARD_WIDTH, MINES = mode(DIFFICULTY)
            elif (row, col) == (-2, 0):
                print('mediam')
                DIFFICULTY = 2
                GAME_MODE = 0
                BOARD_HEIGHT, BOARD_WIDTH, MINES = mode(DIFFICULTY)
            elif (row, col) == (-3, 0):
                print('hard')
                DIFFICULTY = 3
                GAME_MODE = 0
                BOARD_HEIGHT, BOARD_WIDTH, MINES = mode(DIFFICULTY)
            elif (row, col) == (-4, 0):
                print('expert')
                DIFFICULTY = 4
                GAME_MODE = 0
                BOARD_HEIGHT, BOARD_WIDTH, MINES = mode(DIFFICULTY)
            elif (row, col) == (-5, 0):
                print('master')
                DIFFICULTY = 5
                GAME_MODE = 0
                BOARD_HEIGHT, BOARD_WIDTH, MINES = mode(DIFFICULTY)

            elif row in range(BOARD_WIDTH) and col in range(BOARD_HEIGHT):
                if event.button == 1:
                    if GAME_MODE == 0:
                        GAME_GRID, GAME_MODE = generate_new_board(row, col)
                        VISUAL_BOARD = generate_visual()
                        update_board(row, col)
                    elif GAME_MODE == 1:
                        GAME_MODE = update_board(row, col)
                        if GAME_MODE != 2:
                            GAME_MODE = check_win(VISUAL_BOARD)
                if event.button == 2 and GAME_MODE == 1:
                    clear_space(row, col)
                if event.button == 3 and GAME_MODE == 1:
                    flag_board(row, col)

            draw_board()
    pygame.display.update()

pygame.quit()
