from turtle import update

import pymysql
from interfaces.edit_reservation_dialog import Ui_Dialog
from database.db import get_fio_clients, get_room_statuses, get_categories, get_room_numbers, update_reservation
from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import pyqtSignal
from dto.reservation import Reservation

class EditReservationDialog(QDialog, Ui_Dialog):
    updated = pyqtSignal()

    def __init__(self, reservation: Reservation):
        super().__init__()
        self.reservation = reservation
        self.setupUi(self)
        self.load_comboboxes()
        self.set_data()
        self.pushButton.clicked.connect(self.on_update_click)
    
    def on_update_click(self):
        client_id: int = self.client_box.currentData()
        room_id: int = self.room_number_box.currentData()
        check_in_date: str = self.check_in_date_edit.date().toString("yyyy-MM-dd")
        check_out_date: str = self.check_out_date_edit.date().toString("yyyy-MM-dd")

        try:
            update_reservation(self.reservation.reservation_id, room_id, client_id, check_in_date, check_out_date)
            self.updated.emit()
            QMessageBox.information(self, "Успех", "Данные обновлены")
        except pymysql.ProgrammingError:
            QMessageBox.warning(self, "Ошибка", "Не удалось обновить данные")
    
    def load_comboboxes(self):
        fio_clients = get_fio_clients()
        room_statuses = get_room_statuses()
        categories = get_categories()
        room_numbers = get_room_numbers()

        # print(fio_clients)

        for client in fio_clients:
            self.client_box.addItem(client["fio"], client["id"])
        
        for room_status in room_statuses:
            self.room_status_box.addItem(room_status["status_name"], room_status["id"])
        
        for category in categories:
            self.room_type_box.addItem(category["category_name"], category["id"])
        
        for room_number in room_numbers:
            self.room_number_box.addItem(str(room_number["number"]), room_number["id"])

        

        
    def set_data(self):
        self.room_number_box.setCurrentIndex(self.room_number_box.findText(str(self.reservation.room_number)))
        self.room_status_box.setCurrentIndex(self.room_status_box.findText(self.reservation.status_name))
        self.room_type_box.setCurrentIndex(self.room_type_box.findText(self.reservation.category_name))
        self.client_box.setCurrentIndex(self.client_box.findText(self.reservation.fio))
    
