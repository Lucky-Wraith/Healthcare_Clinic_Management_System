"""
Test cases for Healthcare Clinic Management System
Each section tests one feature with at least two test instances.
"""

from clinic import Clinic
from department import Department
from doctor import Doctor
from patient import Patient
from appointment import Appointment
from medical_record import MedicalRecord
from lab_order import LabOrder
from prescription import Prescription
from billing import Billing

print("\n===== TEST 1: CLINIC AND DEPARTMENT CREATION =====")
clinic = Clinic("Royal Care Clinic", "MG Road, Indore", "0731-2345678", "info@royalcare.com")
dept1 = Department("General Practice", "Mon–Sat 10:00–17:00")
dept2 = Department("Cardiology", "Mon–Fri 09:00–16:00")
clinic.add_department(dept1)
clinic.add_department(dept2)
print(clinic)
print("Departments:", [d.get_name() for d in clinic.get_departments()])

print("\n===== TEST 2: DOCTOR CREATION =====")
doc1 = Doctor("Dr. Brown", "9999999999", "brown@clinic.com", "General Practice", "MBBS", "10–17", True)
doc2 = Doctor("Dr. Mehta", "8888888888", "mehta@clinic.com", "Cardiology", "MD", "9–16", True)
dept1.add_staff(doc1)
dept2.add_staff(doc2)
print(doc1)
print(doc2)

print("\n===== TEST 3: PATIENT REGISTRATION =====")
pat1 = Patient("Aliyah", "7777777777", "aliyah@mail.com", "1990-04-05", "Old Palasia, Indore", "ICICI Health")
pat2 = Patient("Rahul", "6666666666", "rahul@mail.com", "1985-08-20", "Vijay Nagar, Indore", "Star Health")
clinic.register_patient(pat1)
clinic.register_patient(pat2)
print(pat1)
print(pat2)

print("\n===== TEST 4: APPOINTMENT BOOKING =====")
appt1 = Appointment("2025-11-02", "10:30 AM", pat1, doc1, dept1)
appt2 = Appointment("2025-11-03", "11:00 AM", pat2, doc2, dept2)
appt1.schedule()
appt2.schedule()
print(appt1)
print(appt2)

print("\n===== TEST 5: MEDICAL RECORD CREATION =====")
mr1 = MedicalRecord("Flu", "Rest and hydration advised", "BP: 110/70; Temp: 100F")
mr2 = MedicalRecord("Chest Pain", "Prescribed ECG and further observation", "BP: 130/85")
appt1.attach_medical_record(mr1)
appt2.attach_medical_record(mr2)
print(mr1)
print(mr2)

print("\n===== TEST 6: LAB ORDER LIFECYCLE =====")
lab1 = LabOrder("CBC Panel")
lab2 = LabOrder("ECG Test")
mr1.order_lab_test(lab1)
mr2.order_lab_test(lab2)
lab1.update_status(LabOrder.STATUS_IN_PROGRESS)
lab1.link_result("All parameters normal.")
lab2.link_result("Mild irregularity detected.")
print(lab1)
print(lab2)

print("\n===== TEST 7: PRESCRIPTION GENERATION =====")
rx1 = Prescription("Paracetamol 500mg", "1 tab TID", "After meals for 3 days")
rx2 = Prescription("Aspirin 75mg", "1 tab OD", "After breakfast")
rx1.mark_as_sent()
appt1.attach_prescription(rx1)
appt2.attach_prescription(rx2)
print(rx1)
print(rx2)

print("\n===== TEST 8: BILLING AND INSURANCE =====")
bill1 = Billing("INV-001", consultation_fee=500, lab_charges=300, medication_charges=150)
bill1.set_billed_to(pat1)
bill1.set_service_doctor(doc1)
amount_due1 = bill1.apply_insurance(0.2)
bill1.process_payment()

bill2 = Billing("INV-002", consultation_fee=700, lab_charges=400, medication_charges=200)
bill2.set_billed_to(pat2)
bill2.set_service_doctor(doc2)
amount_due2 = bill2.apply_insurance(0.3)
bill2.process_payment()

appt1.attach_billing(bill1)
appt2.attach_billing(bill2)

print(bill1, "Payable After Insurance:", amount_due1)
print(bill2, "Payable After Insurance:", amount_due2)

print("\n===== TEST 9: APPOINTMENT CANCELLATION =====")
appt_cancel = Appointment("2025-11-05", "12:00 PM", pat1, doc2)
appt_cancel.cancel()
print(appt_cancel)

print("\n===== TEST 10: SUMMARY CHECK =====")
for appt in [appt1, appt2]:
    print("\n--- Appointment Summary ---")
    print(appt)
    print("Medical Record:", appt.get_medical_record())
    print("Prescription:", appt.get_prescription())
    print("Billing:", appt.get_billing())
