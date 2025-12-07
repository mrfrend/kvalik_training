from dataclasses import dataclass

from PyQt6.QtCore import QDate

@dataclass
class Reservation:
    reservation_id: int
    room_number: int
    category_name: str
    status_name: str
    fio: str
    check_in_date: QDate
    check_out_date: QDate