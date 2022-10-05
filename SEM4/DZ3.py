seq = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Исходный список: {seq}")
new_seq = []
[new_seq.append(i) for i in seq if i not in new_seq]
print(f"Список из неповторяющихся элементов: {new_seq}")