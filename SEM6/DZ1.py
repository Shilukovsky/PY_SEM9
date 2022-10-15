a = map(int, '4 7 9 4 3 0'.split())

res = list(filter(lambda x: x % 2, a))
print(res)


def get_sum(b):
     sum = 0
     for i in b:
         sum += i
     return sum

summa = get_sum(res)
print(summa)
