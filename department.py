from typing import List
from doctor import Doctor


class Department:
    """
    Department under a clinic, e.g., General Practice, Cardiology.
    """

    def __init__(self, name: str, operating_hours: str):
        self.__name = name.strip()
        self.__operating_hours = operating_hours.strip()
        self.__staff: List[Doctor] = []

    def add_staff(self, staff: Doctor) -> None:
        if not isinstance(staff, Doctor):
            raise TypeError("staff must be Doctor.")
        if staff not in self.__staff:
            self.__staff.append(staff)

    def get_staff(self) -> list:
        return list(self.__staff)

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        if not name or not name.strip():
            raise ValueError("Department name cannot be empty.")
        self.__name = name.strip()

    def get_operating_hours(self) -> str:
        return self.__operating_hours

    def set_operating_hours(self, hours: str) -> None:
        self.__operating_hours = (hours or "").strip()

    def __str__(self) -> str:
        return f"Department(name={self.__name}, staff={len(self.__staff)}, hours={self.__operating_hours})"
