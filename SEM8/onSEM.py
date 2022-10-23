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

baza = [(1,"Иван", "Иванов", "главный инженер", 50000, 10000),
        (2,"Игорь", "Петров", "инженер", 20000, 8000),
        (3,"Олег", "Семенов", "завхоз", 12000, 3000)]

try:
    cursor.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?)', baza)
    bd.commit()
except:
    print('Данные уже есть')

for i in cursor.execute('SELECT * FROM personal'):
    print(*i)
#
# cursor.execute('select * from personal WHERE name LIKE "Олег";')
# one = cursor.fetchmany()
# print(*one)
#
# # cursor.execute('select * from personal WHERE id=2;')
# # one = cursor.fetchmany()
# # print(*one)
#
# cursor.execute('DELETE from personal WHERE id=1')
# bd.commit()
# def previev_base():
#     pass
#
# def add_record():
#     info = []
#     id = input('Введите номер: ')
#     info.append(id)
#     last_name = input('Введите фамилию: ')
#     info.append(last_name)
#     first_name = input('Введите имя: ')
#     info.append(first_name)
#     position = input('Введите должность: ')
#     info.append(position)
#     salary = ''
#     valid = False
#     while not valid:
#         try:
#             salary = input('Введите зарплату: ')
#             if len(salary) < 0:
#                 print('Не может быть такой зарплаты.')
#             else:
#                 salary = int(salary)
#                 valid = True
#         except:
#             print('Зарплата должна состоять только из цифр.')
#     info.append(salary)
#     bonus = ''
#     valid = False
#     while not valid:
#         try:
#             bonus = input('Введите премию: ')
#             if len(bonus) <= 0:
#                 print('Не может быть такой премии.')
#             else:
#                 bonus = int(bonus)
#                 valid = True
#         except:
#             print('Премия должна состоять только из цифр.')
#     info.append(bonus)
#     return info
#
# def find_record(column, nam):
#     cursor.execute(f'select * from personal WHERE {column} LIKE {nam};')
#     one = cursor.fetchmany()
#     return one
#
# def delete_record():
#     cursor.execute(f'DELETE from personal WHERE id={id}')
#     bd.commit()
#
# for i in cursor.execute('SELECT * FROM personal'):
#     print(*i)
#
# def input_choice():
#     while True:
#         user_choice = input('1 - посмотреть базу, 2 - добавить запись, 3 - удалить запись, 4 - найти по Ф.И.О:, q - выход:')
#         if user_choice == "1":
#             previev_base()
#         elif user_choice == "2":
#             add_record()
#         elif user_choice == "3":
#             delete_record()
#         elif user_choice == "4":
#             find_record()
#         elif user_choice == "q":
#             print('Выход')
#             break
#         else:
#             print('Не верно введен режим работы')
#
# cursor.execute('SELECT * FROM personal')
#
# input_choice()
#
