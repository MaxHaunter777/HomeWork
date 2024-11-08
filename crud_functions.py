import sqlite3

#Функции initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса.
# Эта таблица должна содержать следующие поля: id, title, description, price
def initiate_db():
    connection = sqlite3.connect('products_db.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()
# Функции initiate_db, которая создаёт таблицу Users, если она ещё не создана при помощи SQL запроса.
# Эта таблица должна содержать следующие поля: id, username, email, age, balance
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

#Функция get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
def get_all_products():
    connection = sqlite3.connect('products_db.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result
#
def add_products(product_title, product_description, product_price):
    connection = sqlite3.connect('products_db.db')
    cursor = connection.cursor()
    check_product = cursor.execute('SELECT * FROM Products WHERE title=? ', (product_title,))
    if check_product.fetchone() is None:
        cursor.execute(f' INSERT INTO Products (title,description,price ) VALUES(?, ?, ?)',
                        (f'{product_title}', f'{product_description}', f'{product_price}')
                        )
    connection.commit()
    connection.close()


#Данная функция должна добавлять в таблицу Users вашей БД запись с переданными данными.
#add_user(username, email, age), которая принимает: имя пользователя, почту и возраст.
# Баланс у новых пользователей всегда равен 1000. Для добавления записей в таблице используйте SQL запрос.
def add_user(username, email, age):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT * FROM Users WHERE username=? ', (username,))

    if check_user.fetchone() is None:
        cursor.execute(f' INSERT INTO Users (username,email,age,balance ) VALUES(?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', 1000))
        connection.commit()
        connection.close()

#is_included(username) принимает имя пользователя и возвращает True, если такой пользователь есть в таблице Users,
# в противном случае False. Для получения записей используйте SQL запрос.
def is_included(username):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    user = cursor.execute(f'SELECT username FROM Users WHERE username = ?', (username,)).fetchone()
    connection.commit()
    connection.close()
    if user is None:
        return False
    else:
        return True

initiate_db()

for i in range(1, 5):
    add_products(f'Продукт {i}', f'Описание {i}', f'{i*100}')

