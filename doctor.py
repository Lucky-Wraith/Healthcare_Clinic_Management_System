from person import Person

class Doctor(Person):
    """
    Doctor profile with specialty and availability.
    """

    def __init__(self, name: str, contact: str, email: str, specialty: str, qualifications: str,
                 working_hours: str, available: bool = True):
        super().__init__(name, contact, email)
        self.__specialty = specialty.strip()
        self.__qualifications = qualifications.strip()
        self.__working_hours = working_hours.strip()
        self.__available = bool(available)

    def get_specialty(self) -> str:
        return self.__specialty

    def set_specialty(self, specialty: str) -> None:
        self.__specialty = (specialty or "").strip()

    def get_qualifications(self) -> str:
        return self.__qualifications

    def set_qualifications(self, quals: str) -> None:
        self.__qualifications = (quals or "").strip()

    def get_working_hours(self) -> str:
        return self.__working_hours

    def set_working_hours(self, hours: str) -> None:
        self.__working_hours = (hours or "").strip()

    def is_available(self) -> bool:
        return self.__available

    def set_availability(self, available: bool) -> None:
        self.__available = bool(available)

    def __str__(self) -> str:
        return (f"Doctor(name={self.get_name()}, specialty={self.__specialty}, "
                f"available={self.__available}, hours={self.__working_hours})")
