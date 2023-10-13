import sqlite3
import bcrypt
from PyQt5.QtWidgets import QMessageBox

conn = sqlite3.connect('messenger.db')
cursor = conn.cursor()

def register_user(email, password, nickname):
    cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
    existing_user = cursor.fetchone()
    if existing_user:
        QMessageBox.critical(None, "Ошибка", "Пользователь с таким email уже существует.")
    else:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute('INSERT INTO users (email, password, nickname) VALUES (?, ?, ?)', (email, hashed_password, nickname))
        conn.commit()
        QMessageBox.information(None, "Успешно", "Пользователь успешно зарегистрирован.")

def authenticate_user(email, password):
    cursor.execute('SELECT password, nickname FROM users WHERE email = ?', (email,))
    row = cursor.fetchone()
    if row:
        stored_password, nickname = row[0], row[1]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            QMessageBox.information(None, "Успешно", "Вход выполнен успешно.")
            return nickname
        else:
            QMessageBox.critical(None, "Ошибка", "Неверный пароль.")
    else:
        QMessageBox.critical(None, "Ошибка", "Пользователь не найден.")


conn.close()