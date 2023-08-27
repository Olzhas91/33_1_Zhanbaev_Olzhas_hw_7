import sqlite3

def create_connection(db_hw):
    conn = None
    try:
        conn = sqlite3.connect(db_hw)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_products(connection, products):
    sql = '''INSERT INTO products
    (product_titel, price, quantity)
    VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

# def add_products(connection):
#     products = [
#         ('Тонер стартовый', 1800, 10),
#         ('Тоенр панасоник', 1200, 5),
#         ('Бушинги', 50, 200),
#         ('Бушинги для IR', 80, 120),
#         ('Ракель 1010', 90, 12),
#         ('Ракель 1005', 90, 20),
#         ('Дозирующее лезвие 1010', 120, 15),
#         ('Дозирующее лезвие 1005', 120, 16),
#         ('Жесткий диск SSD 120gb', 980, 10),
#         ('Жесткий диск SSD 256gb', 1500, 8),
#         ('Жесткий диск HDD 500gb', 3200, 15),
#         ('Жесткий диск HDD 1000gb', 4800, 11),
#         ('Оперативная память 4 gb DDR3', 800, 8),
#         ('Оперативная память 4 gb DDR4', 1800, 4),
#         ('Оперативная память 4 gb DDR5', 2400, 4)
#     ]
#     connection.executemany('''
#     INSERT INTO products (product_titel, price, quantity)
#     VALUES (?, ?, ?)''', products)
#     connection.commit()
#
# def update_quantity(product_id, new_quantity):
#     connection.execute('''
#     UPDATE products SET quantity = ? WHERE id = ?''', (new_quantity, product_id))
#     connection.commit()
#
# def update_price(product_id, new_price):
#     connection.execute('''
#     UPDATE products SET price = ? WHERE id = ?''', (new_price, product_id))
#     connection.commit()
#
# def delete_product(product_id):
#     connection.execute('''
#     DELETE FROM products WHERE id = ?''', (product_id,))
#     connection.commit()

# def select_all_products():
#     cursor = connection.cursor()
#     cursor.execute('SELECT * FROM products')
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

# def select_cheap_products():
#     cursor = connection.cursor()
#     cursor.execute('SELECT * FROM products WHERE price < 100.0 AND quantity > 5')
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#
# def search_products_by_title(keyword):
#     cursor = connection.cursor()
#     cursor.execute('SELECT * FROM products WHERE product_titel LIKE ?',
#                        ('%' + keyword + '%',))
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

sql_to_created_products = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_titel VARCHAR (200) NOT NULL,
price FLOAT (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL

)

'''

connection = create_connection('''hw.db''')
if connection is not None:
    print('Seccessfully connected!')
    # create_table(connection, sql_to_created_products)
    # insert_products(connection, ('Фотовал 1010', 250, 20))
    # insert_products(connection, ('Коротрон 1010', 180, 10))
    # insert_products(connection, ('Тонер 5000', 1500, 8))
    # insert_products(connection, ('Тонер Самсунг', 2200, 5))
    # insert_products(connection, ('Тонер Пантум', 2500, 5))
    # insert_products(connection, ('Фотовал 1005', 250, 23))
    # insert_products(connection, ('Коротрон 1005', 250, 17))
    # insert_products(connection, ('Картридж 725', 1200, 4))
    # insert_products(connection, ('Картридж 2612', 1200, 7))
    # insert_products(connection, ('Чернила жидкие Эпсон', 200, 24))
    # insert_products(connection, ('Чернила жидкие Кэнон', 250, 36))
    # insert_products(connection, ('Термопленка 1010', 1200, 3))
    # insert_products(connection, ('Прижтимной вал 1010', 1200, 1))
    # insert_products(connection, ('Прижимной вал 1005', 1550, 2))
    # insert_products(connection, ('Термопленка 1005', 1670, 9))
    # add_products()
    # update_quantity(3, 20)
    # update_price(5, 1000)
    # delete_product(10)
    # select_all_products()
    # select_cheap_products()
    # search_products_by_title('Тонер')

    connection.close()