#Задача "Первые пользователи":

import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

#Создайте таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

#Заполните её 10 записями:
for i in range(10):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', 
                                    (f'User{i+1}', f'example{i+1}@gmail.com', f'{(i+1)*10}', '1000'))

#Обновите balance у каждой 2ой записи начиная с 1ой на 500:
for i in range(10):
    if (i+1)%2 != 0:
        cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, f'{i+1}'))

#Удалите каждую 3ую запись в таблице начиная с 1ой:
i = range(1, 11)
n = i[::3]
for i in n:
    cursor.execute('DELETE from users WHERE id = ?', (f'{i}',))

#Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль
cursor.execute('SELECT * FROM Users')
cursor.execute('SELECT username, email, age, balance from users WHERE age != ?', (60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')


connection.commit()
connection.close()
