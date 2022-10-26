from choice import previev_base
from choice import add_record
from choice import delete_record
from choice import find_record


def input_choice(db, cursor):
    while True:
        user_choice = input(
            '1 - посмотреть базу, 2 - добавить запись, 3 - удалить запись, 4 - найти по Ф.И.О:, q - выход:')
        if user_choice == "1":
            previev_base()
        elif user_choice == "2":
            add_record()
        elif user_choice == "3":
            delete_record()
        elif user_choice == "4":
            find_record()
        elif user_choice == "q":
            print('Выход')
            break
        else:
            print('Не верно введен режим работы')
