import random


def vyvod(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()


def generator():
    n, m = random.randint(1, 5), random.randint(2, 5)
    board = []
    rooms = ['0', '!', '$', '@', '0', '0', '0', '$', '!'] # 0 - пустая, ! - ловушка, $ - сундук, ^ - ключ, # - портал, @ - монстр, * - туман
    l = []
    # n = 1
    # m = 2
    for y in range(m):
        for x in range(n):
            l.append(random.choice(rooms))
        board.append(l)
        l = []
    # обязательно 1 ключ 1 портал
    if '^' not in board:
        x1, y1 = random.randint(0, n), random.randint(0, m)
        while x1 >= n or y1 >= m:
            x1, y1 = random.randint(0, n), random.randint(0, m)
        board[y1][x1] = '^'
    if "#" not in board:
        x1, y1 = random.randint(0, n), random.randint(0, m)
        while x1 >= n or y1 >= m or board[y1][x1] == '^':
            x1, y1 = random.randint(0, n), random.randint(0, m)
        board[y1][x1] = '#'

    vyvod(board)


generator()