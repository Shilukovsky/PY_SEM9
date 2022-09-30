n = int(input('Введите число: '))

def seq(n):
    return [round((1 + 1 / i) ** i, 4) for i in range(1, n + 1)]


print(seq(n))
print(round(sum(seq(n)), 4))
