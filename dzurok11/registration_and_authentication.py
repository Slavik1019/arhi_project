import bcrypt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from messenger import MessengerApp
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from database import create_connection, execute_query

class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Добро пожаловать в чат, авторизуйтесь')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        # Заголовок
        title_label = QLabel("Добро пожаловать в чат, авторизуйтесь!")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Стили для виджетов
        style = "QLineEdit { border: 2px solid #2196F3; border-radius: 5px; padding: 5px; }"
        style += "QPushButton { background-color: #2196F3; color: white; border: none; border-radius: 5px; padding: 7px; }"

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet(style)
        layout.addWidget(self.email_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(style)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Войти")
        self.login_button.setStyleSheet(style)
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.register_button = QPushButton("Зарегистрироваться")
        self.register_button.setStyleSheet(style)
        self.register_button.clicked.connect(self.register)
        layout.addWidget(self.register_button)

        self.central_widget.setLayout(layout)

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        if not email or not password:
            QMessageBox.critical(self, "Ошибка", "Введите Email и пароль.")
        else:
            nickname = authenticate_user(email, password)
            if nickname:
                self.messenger = MessengerApp(email, nickname) 
                self.messenger.show()
                self.close()
            else:
                QMessageBox.critical(self, "Ошибка", "Аутентификация не удалась. Проверьте email и пароль.")

    

    def register(self):
        self.registration_window = RegistrationForm()
        self.registration_window.show()

    def open_main_window(self, email, nickname):
        messenger = MessengerApp(email, nickname)
        messenger.show()
        self.close()

class RegistrationForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 250)
        self.setWindowTitle('Регистрация')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        # Заголовок
        title_label = QLabel("Заполните все поля для регистрации!")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Стили для виджетов
        style = "QLineEdit { border: 2px solid #4CAF50; border-radius: 5px; padding: 5px; }"
        style += "QPushButton { background-color: #4CAF50; color: white; border: none; border-radius: 5px; padding: 7px; }"

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet(style)
        layout.addWidget(self.email_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(style)
        layout.addWidget(self.password_input)

        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Повторите пароль")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_input.setStyleSheet(style)
        layout.addWidget(self.confirm_password_input)

        self.nickname_input = QLineEdit()
        self.nickname_input.setPlaceholderText("Никнейм")
        self.nickname_input.setStyleSheet(style)
        layout.addWidget(self.nickname_input)

        self.register_button = QPushButton("Зарегистрироваться")
        self.register_button.setStyleSheet(style)
        self.register_button.clicked.connect(self.register)
        layout.addWidget(self.register_button)

        self.central_widget.setLayout(layout)

    def register(self):
        email = self.email_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        nickname = self.nickname_input.text()

        if not email or not password or not confirm_password or not nickname:
            QMessageBox.critical(self, "Ошибка", "Заполните все поля.")
        elif password != confirm_password:
            QMessageBox.critical(self, "Ошибка", "Пароли не совпадают.")
        else:
            if self.register_user(email, password, nickname):
                self.close()
            else:
                QMessageBox.critical(self, "Ошибка", "Регистрация не удалась. Пожалуйста, проверьте введенные данные.")

    def register_user(self, email, password, nickname):
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            QMessageBox.critical(self, "Ошибка", "Пользователь с таким email уже существует.")
            conn.close()
            return False
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            cursor.execute('INSERT INTO users (email, password, nickname) VALUES (?, ?, ?)', (email, hashed_password, nickname))
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Успешно", "Пользователь успешно зарегистрирован.")
            return True

def authenticate_user(email, password):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT email, password, nickname FROM users WHERE email = ?', (email,))
    user_data = cursor.fetchone()
    if user_data:
        stored_password, nickname = user_data[1], user_data[2]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            conn.close()            
            return nickname
        else:
            QMessageBox.critical(None, "Ошибка", "Неверный пароль.")
    else:
        QMessageBox.critical(None, "Ошибка", "Пользователь не найден.")
    conn.close()
    return None