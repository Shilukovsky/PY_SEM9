import random
k = int(input("Введите натуральную степень k = "))
def write_file(st):
    with open('fileDZ4.txt', 'w') as data:
        data.write(st)

def rnd():
    return random.randint(0, 101)

def create_polinom(a):
    list = [rnd() for i in range(a + 1)]
    return list

def create_str(sp):
    list = sp[::-1]
    wr = ''
    if len(list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                wr += f'{list[i]}x^{len(list) - i - 1}'
                if list[i + 1] != 0:
                    wr += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                wr += f'{list[i]}x'
                if list[i + 1] != 0:
                    wr += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                wr += f'{list[i]} = 0'
            elif i == len(lst) - 1 and list[i] == 0:
                wr += ' = 0'
    return wr

koef = create_polinom(k)
write_file(create_str(koef))