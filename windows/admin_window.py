from interfaces.admin import Ui_Form
from PyQt6.QtWidgets import QTableWidget, QWidget, QTableWidgetItem, QMessageBox
from PyQt6.QtCore import QDate, Qt
from database.db import *
from dto.reservation import Reservation
from dialogs.edit_reservation_dialog import EditReservationDialog

class AdminWindow(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_reservations()
        self.load_clients()
        self.set_tabs_names()
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.tableWidget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tableWidget.cellDoubleClicked.connect(self.on_cell_double_clicked)

        self.filter_button.clicked.connect(self.on_button_click)
        self.reset_filter_button.clicked.connect(self.on_reset_filter_click)
        self.add_client_button.clicked.connect(self.add_client)
    
    def set_tabs_names(self):
        self.tabWidget.setTabText(0, "Бронирования")
        self.tabWidget.setTabText(1, "Клиенты")
        self.tabWidget.setTabText(2, "Номера")
    
    def on_cell_double_clicked(self, row_idx: int, column_idx: int):
        row_data = []
        for col_idx in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row_idx, col_idx)
            row_data.append(item.text())
        row_data[0] = int(row_data[0])
        reservation_id: int = self.tableWidget.item(row_idx, 0).data(Qt.ItemDataRole.UserRole)
        row_data[4] = QDate.fromString(row_data[4], "yyyy-MM-dd")
        row_data[5] = QDate.fromString(row_data[5], "yyyy-MM-dd")

        reservation = Reservation(reservation_id, *row_data) # row_data[0], row_data[1].. row_data[5]
        self.edit_dialog = EditReservationDialog(reservation)
        self.edit_dialog.updated.connect(self.update_reservations)
        self.edit_dialog.show()
        
    
    # Методы для окна бронирования
    def on_reset_filter_click(self):
        self.check_in_date.setDate(QDate.currentDate())
        self.check_out_date.setDate(QDate.currentDate().addDays(1))
        for row_index in range(self.tableWidget.rowCount()): # (0, 1, 2, 3, 4)
            self.tableWidget.setRowHidden(row_index, False)
    
    def on_button_click(self):
        check_in_date = self.check_in_date.date()
        check_out_date = self.check_out_date.date()

        if check_in_date < check_out_date:
            self.filter_reservation(check_in_date, check_out_date)
        
            
    def filter_reservation(self, check_in_date: QDate, check_out_date: QDate):
        for row_number in range(self.tableWidget.rowCount()):
            check_in_date_item = self.tableWidget.item(row_number, 4)
            compare_date = QDate.fromString(check_in_date_item.text(), "yyyy-MM-dd")

            if check_in_date <= compare_date <= check_out_date:
                self.tableWidget.setRowHidden(row_number, False)
            else:
                self.tableWidget.setRowHidden(row_number, True)

    def update_reservations(self):
        self.tableWidget.setRowCount(0)
        self.load_reservations()
    def load_reservations(self):
        data = get_reservations()
        self.tableWidget.setRowCount(len(data))
        column_order = ["number", "category_name", "status_name", "fio", "check_in", "check_out"]

        for row_idx, row in enumerate(data):
            for col_idx, key in enumerate(column_order):
                value = row.get(key, "")
                item = QTableWidgetItem(str(value))
                if col_idx == 0:
                    item.setData(Qt.ItemDataRole.UserRole, row["id"])
                self.tableWidget.setItem(row_idx, col_idx, item)
                
                
    
    # Методы для окна клиентов
    def load_clients(self):
        data = get_clients_info()
        self.client_table.setRowCount(len(data))
        for row_idx, row in enumerate(data):
            for col_idx, (col, value) in enumerate(row.items()):
                self.client_table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
    def add_client(self):
        first_name = self.name_edit.text() # None, 0, "" == False
        last_name = self.last_name_edit.text()
        middle_name = self.middle_name_edit.text() # Может быть пустым
        passport_series = self.passport_series_spinbox.value()
        passport_number = self.passport_number_spinbox.value()
        cause_visit = self.cause_visit_edit.text()

        if all([first_name, last_name, passport_series, passport_number, cause_visit]):
            add_new_client(first_name, last_name, middle_name, passport_series, passport_number, cause_visit)
            QMessageBox.information(self, "Успех", "Новый клиент добавлен в базу")
            # Обновить таблицу
            self.client_table.setRowCount(0)
            self.load_clients()
        else:
            QMessageBox.warning(self, "Пустые поля", "Найдены пустые поля (за исключением отчества). Введите недостающие данные.")

        





