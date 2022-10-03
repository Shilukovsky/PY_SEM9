a = int(input('Введите натуральное число: '))
b = ''
while a != 0:
    b = str(a % 2) + b
    a //= 2
print(f'- {a} => {b}')
