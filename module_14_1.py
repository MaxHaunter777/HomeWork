import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
for i in range(10):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i+1}', f'example{i+1}@gmail.com', f'{(i+1)*10}', '1000'))

for i in range(10):
    if (i+1)%2 != 0:
        cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, f'{i+1}'))

i = range(1, 11)
n = i[::3]
for i in n:
    cursor.execute('DELETE from users WHERE id = ?', (f'{i}',))

cursor.execute('SELECT * FROM Users')
cursor.execute('SELECT username, email, age, balance from users WHERE age != ?', (60,))
users = cursor.fetchall()
for user in users:
    print(user)


connection.commit()
connection.close()