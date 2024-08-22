import sqlite3

def create_conn(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def add_product(cursor, title, price, quantity):
    try:
        cursor.execute('''
        INSERT INTO products (product_title, price, quantity)
        VALUES (?, ?, ?)
        ''', (title, price, quantity))
    except sqlite3.Error as e:
        print(f"Error adding product: {e}")

def update_quantity(cursor, product_id, new_quantity):
    try:
        cursor.execute('''
        UPDATE products
        SET quantity = ?
        WHERE id = ?
        ''', (new_quantity, product_id))
    except sqlite3.Error as e:
        print(f"Error updating quantity: {e}")

def update_price(cursor, product_id, new_price):
    try:
        cursor.execute('''
        UPDATE products
        SET price = ?
        WHERE id = ?
        ''', (new_price, product_id))
    except sqlite3.Error as e:
        print(f"Error updating price: {e}")

def delete_product(cursor, product_id):
    try:
        cursor.execute('''
        DELETE FROM products
        WHERE id = ?
        ''', (product_id,))
    except sqlite3.Error as e:
        print(f"Error deleting product: {e}")

def print_all_products(cursor):
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def find_products_by_price_and_quantity(cursor, price_limit, quantity_limit):
    cursor.execute('''
    SELECT * FROM products
    WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def search_products_by_title(cursor, search_term):
    cursor.execute('''
    SELECT * FROM products
    WHERE product_title LIKE ?
    ''', ('%' + search_term + '%',))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    db_name = "hw.db"

    sql_table_products = '''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT(200) NOT NULL,
        price NUMERIC(10,2) NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
    '''

    conn = create_conn(db_name)
    if conn is not None:
        print("Connected to database")
        create_table(conn, sql_table_products)

        cursor = conn.cursor()
        add_product(cursor, "apple", 30, 98)
        add_product(cursor, "banana", 50, 67)
        add_product(cursor, "mango", 50, 37)
        add_product(cursor, "orange", 40, 89)
        add_product(cursor, "strawberry", 90, 76)
        add_product(cursor, "pineapple", 185, 100)
        add_product(cursor, "dragon fruit", 250, 30)
        add_product(cursor, "plum", 160, 90)
        add_product(cursor, "cherry", 78, 99)
        add_product(cursor, "watermelon", 78, 60)
        add_product(cursor, "grapes", 70, 80)
        add_product(cursor, "lemon", 50, 100)
        add_product(cursor, "kiwi", 89, 78)
        add_product(cursor, "pear", 45, 67)
        add_product(cursor, "apricot", 30, 37)

        conn.commit()
        conn.close()
    else:
        print("Error connecting to database")

if __name__ == "__main__":
    main()