from PyQt6.QtCore import QDate
from interfaces.client import Ui_Form
from PyQt6.QtWidgets import QMessageBox, QWidget, QApplication, QTableWidgetItem
from database.db import get_available_rooms

class ClientWindow(Ui_Form, QWidget): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Окно клиента")
        self.filter_button.clicked.connect(self.load_rooms)
        self.check_in_date.setMinimumDate(QDate.currentDate())
        self.check_out_date.setMinimumDate(QDate.currentDate())
    
    def load_rooms(self):
        check_in_date = self.check_in_date.date()
        check_out_date = self.check_out_date.date()

        if check_in_date >= check_out_date:
            QMessageBox.critical(self, "Невалидные даты", "Дата въезда должна быть строго раньше даты выезда.")
            return

        check_in_date = check_in_date.toString("yyyy-MM-dd")
        check_out_date = check_out_date.toString("yyyy-MM-dd")

        data = get_available_rooms(check_in_date, check_out_date)

        if len(data) == 0:
            QMessageBox.information(self, "Бронирования", "Свободных номеров на данный период нет")
            return

        self.tableWidget.setRowCount(len(data))

        for row_idx, row in enumerate(data):
            for col_idx, key in enumerate(row):
                value = row.get(key, "")
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row_idx, col_idx, item)

if __name__ == "__main__":
    app = QApplication([])
    window = ClientWindow()
    window.show()
    app.exec()