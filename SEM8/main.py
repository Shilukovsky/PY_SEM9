from User_interface import input_choice
input_choice()

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






