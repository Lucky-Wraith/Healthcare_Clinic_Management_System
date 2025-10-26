class LabOrder:
    """
    Laboratory test order and its result lifecycle.
    """

    STATUS_ORDERED = "ORDERED"
    STATUS_IN_PROGRESS = "IN_PROGRESS"
    STATUS_COMPLETED = "COMPLETED"

    def __init__(self, test_name: str):
        self.__test_name = (test_name or "").strip()
        self.__result = ""
        self.__status = LabOrder.STATUS_ORDERED

    def get_test_name(self) -> str:
        return self.__test_name

    def set_test_name(self, test_name: str) -> None:
        self.__test_name = (test_name or "").strip()

    def get_status(self) -> str:
        return self.__status

    def update_status(self, status: str) -> None:
        allowed = {LabOrder.STATUS_ORDERED, LabOrder.STATUS_IN_PROGRESS, LabOrder.STATUS_COMPLETED}
        if status not in allowed:
            raise ValueError("Invalid status for LabOrder.")
        self.__status = status

    def link_result(self, result_text: str) -> None:
        self.__result = (result_text or "").strip()
        self.__status = LabOrder.STATUS_COMPLETED

    def get_result(self) -> str:
        return self.__result

    def __str__(self) -> str:
        return f"LabOrder(test={self.__test_name}, status={self.__status}, has_result={bool(self.__result)})"
