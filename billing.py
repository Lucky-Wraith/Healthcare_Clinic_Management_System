class Billing:
    """
    Billing for an appointment: invoice, insurance, and payment.
    """

    PAYMENT_PENDING = "PENDING"
    PAYMENT_PAID = "PAID"

    def __init__(self, invoice_id: str, consultation_fee: float = 0.0, lab_charges: float = 0.0,
                 medication_charges: float = 0.0):
        self.__invoice_id = (invoice_id or "").strip()
        self.__consultation_fee = float(consultation_fee or 0.0)
        self.__lab_charges = float(lab_charges or 0.0)
        self.__medication_charges = float(medication_charges or 0.0)
        self.__insurance_applied = False
        self.__payment_status = Billing.PAYMENT_PENDING
        
        self.__billed_to_patient = None
        self.__service_doctor = None

    # Associations
    def set_billed_to(self, patient) -> None:
        # late import avoidance: type check by attribute
        if not hasattr(patient, "get_name"):
            raise TypeError("Invalid patient reference.")
        self.__billed_to_patient = patient

    def get_billed_to(self):
        return self.__billed_to_patient

    def set_service_doctor(self, doctor) -> None:
        if not hasattr(doctor, "get_name"):
            raise TypeError("Invalid doctor reference.")
        self.__service_doctor = doctor

    def get_service_doctor(self):
        return self.__service_doctor

    # Charges + totals
    def get_total(self) -> float:
        return round(self.__consultation_fee + self.__lab_charges + self.__medication_charges, 2)

    def apply_insurance(self, coverage_rate: float) -> float:
        """
        coverage_rate in 0..1 -> reduces payable amount.
        Returns payable after insurance.
        """
        if not (0.0 <= coverage_rate <= 1.0):
            raise ValueError("coverage_rate must be between 0 and 1.")
        gross = self.get_total()
        payable = round(gross * (1.0 - coverage_rate), 2)
        self.__insurance_applied = True
        return payable

    def process_payment(self) -> None:
        self.__payment_status = Billing.PAYMENT_PAID

    # Getters/Setters
    def get_invoice_id(self) -> str:
        return self.__invoice_id

    def set_invoice_id(self, invoice_id: str) -> None:
        self.__invoice_id = (invoice_id or "").strip()

    def get_consultation_fee(self) -> float:
        return self.__consultation_fee

    def set_consultation_fee(self, fee: float) -> None:
        self.__consultation_fee = float(fee or 0.0)

    def get_lab_charges(self) -> float:
        return self.__lab_charges

    def set_lab_charges(self, charges: float) -> None:
        self.__lab_charges = float(charges or 0.0)

    def get_medication_charges(self) -> float:
        return self.__medication_charges

    def set_medication_charges(self, charges: float) -> None:
        self.__medication_charges = float(charges or 0.0)

    def is_insurance_applied(self) -> bool:
        return self.__insurance_applied

    def get_payment_status(self) -> str:
        return self.__payment_status

    def __str__(self) -> str:
        billed = self.__billed_to_patient.get_name() if self.__billed_to_patient else "N/A"
        doc = self.__service_doctor.get_name() if self.__service_doctor else "N/A"
        return (f"Billing(invoice={self.__invoice_id}, total={self.get_total()}, "
                f"insurance={self.__insurance_applied}, payment={self.__payment_status}, "
                f"patient={billed}, doctor={doc})")
