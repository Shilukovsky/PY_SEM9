a = input('введите число: ')

sum = 0
for i in a:
     if i != '.':
        sum += int(i)
print(f'{a} -> {sum}')

