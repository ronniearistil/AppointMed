from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Patient, Doctor, Specialty, Appointment, PatientDoctor
import os
from datetime import datetime

# Absolute path to the database file
db_path = os.path.join(os.path.dirname(__file__), '../AppointMed.db')  
DATABASE_URL = f"sqlite:///{db_path}"

# Create the engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Create some specialties
specialties = ['Cardiology', 'Dermatology', 'Pediatrics', 'General Practice']
for specialty_name in specialties:
    specialty = Specialty(name=specialty_name)
    session.add(specialty)

# Create some users (patients)
patients_data = [
    {'username': 'patient1', 'password_hash': 'hash1', 'role': 'patient', 'medical_history': 'No known allergies'},
    {'username': 'patient2', 'password_hash': 'hash2', 'role': 'patient', 'medical_history': 'Diabetic'},
    {'username': 'patient3', 'password_hash': 'hash3', 'role': 'patient', 'medical_history': 'Hypertension'},
    {'username': 'patient4', 'password_hash': 'hash4', 'role': 'patient', 'medical_history': 'Asthma'}
]

for data in patients_data:
    existing_user = session.query(User).filter_by(username=data['username']).first()
    if existing_user is None:
        user = User(username=data['username'], password_hash=data['password_hash'], role=data['role'])
        session.add(user)
        session.commit()  # Commit to get the user ID for the patient
        patient = Patient(user_id=user.id, medical_history=data['medical_history'])
        session.add(patient)
    else:
        print(f"User {data['username']} already exists.")

# Create some users (doctors)
doctors_data = [
    {'username': 'doctor1', 'password_hash': 'hash1', 'role': 'doctor', 'availability_schedule': 'M-F 9-5'},
    {'username': 'doctor2', 'password_hash': 'hash2', 'role': 'doctor', 'availability_schedule': 'M-F 10-6'},
    {'username': 'doctor3', 'password_hash': 'hash3', 'role': 'doctor', 'availability_schedule': 'M-W 8-4'},
    {'username': 'doctor4', 'password_hash': 'hash4', 'role': 'doctor', 'availability_schedule': 'T-Th 9-5'}
]

for data in doctors_data:
    existing_user = session.query(User).filter_by(username=data['username']).first()
    if existing_user is None:
        user = User(username=data['username'], password_hash=data['password_hash'], role=data['role'])
        session.add(user)
        session.commit()  # Commit to get the user ID for the doctor
        doctor = Doctor(user_id=user.id, availability_schedule=data['availability_schedule'])
        session.add(doctor)
    else:
        print(f"User {data['username']} already exists.")

# Create some appointments
appointments_data = [
    {'doctor_id': 1, 'patient_id': 1, 'specialty_id': 1, 'appointment_datetime': datetime(2024, 11, 10, 9, 0), 'duration': 30, 'status': 'scheduled'},
    {'doctor_id': 2, 'patient_id': 2, 'specialty_id': 2, 'appointment_datetime': datetime(2024, 11, 11, 10, 0), 'duration': 45, 'status': 'scheduled'},
    {'doctor_id': 3, 'patient_id': 3, 'specialty_id': 3, 'appointment_datetime': datetime(2024, 11, 12, 11, 0), 'duration': 30, 'status': 'scheduled'},
    {'doctor_id': 4, 'patient_id': 4, 'specialty_id': 4, 'appointment_datetime': datetime(2024, 11, 13, 14, 0), 'duration': 60, 'status': 'scheduled'},
]

for data in appointments_data:
    appointment = Appointment(
        doctor_id=data['doctor_id'],
        patient_id=data['patient_id'],
        specialty_id=data['specialty_id'],
        appointment_datetime=data['appointment_datetime'],
        duration=data['duration'],
        status=data['status']
    )
    session.add(appointment)

# Commit all changes to the database
session.commit()
print("Database populated successfully!")

# Close the session
session.close()


