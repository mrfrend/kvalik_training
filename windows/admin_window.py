from interfaces.admin import Ui_Form
from PyQt6.QtWidgets import QWidget, QTableWidgetItem
from database.db import get_reservations

class AdminWindow(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_reservations()
    def load_reservations(self):
        data = get_reservations()
        self.tableWidget.setRowCount(len(data))
        for row_idx, row in enumerate(data):
            for col_idx, (col, value) in enumerate(row.items()): # [(0, ("id", 1)) (1, (number, 101))]
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        