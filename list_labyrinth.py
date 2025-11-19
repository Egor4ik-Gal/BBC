import random


def vyvod(board, hp, inv):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()
    print(f'{hp} хп, в инвенторе {inv}')
    print('=====')


def generator():
    n, m = random.randint(1, 5), random.randint(2, 5)
    board = []
    rooms = ['0', '!', '$', '@', '0', '0', '0', '$', '!'] # 0 - пустая, ! - ловушка, $ - сундук, ^ - ключ, # - портал, @ - монстр, * - туман
    l = []
    game_board = []
    # n = 1
    # m = 2
    for y in range(m):
        for x in range(n):
            l.append(random.choice(rooms))
        board.append(l)
        l = []
    for y in range(m):
        for x in range(n):
            l.append('*')
        game_board.append(l)
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

    # vyvod(game_board)
    return game_board, board


def open(board, sec_board, x, y):
    board[y][x] = sec_board[y][x]
    return board


def start():
    items = {"меч": 50, "пистолет": 100, "граната": 75}
    board, sec_board = generator()
    x, y = 0, 0
    hp = 100
    fl = 1
    chek = 1
    inventory = ['', '', '']
    board = open(board, sec_board, x, y)

    print("Привет, Игрок! Твоя задача найти выход и остаться в живых, но не забудь ключ!")
    vyvod(board, hp, inventory)
    while fl:
        if board[y][x] == '!':
            print('Ты попал в ловушку! Ты потерял 20 хп')
            hp -= 20
            if hp <= 0:
                chek = 0
        elif board[y][x] == '@':
            print("Ты забрел к монстру, СРАЖАЙСЯ!")
            if inventory:
                print("Ты легко его одолел")
            else:
                print("Ты еле выжил")
                hp -= 70
                if hp <= 0:
                    chek = 0
        elif board[y][x] == '0':
            print("Эта комната пуста")
        elif board[y][x] == '$':
            print("Ты нашел сундук, что же в нем?")
            r = random.randint(0, 2)
            print(f"{[*items.keys()][r]} куда положить? (выбери слот (цифру) в инветоре)")
            slot = int(input())
            while slot > 3 or slot < 1:
                print("Выбери корректный слот!")
                slot = int(input())
            inventory[slot - 1] = [*items.keys()][r]
        elif board[y][x] == '^':
            print("Ты нашел ключ от портала, куда положить? (Можешь заменить что-то)")
            slot = int(input())
            while int(slot) > 3 or int(slot) < 1:
                print("Выбери корректный слот!")
                slot = int(input())
            inventory[slot - 1] = "ключ"
        elif board[y][x] == '#':
            if 'ключ' in inventory:
                fl = 0
                # print("Поздравляю, ты победил!")
            else:
                print("Кто-то забыл ключ...")
        if hp > 0:
            print("Куда походим? (wasd)")
            hod = input()
            flag = 1
            while flag:
                if sec_board[y][x] == "#" and 'ключ' in inventory:
                    break

                if hod == 'w':
                    if 0 <= y - 1 < len(board):
                        y = y - 1
                        flag = 0
                        break
                    else:
                        print("Ты не убежишь за поле!")
                elif hod == 'a':
                    if 0 <= x - 1 < len(board[0]):
                        x = x - 1
                        flag = 0
                        break
                    else:
                        print("Ты не убежишь за поле!")
                elif hod == 's':
                    if 0 <= y + 1 < len(board):
                        y = y + 1
                        flag = 0
                        break
                    else:
                        print("Ты не убежишь за поле!")
                elif hod == 'd':
                    if 0 <= x + 1 < len(board[0]):
                        x = x + 1
                        flag = 0
                        break
                    else:
                        print("Ты не убежишь за поле!")
                hod = input()
            open(board, sec_board, x, y)
            vyvod(board, hp, inventory)
            if chek == 0:
                flag = 0
        else:
            print("Ты проиграл, у тебя 0 хп!!!")
            fl = 0
    if chek:
        print(f"Поздравляю, ты победил! У тебя осталось {hp} хп, а в твоем инветоре осталось: {inventory}")
start()