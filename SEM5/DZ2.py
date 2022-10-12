from random import *
import os
text = ('на столе 2021 конфета, вы берете их поочереди,\n'
'за один раз можно взять не больше 28 конфет.\n'
'Выигрывает тот, кто сделает последний ход\n')
print(text)




def with_player():
    candies = 2021
    max = 28
    count = 0
    player_1 = input('введи имя первого игрока: ')
    player_2 = input('введи имя второго игрока: ')
    x = randint(1, 2)
    if x == 1:
        print(f'{player_1} ходит первый')

        a = player_1
        b = player_2
    else:
        print(f'{player_2} ходит первый')

        a = player_2
        b = player_1
    while candies > 0:
        if count == 0:
            step = int(input(f'\nходит {a} = '))
            while step > candies or step > max:
                step = int(input(f'\nможно взять не больше {max} конфет {a}, попробуй еще раз: '))
            candies = candies - step
        if candies > 0:
            print(f'\nосталось {candies} конфет')
            count = 1
        else:
            print('конфеты кончились')

        if count == 1:
            step = int(input(f'\nходит {b} '))
            while step > candies or step > max:
                step = int(input(f'\nможно взять не больше {max} конфет {b}, попробуй еще раз: '))
            candies = candies - step
        if candies > 0:
            print(f'\nосталось {candies} конфет')
            count = 0
        else:
            print('конфеты кончились')

    if count == 0:
        print(f'{a} ПОБЕДИЛ')
    if count == 1:
        print(f'{b} ПОБЕДИЛ')


# with_player()


def with_bot():
    candies = 2021
    max = 28
    count = 0
    player_1 = input('введи имя игрока: ')
    player_2 = 'Компьютер'
    players = [player_1, player_2]
    x = randint(-1, 0)

    print(f'{players[x + 1]} ходит первый')

    while candies > 0:
        x += 1
        if players[x % 2] == 'Компьютер':
            print(f'\nХод {players[x % 2]} \nосталось {candies} конфет. \nкомпьютер берет: ')

            if candies < 29:
                step = candies
            else:
                dev = candies // 28
                step = candies - ((dev * max) + 1)
                if step ==  -1:
                    step = max - 1
                if step == 0:
                    step = max
            while step > 28 or step < 1:
                step = randint(1, 28)
            print(step)
        else:
            step = int(input(f'\nход {players[x % 2]} \nосталось {candies}:  '))
            while step > max or step > candies:
                step = int(input(f'\nможно взять не больше {max} конфет, попробуй еще раз: '))
        candies = candies - step

    print(f'осталось {candies} \nПобедил {players[x % 2]}')

with_bot()
