n = int(input("Введите число: "))
i = 2
my_list = []
print(f"Простые множители числа {n} приведены в списке:")
while i <= n:
    if n % i == 0:
        my_list.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(my_list)