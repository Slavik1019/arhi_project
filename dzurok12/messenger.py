import sqlite3
from PyQt5.QtWidgets import QApplication, QListWidget, QMainWindow, QSplitter, QTextBrowser, QVBoxLayout, QWidget, QPushButton, QLineEdit, QInputDialog
from PyQt5.QtCore import Qt
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(current_directory, "messenger.db")

def create_connection():
    conn = sqlite3.connect(database_path)
    return conn

def get_user_list():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT nickname FROM users')
    user_list = [row[0] for row in cursor.fetchall()]
    conn.close()
    return user_list

def update_nickname_in_db(old_nickname, new_nickname):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET nickname = ? WHERE nickname = ?', (new_nickname, old_nickname))
    conn.commit()
    conn.close()

class UserListWidget(QListWidget):
    def __init__(self, message_display_widget):
        super().__init__()

        self.itemDoubleClicked.connect(self.change_nickname)
        self.chats = {}
        self.current_user = None

        user_list = get_user_list()
        self.addItems(user_list)

        self.message_display_widget = message_display_widget

    def update_chat(self, user, message):
        if user not in self.chats:
            self.chats[user] = []
        self.chats[user].append(message)

    def get_chat(self, user):
        return self.chats.get(user, [])

    def change_nickname(self, item):
        new_nickname, ok = QInputDialog.getText(self, "Change Nickname", "Enter a new nickname:")
        if ok and new_nickname:
            old_nickname = item.text()
            item.setText(new_nickname)
            update_nickname_in_db(old_nickname, new_nickname)

    def update_current_user_chat(self):
        selected_user = self.currentItem()
        if selected_user:
            user = selected_user.text()
            self.current_user = user
            self.message_display_widget.clear_chat_view()
            self.message_display_widget.update_chat_view(user, self.chats)

class MessageDisplayWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.chat_view = QTextBrowser()
        self.layout.addWidget(self.chat_view)
        self.setLayout(self.layout)
        self.chats = {}

    def update_chat_view(self, user, chats):
        chat_view = self.chat_view
        user_chats = chats.get(user, [])
        chat_view.clear() 
        chat_view.append("\n".join(user_chats))

class MessengerApp(QMainWindow):
    def __init__(self, user_email, user_nickname):
        super().__init__()
        self.initUI()
        self.user_email = user_email
        self.user_nickname = user_nickname
        self.chats = {} 
        self.current_user = None 
        self.setWindowTitle(f'Мессенджер ({user_nickname})')

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Мессенджер')

        splitter = QSplitter(Qt.Horizontal)

        self.message_display_widget = MessageDisplayWidget()
        self.user_list_widget = UserListWidget(self.message_display_widget)

        splitter.addWidget(self.user_list_widget)
        splitter.addWidget(self.message_display_widget)

        self.send_button = QPushButton('Send')
        self.input_box = QLineEdit()
        self.send_button.clicked.connect(self.send_message)
        self.input_box.returnPressed.connect(self.send_message)

        main_layout = QVBoxLayout()
        main_layout.addWidget(splitter)
        main_layout.addWidget(self.input_box)
        main_layout.addWidget(self.send_button)

        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        

        self.show()

    def send_message(self):
        selected_user = self.user_list_widget.currentItem()
        if selected_user:
            user = selected_user.text()
            message_text = self.input_box.text()

            if user not in self.chats:
                self.chats[user] = []
            self.chats[user].append(f"{self.user_nickname}: {message_text}")

            self.message_display_widget.update_chat_view(user, self.chats)

            self.input_box.clear()

    def update_chat_on_user_switch(self):
        selected_user = self.user_list_widget.currentItem()
        if selected_user:
            user = selected_user.text()
            self.current_user = user

            # Обновляем окно сообщений при переключении между пользователями
            self.message_display_widget.update_chat_view(user, self.chats)

def main():
    app = QApplication([])
    ex = MessengerApp("user@example.com", "UserNickname")
    
    ex.user_list_widget.itemClicked.connect(ex.update_chat_on_user_switch)
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication([])

    ex = MessengerApp("user@example.com", "UserNickname")

    ex.user_list_widget.itemClicked.connect(ex.update_chat_on_user_switch)

    sys.exit(app.exec_())