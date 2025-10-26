from typing import Optional


class Person:
    """
    Base class for people in the clinic.
    """

    def __init__(self, name: str, contact: str, email: str):
        self.__name = name.strip()
        self.__contact = contact.strip()
        self.__email = email.strip()

    # Getters / Setters
    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        if not name or not name.strip():
            raise ValueError("Name cannot be empty.")
        self.__name = name.strip()

    def get_contact(self) -> str:
        return self.__contact

    def set_contact(self, contact: str) -> None:
        self.__contact = (contact or "").strip()

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str) -> None:
        self.__email = (email or "").strip()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name={self.__name}, contact={self.__contact}, email={self.__email})"
