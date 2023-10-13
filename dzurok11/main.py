import sys
from PyQt5.QtWidgets import QApplication
from registration_and_authentication import AuthWindow

def main():
    app = QApplication(sys.argv)
    auth_window = AuthWindow()
    auth_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()