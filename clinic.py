from typing import List
from department import Department
from patient import Patient


class Clinic:
    """
    Represents the clinic entity and its profile.
    """

    def __init__(self, name: str, address: str, contact: str, email: str):
        self.__name = name.strip()
        self.__address = address.strip()
        self.__contact = contact.strip()
        self.__email = email.strip()
        self.__departments: List[Department] = []
        self.__patients: List[Patient] = []

    # Department management
    def add_department(self, dept: Department) -> None:
        if not isinstance(dept, Department):
            raise TypeError("dept must be Department.")
        if dept not in self.__departments:
            self.__departments.append(dept)

    def get_departments(self) -> List[Department]:
        return list(self.__departments)

    # Patient registry
    def register_patient(self, patient: Patient) -> None:
        if not isinstance(patient, Patient):
            raise TypeError("patient must be Patient.")
        if patient not in self.__patients:
            self.__patients.append(patient)

    def get_patients(self) -> List[Patient]:
        return list(self.__patients)

    # Profile getters/setters
    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        if not name or not name.strip():
            raise ValueError("Clinic name cannot be empty.")
        self.__name = name.strip()

    def get_address(self) -> str:
        return self.__address

    def set_address(self, address: str) -> None:
        self.__address = (address or "").strip()

    def get_contact(self) -> str:
        return self.__contact

    def set_contact(self, contact: str) -> None:
        self.__contact = (contact or "").strip()

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str) -> None:
        self.__email = (email or "").strip()

    def __str__(self) -> str:
        return f"Clinic(name={self.__name}, departments={len(self.__departments)}, patients={len(self.__patients)})"
