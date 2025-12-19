from interfaces.authorisation import Ui_Form
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox
from database.db import login as db_login
from windows.admin_window import AdminWindow
from windows.client_window import ClientWindow


class AuthWindow(Ui_Form, QWidget):  # Наследование
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click_login)

    def on_click_login(self):
        user_login = self.login_edit.text().strip()
        password = self.password_edit.text().strip()
        account = db_login(user_login, password)

        if account is None:
            QMessageBox.warning(self, "Ошибка", "Такой аккаунт не существует")
            return
        QMessageBox.information(self, "Успех", "Успешно авторизовано!")
        type_account: int = account["type_account_id"]

        if type_account == 1:
            self.admin_window = AdminWindow()
            self.admin_window.show()
            self.close()
        elif type_account == 4:
            self.client_window = ClientWindow()
            self.client_window.show()
            self.close()

