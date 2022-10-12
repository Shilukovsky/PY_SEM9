a = [0] * 3
for i in range(3):
    a[i] = [0] * 3
    ind = 1
for i in range(3):
    for j in range(3):
        a[i][j] = f'|{ind}|'
        ind += 1

def print_board(x):

    for i in range(3):
        print(x[i])

def input_x_o(player, x):
    num = (input('введите номер поля: '))
    if num.isdigit():
        num = int(num)
        if num < 1 or num > 9:
            print('введите число от 1 до 9')
            input_x_o(player, x)
        if player == 1:
            temp = '|X|'
        else:
            temp = '|O|'
        if num < 4:
            if x[0][num - 1] == '|X|' or x[0][num - 1] == '|O|':
                print(f'ячейка {num} уже занята, введите другое число')
                input_x_o(player, x)
            else:
                x[0][num - 1] = temp
        elif num > 3 and num < 7:
            if x[1][num - 4] == '|X|' or x[1][num - 4] == '|O|':
                    print(f'ячейка {num} уже занята, введите другое число')
                    input_x_o(player, x)
            else:
                    x[1][num - 4] = temp
        elif num > 6 and num < 10:
            if x[2][num - 7] == '|X|' or x[2][num - 7] == '|O|':
                print(f'ячейка {num} уже занята, введите другое число')
                input_x_o(player, x)
            else:
                x[2][num - 7] = temp
        return x
    else:
        print('введите число от 1 до 9')
        input_x_o(player, x)

def win(x):
    for i in range(len(x)):
        if x[i][0] == x[i][1] == x[i][2]:
            return True
        if x[0][i] == x[1][i] == x[2][i]:
            return True
    if x[0][0] == x[1][1] == x[2][2]:
        return True
    if x[0][2] == x[1][1] == x[2][0]:
        return True
    else:
        return False

def game(x):
    count = 1
    n = 1
    while count <= 9:
        print_board(x)
        if count % 2 !=0:
            n = 1
            print('ходит "Х"')
            input_x_o(n, x)
            if win(x):
                print('победил "Х"')
                print_board(x)
                break
        else:
            n = 2
            print('ходит "O"')
            input_x_o(n, x)
            if win(x):
                print('победил "O"')
                print_board(x)
                break
        if count == 9:
            print('ничья')
            print_board(x)
        count += 1


game(a)