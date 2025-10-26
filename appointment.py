from typing import Optional
from patient import Patient
from doctor import Doctor
from department import Department


class Appointment:
    """
    Appointment linking patient, doctor, and optional department context.
    """

    STATUS_SCHEDULED = "SCHEDULED"
    STATUS_CANCELLED = "CANCELLED"
    STATUS_COMPLETED = "COMPLETED"

    def __init__(self, date: str, time: str, patient: Patient, doctor: Doctor, department: Optional[Department] = None):
        if not isinstance(patient, Patient):
            raise TypeError("patient must be Patient.")
        if not isinstance(doctor, Doctor):
            raise TypeError("doctor must be Doctor.")
        self.__date = date.strip()
        self.__time = time.strip()
        self.__patient = patient
        self.__doctor = doctor
        self.__department = department
        self.__status = Appointment.STATUS_SCHEDULED
        # Composition references (assigned externally after creation)
        self.__medical_record = None
        self.__prescription = None
        self.__billing = None

    # Basic state ops
    def schedule(self) -> None:
        self.__status = Appointment.STATUS_SCHEDULED

    def cancel(self) -> None:
        self.__status = Appointment.STATUS_CANCELLED

    def complete(self) -> None:
        self.__status = Appointment.STATUS_COMPLETED

    # Getters/Setters
    def get_date(self) -> str:
        return self.__date

    def set_date(self, date: str) -> None:
        self.__date = (date or "").strip()

    def get_time(self) -> str:
        return self.__time

    def set_time(self, time: str) -> None:
        self.__time = (time or "").strip()

    def get_status(self) -> str:
        return self.__status

    def get_patient(self) -> Patient:
        return self.__patient

    def get_doctor(self) -> Doctor:
        return self.__doctor

    def get_department(self) -> Optional[Department]:
        return self.__department

    def set_department(self, dept: Optional[Department]) -> None:
        self.__department = dept

    # Composition links
    def attach_medical_record(self, mr) -> None:
        self.__medical_record = mr

    def get_medical_record(self):
        return self.__medical_record

    def attach_prescription(self, pr) -> None:
        self.__prescription = pr

    def get_prescription(self):
        return self.__prescription

    def attach_billing(self, bill) -> None:
        self.__billing = bill

    def get_billing(self):
        return self.__billing

    def __str__(self) -> str:
        dept = self.__department.get_name() if self.__department else "N/A"
        return (f"Appointment(date={self.__date}, time={self.__time}, "
                f"patient={self.__patient.get_name()}, doctor={self.__doctor.get_name()}, "
                f"dept={dept}, status={self.__status})")
