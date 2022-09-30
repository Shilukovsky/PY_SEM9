n = int(input('Введите число: '))

def get_numbers(n):
    return [int(i) for i in range(-n, n + 1)]

positions = [1, 3, 6]

def get_composition(num, pos):
    comp = 1
    for i in pos:
        comp *= num[i]
    return comp


numbers = get_numbers(n)
print(numbers)
print(get_composition(numbers, positions))
