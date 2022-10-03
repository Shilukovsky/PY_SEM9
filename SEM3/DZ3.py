a = [1.1, 1.2, 3.1, 5, 10.01]
min = max = a[0] % 1

for i in range(len(a)):
    if a[i] % 1 < min:
        min = a[i] % 1
    elif a[i] % 1 > max:
        max = a[i] % 1
    else:
        continue

print(f'- {a} => {round(max - min, 100)};')