import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from login_form import Ui_MainWindow
from database import Database
from product_form import ProductForm


class LoginForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db = Database()

        self.loginButton.clicked.connect(self.on_login)
        self.guestButton.clicked.connect(self.on_guest)
        self.exitButton.clicked.connect(self.close)

    def on_login(self):
            login = self.loginEdit.text()
            password = self.passwordEdit.text()
            print(f"Попытка входа: {login} / {password}")

            if not login or not password:
                QMessageBox.warning(self, "Предупреждение", "Введите логин и пароль")
                return

            user = self.db.get_user(login, password)
            if user:
                print(f"Успешный вход: {user['full_name']} ({user['role']})")
                self.open_product_form(user)
            else:
                QMessageBox.critical(self, "Ошибка", "Неверный логин или пароль")

    def on_guest(self):
        print("Вход как гость")
        guest_user = {
                'id_user': 0,
                'role': 'Гость',
                'full_name': 'Гость',
                'login': '',
                'password': ''
        }
        self.open_product_form(guest_user)

    def open_product_form(self, user):
        self.hide()
        self.product_form = ProductForm(user, login_window=self)
        self.product_form.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginForm()
    window.show()
    sys.exit(app.exec_())
