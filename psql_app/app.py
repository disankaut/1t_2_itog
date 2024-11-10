import psycopg2
from psycopg2 import sql


DB_HOST = "psql_container"
DB_PORT = "5432"
DB_NAME = "db_name"
DB_USER = "sysadmin"
DB_PASSWORD = "12345678"

def create_connection():
    """Создаёт подключение к базе данных PostgreSQL"""
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return connection
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

def create_table(connection):
    """Создаёт таблицу users в базе данных"""
    try:
        with connection.cursor() as cursor:
            # SQL-запрос для создания таблицы
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT NOT NULL
            );
            '''
            cursor.execute(create_table_query)
            connection.commit()
            print("Таблица 'users' успешно создана.")
    except Exception as e:
        print(f"Ошибка при создании таблицы: {e}")

def insert_data(connection):
    """Наполняет таблицу данными"""
    try:
        with connection.cursor() as cursor:
            # SQL-запрос для вставки данных
            insert_query = '''
            INSERT INTO users (name, age)
            VALUES (%s, %s)
            '''
            # Пример данных для вставки
            data = [
                ('Alice', 30),
                ('Bob', 25),
                ('Charlie', 35)
            ]
            cursor.executemany(insert_query, data)
            connection.commit()
            print("Данные успешно добавлены в таблицу.")
    except Exception as e:
        print(f"Ошибка при вставке данных: {e}")

def fetch_data(connection):
    """Выводит данные из таблицы"""
    try:
        with connection.cursor() as cursor:
            # SQL-запрос для выборки всех данных из таблицы
            select_query = 'SELECT * FROM users;'
            cursor.execute(select_query)
            rows = cursor.fetchall()
            print("Данные из таблицы 'users':")
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")

def main():
    """Основная функция выполнения всех шагов"""
    connection = create_connection()
    if connection:
        create_table(connection)
        insert_data(connection)
        fetch_data(connection)
        connection.close()

if __name__ == "__main__":
    main()
