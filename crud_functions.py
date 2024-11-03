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


initiate_db()

for i in range(1, 5):
    add_products(f'Продукт {i}', f'Описание {i}', f'{i*100}')
