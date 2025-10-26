class Prescription:
    """
    Prescription issued during an appointment.
    """

    def __init__(self, drug_name: str, dosage: str, directions: str):
        self.__drug_name = (drug_name or "").strip()
        self.__dosage = (dosage or "").strip()
        self.__directions = (directions or "").strip()
        self.__sent_to_pharmacy = False

    def get_drug_name(self) -> str:
        return self.__drug_name

    def set_drug_name(self, name: str) -> None:
        self.__drug_name = (name or "").strip()

    def get_dosage(self) -> str:
        return self.__dosage

    def set_dosage(self, dosage: str) -> None:
        self.__dosage = (dosage or "").strip()

    def get_directions(self) -> str:
        return self.__directions

    def set_directions(self, directions: str) -> None:
        self.__directions = (directions or "").strip()

    def mark_as_sent(self) -> None:
        self.__sent_to_pharmacy = True

    def is_sent(self) -> bool:
        return self.__sent_to_pharmacy

    def __str__(self) -> str:
        return (f"Prescription(drug={self.__drug_name}, dosage={self.__dosage}, "
                f"sent={self.__sent_to_pharmacy})")
