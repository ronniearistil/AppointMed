from lib.models import Patient, Doctor  # Import other models

def test_patient_creation():
    patient = Patient(user_id=1, medical_history='No known allergies')
    assert patient.medical_history == 'No known allergies'

def test_doctor_creation():
    doctor = Doctor(user_id=1, availability_schedule='M-F 9-5')
    assert doctor.availability_schedule == 'M-F 9-5'
