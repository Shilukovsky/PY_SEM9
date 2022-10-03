a = [2, 3, 4, 5, 6]
comp = []
import math
for i in range(math.ceil(len(a) / 2)):
    compos = 1
    x = a[i]
    y = a[i-(1+2*i)]
    comp.append(x*y)
print(f'{a} -> {comp}  ')


