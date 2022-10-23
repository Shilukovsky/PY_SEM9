def previev_base():
    for i in cursor.execute('SELECT * FROM personal'):
        print(*i)

def add_record():
    info = []
    id = input('Введите номер: ')
    info.append(id)
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    position = input('Введите должность: ')
    info.append(position)
    salary = ''
    valid = False
    while not valid:
        try:
            salary = input('Введите зарплату: ')
            if len(salary) < 0:
                print('Не может быть такой зарплаты.')
            else:
                salary = int(salary)
                valid = True
        except:
            print('Зарплата должна состоять только из цифр.')
    info.append(salary)
    bonus = ''
    valid = False
    while not valid:
        try:
            bonus = input('Введите премию: ')
            if len(bonus) <= 0:
                print('Не может быть такой премии.')
            else:
                bonus = int(bonus)
                valid = True
        except:
            print('Премия должна состоять только из цифр.')
    info.append(bonus)
    return info

def find_record(column, nam):
    cursor.execute(f'select * from personal WHERE {column} LIKE {nam};')
    one = cursor.fetchmany()
    return one

def delete_record():
    cursor.execute(f'DELETE from personal WHERE id={id}')
    bd.commit()
