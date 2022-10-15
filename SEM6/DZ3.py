a = input("Введите текст через пробел:\n")
print(a)
list = [i for i in a.split() if 'абв' not in i]
print(list)