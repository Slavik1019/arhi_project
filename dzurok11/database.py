import sqlite3
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

database_path = os.path.join(current_directory, "messenger.db")

def create_connection():
    conn = sqlite3.connect(database_path)
    return conn

# Функция для получения списка пользователей из базы данных
def get_user_list():
    # Устанавливаем соединение с базой данных
    conn = create_connection()
    cursor = conn.cursor()

    # Выполняем SQL-запрос для выборки пользователей из таблицы 'users'
    cursor.execute('SELECT nickname FROM users')

    # Извлекаем результаты запроса
    user_list = [row[0] for row in cursor.fetchall()]

    # Закрываем соединение с базой данных
    conn.close()

    return user_list

def execute_query(query, params=()):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()