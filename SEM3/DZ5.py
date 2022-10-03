k = int(input('Введите натуральное число, большее 2: '))

while k < 2:
    if k < 2:
        print('Ошибка ввода!')
fib = [-1, 1, 0, 1, 1]
for i in range(3, k+1):
    fib.append(fib[-2] + fib[-1])
    fib.insert(0, fib[1] - fib[0])
print(fib)