from windows.auth_window import AuthWindow
from PyQt6.QtWidgets import QApplication

app = QApplication([])
window = AuthWindow()
window.show()
app.exec()