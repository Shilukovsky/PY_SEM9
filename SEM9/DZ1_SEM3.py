a = [4, 7, 9, 4, 3, 0]

b = []
for i in range(len(a)):
    if (i % 2) != 0:
        b.append(a[i])


def get_sum(b):
    sum = 0
    for i in b:
        sum += i
    return sum


summa = get_sum(b)
print(f'{a} -> на нечетных позициях элементы {b}, ответ: {summa}  ')