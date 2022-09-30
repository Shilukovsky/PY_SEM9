n = int(input('Введите число: '))
compos = 1
for i in range(1, n+1):
    compos *= i
    print(compos, end=' ')