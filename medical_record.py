from typing import List
from lab_order import LabOrder


class MedicalRecord:
    """
    Medical record for a specific visit: diagnosis, notes, vitals, attachments, and lab orders.
    """

    def __init__(self, diagnosis: str, visit_notes: str, vitals: str):
        self.__diagnosis = (diagnosis or "").strip()
        self.__visit_notes = (visit_notes or "").strip()
        self.__vitals = (vitals or "").strip()
        self.__attachments: List[str] = []
        self.__lab_orders: List[LabOrder] = []

    def add_attachment(self, path_or_id: str) -> None:
        a = (path_or_id or "").strip()
        if a:
            self.__attachments.append(a)

    def order_lab_test(self, lab_order: LabOrder) -> None:
        if not isinstance(lab_order, LabOrder):
            raise TypeError("lab_order must be LabOrder.")
        self.__lab_orders.append(lab_order)

    # Getters/Setters
    def get_diagnosis(self) -> str:
        return self.__diagnosis

    def set_diagnosis(self, diagnosis: str) -> None:
        self.__diagnosis = (diagnosis or "").strip()

    def get_visit_notes(self) -> str:
        return self.__visit_notes

    def set_visit_notes(self, notes: str) -> None:
        self.__visit_notes = (notes or "").strip()

    def get_vitals(self) -> str:
        return self.__vitals

    def set_vitals(self, vitals: str) -> None:
        self.__vitals = (vitals or "").strip()

    def get_attachments(self) -> list:
        return list(self.__attachments)

    def get_lab_orders(self) -> list:
        return list(self.__lab_orders)

    def __str__(self) -> str:
        return (f"MedicalRecord(diagnosis={self.__diagnosis}, vitals={self.__vitals}, "
                f"attachments={len(self.__attachments)}, lab_orders={len(self.__lab_orders)})")
