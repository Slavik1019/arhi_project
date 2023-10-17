#Проведем тесты части приложения
#Авторизация и регистрация: Тестирование, чтобы убедиться, что пользовательские данные правильно сохраняются в базе данных и пользователи могут авторизовываться.
#Смена текущего пользователя в чате: Тестирование переключения между пользователями и правильного обновления окна чата.
import pytest
from pytestqt import qtbot
from registration_and_authentication import AuthWindow, RegistrationForm, authenticate_user
from database import create_connection
from messenger import MessengerApp

# Тестирование авторизации
@pytest.mark.parametrize("email, password, expected_message", [
    ('', '', 'Введите Email и пароль'),
    ('nonexistent@example.com', 'wrongpassword', 'Аутентификация не удалась'),
    ('test@example.com', 'hashedpassword', None),
])
def test_authentication(qtbot, email, password, expected_message):
    auth_window = AuthWindow()

    assert auth_window.title() == 'Добро пожаловать в чат, авторизуйтесь'
    assert auth_window.email_input.placeholderText() == 'Email'
    assert auth_window.password_input.placeholderText() == 'Пароль'
    assert auth_window.login_button.text() == 'Войти'
    assert auth_window.register_button.text() == 'Зарегистрироваться'

    auth_window.email_input.setText(email)
    auth_window.password_input.setText(password)

    with qtbot.waitSignal(auth_window.messageClicked):
        auth_window.login_button.click()

    if expected_message:
        assert expected_message in auth_window.messageClicked.text()
    else:
        assert isinstance(auth_window.messenger, MessengerApp)

    auth_window.close()

# Тестирование регистрации
@pytest.mark.parametrize("email, password, confirm_password, nickname, expected_message", [
    ('', '', '', '', 'Заполните все поля'),
    ('test@example.com', 'password1', 'password2', 'TestUser', 'Пароли не совпадают'),
    ('test@example.com', 'password', 'password', 'TestUser', 'Пользователь успешно зарегистрирован'),
])
def test_registration(qtbot, email, password, confirm_password, nickname, expected_message):
    registration_window = RegistrationForm()

    assert registration_window.title() == 'Регистрация'
    assert registration_window.email_input.placeholderText() == 'Email'
    assert registration_window.password_input.placeholderText() == 'Пароль'
    assert registration_window.confirm_password_input.placeholderText() == 'Повторите пароль'
    assert registration_window.nickname_input.placeholderText() == 'Никнейм'
    assert registration_window.register_button.text() == 'Зарегистрироваться'

    registration_window.email_input.setText(email)
    registration_window.password_input.setText(password)
    registration_window.confirm_password_input.setText(confirm_password)
    registration_window.nickname_input.setText(nickname)

    with qtbot.waitSignal(registration_window.messageClicked):
        registration_window.register_button.click()

    assert expected_message in registration_window.messageClicked.text()

    registration_window.close()

# Тестирование функции аутентификации пользователя
def test_authenticate_user():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (email, password, nickname) VALUES (?, ?, ?)", ('test@example.com', 'hashedpassword', 'TestUser'))
    conn.commit()
    conn.close()

    assert authenticate_user('test@example.com', 'hashedpassword') == 'TestUser'
    assert authenticate_user('test@example.com', 'wrongpassword') is None
    assert authenticate_user('nonexistent@example.com', 'password') is None

def test_clear_messages_on_user_switch(qtbot):
    # Создаем экземпляр приложения
    app = MessengerApp("user@example.com", "UserNickname")

    # Получаем доступ к виджетам приложения, включая список пользователей и окно сообщений
    user_list_widget = app.user_list_widget
    message_display_widget = app.message_display_widget

    # Добавляем сообщения в окно сообщений
    selected_user = user_list_widget.currentItem()
    if selected_user:
        user = selected_user.text()
        message_display_widget.chats[user] = ["UserNickname: Привет"]

    # Переключаем пользователя
    user_list_widget.setCurrentRow(0)

    # Проверяем, что окно сообщений очищено
    assert message_display_widget.chat_view.toPlainText() == ""

    app.close()
    

if __name__ == '__main__':
    pytest.main()