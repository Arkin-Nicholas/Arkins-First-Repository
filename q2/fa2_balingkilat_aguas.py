class Patient:
    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = bill_amount

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, value):
        self._name = value

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value

    def calculate_bill(self):
        return self._bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self._bill_amount * 0.80


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self._bill_amount * 0.85


regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)

patients = [regular_patient, senior_patient, philhealth_patient]

for patient in patients:
    print(f"Patient: {patient.name}")
    print(f"Original Bill: ₱{patient.bill_amount:,.2f}")
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}")
    print("-" * 30)
