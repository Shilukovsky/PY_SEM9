def write_file(name,st):
    with open(name, 'w') as data:
        data.write(st)

def create_str(sp):
    list= sp[::-1]
    wr = ''
    if len(list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                wr += f'{list[i]}x^{len(list)-i-1}'
                if list[i+1] != 0 or list[i+2] != 0:
                    wr += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                wr += f'{list[i]}x'
                if list[i+1] != 0 or list[i+2] != 0:
                    wr += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                wr += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                wr += ' = 0'
    return wr

def sq_polinom(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i + 1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num



def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num



def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    list = []
    l = len(st)
    k = 0
    if sq_polinom(st[-1]) == -1:
        list.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1
    ii = l - 1
    while ii >= 0:
        if sq_polinom(st[ii]) != -1 and sq_polinom(st[ii]) == i:
            list.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            list.append(0)
            i += 1

    return list

with open('fileDZ5_1.txt', 'r') as data:
    st1 = data.readlines()
with open('fileDZ5_2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
list1 = calc_mn(st1)
list2 = calc_mn(st2)
ll = len(list1)
if len(list1) > len(list2):
    ll = len(list2)
list_new = [list1[i] + list2[i] for i in range(ll)]
if len(list1) > len(list2):
    mm = len(list1)
    for i in range(ll, mm):
        list_new.append(list1[i])
else:
    mm = len(list2)
    for i in range(ll, mm):
        list_new.append(list2[i])
write_file("fileDZ5.txt", create_str(list_new))
with open('fileDZ5.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")

