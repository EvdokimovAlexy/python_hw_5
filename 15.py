import random
konfet = 2021
player_1 = 0
player_2 = 0
def rnd():
    return random.randint(1, 2)
luck = rnd()
print(luck)
win_1 = []
win_2 = []
key = True
while konfet > 0:
    if luck == 1:
        player_1 = int(input('игрок 1 введите значение\nсколько хотите конфет ='))
        while player_1 > 28:
            player_1 = int(input('игрок 1 введите значение\n '))
        konfet = konfet - player_1
        print(f'Осталось {konfet} конфет')
        win_1.append(player_1)
        if konfet == 0:
            print(f'Победа Игрока № 1,', sum(win_2))
        player_2 = int(input('Игрок 2 введите значение\n'))
        while player_2 > 28:
            player_2 = int(input('Игрок 2 введите значение\n '))
        konfet = konfet - player_2
        print(konfet)
        win_2.append(player_2)
        if konfet == 0:
            print(f'Победа Игрока № 2', sum(win_2))


    else:
        player_2 = int(input('Игрок 2 введите значение\n'))
        while player_2 > 28:
            player_2 = int(input('Игрок 2 введите значение\n'))
        konfet = konfet - player_2
        print(konfet)
        win_2.append(player_2)
        if konfet == 0:
            print(f'Победа Игрока № 2', sum(win_2))
        player_1 = int(input('Игрок 1 введите значение\n'))
        while player_1 > 28:
            player_1 = int(input('Игрок 1 введите значение\n'))
        konfet = konfet - player_1
        print(konfet)
        win_1.append(player_1)
        if konfet == 0:
            print(f'Победа Игрока № 1,', sum(win_2))


print(win_1, win_2)
