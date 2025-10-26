from typing import List
from person import Person

class Patient(Person):
    """
    Patient profile with insurance, allergies, and medical history pointers.
    """

    def __init__(self, name: str, contact: str, email: str, dob: str, address: str, insurance_details: str):
        super().__init__(name, contact, email)
        self.__dob = dob.strip()
        self.__address = address.strip()
        self.__insurance_details = insurance_details.strip()
        self.__allergies: List[str] = []
        self.__medical_history_summary: List[str] = []  # free-text summaries

    def get_dob(self) -> str:
        return self.__dob

    def set_dob(self, dob: str) -> None:
        self.__dob = (dob or "").strip()

    def get_address(self) -> str:
        return self.__address

    def set_address(self, address: str) -> None:
        self.__address = (address or "").strip()

    def get_insurance_details(self) -> str:
        return self.__insurance_details

    def set_insurance_details(self, details: str) -> None:
        self.__insurance_details = (details or "").strip()

    def add_allergy(self, allergy: str) -> None:
        a = (allergy or "").strip()
        if a and a not in self.__allergies:
            self.__allergies.append(a)

    def get_allergies(self) -> list:
        return list(self.__allergies)

    def add_history_note(self, note: str) -> None:
        n = (note or "").strip()
        if n:
            self.__medical_history_summary.append(n)

    def get_history_notes(self) -> list:
        return list(self.__medical_history_summary)

    def __str__(self) -> str:
        return (f"Patient(name={self.get_name()}, dob={self.__dob}, "
                f"insurance={self.__insurance_details}, allergies={len(self.__allergies)})")
