
def create_db():
    import sqlite3
    bd = sqlite3.connect("Data_base.db")
    cursor = bd.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS personal(
        id INTEGER PRIMARY KEY autoincrement,
        name TEXT,
        last_name TEXT,
        position TEXT,
        salary INT,
        bonus INT
    )''')
    bd.commit()
    return bd, cursor


def previev_base(cursor):
    cursor.execute('SELECT * FROM personal')
    result = cursor.fetchall()
    for i in result:
        print(i)


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


def find_record(cursor, column, nam):
    cursor.execute(f'select * from personal WHERE {column} LIKE {nam};')
    one = cursor.fetchmany()
    return one


def delete_record(cursor, bd):
    cursor.execute(f'DELETE from personal WHERE id={id}')
    bd.commit()
