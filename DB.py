import sqlite3

connection = sqlite3.connect('user.db')
cursor = connection.cursor()

create_table_query = """
    CREATE TABLE IF NOT EXISTS users(
        id integer primary key,
        first_name text,
        last_name text,
        phone_number text
    );
"""

cursor.execute(create_table_query)
connection.commit()
connection.close() 

sample_data_query = """
    INSERT INTO users (id, first_name, last_name, phone_number)
    VALUES (?, ?, ?, ?)
"""

sampel_data = [(6121, 'ali', 'sasa', '21212121'),
               (3121, 'ali', 'sasa', '21212121'),
               (4121, 'ali', 'sasa', '21212121'),
               (5121, 'ali', 'sasa', '21212121')]

# with sqlite3.connect('user.db') as connection:
#     cursor = connection.cursor()
#     cursor.executemany(sample_data_query, sampel_data)



fetch_data_query = """
    SELECT id, first_name, last_name, phone_number FROM users
"""
rows = []

with sqlite3.connect('user.db') as connection:
    cursor = connection.cursor()
    cursor.execute(fetch_data_query)
    rows = cursor.fetchall()

for row in rows:
    print(f"id={row[0]},first_name={row[1]}, last_name={row[2]}, phone_number={row[3]}")