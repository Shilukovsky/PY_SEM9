a = input("Введите текст через пробел:\n")
print(a)
b = "абв"
list = [i for i in a.split() if b not in i]
print(list)