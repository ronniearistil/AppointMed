from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Patient, Doctor, PatientDoctor  # Import models from the current directory
import os

# Absolute path to the database file
db_path = os.path.join(os.path.dirname(__file__), '../AppointMed.db')  # Adjust path if needed
DATABASE_URL = f"sqlite:///{db_path}"

# Create the engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables
Base.metadata.create_all(engine)

# Check if user already exists
username_to_check = 'johndoe'
existing_user = session.query(User).filter_by(username=username_to_check).first()

if existing_user is None:
    # User does not exist, create a new one
    new_user = User(username=username_to_check, password_hash='hashed_password', role='patient')
    session.add(new_user)
    session.commit()
    print(f"User {username_to_check} created successfully.")
else:
    print(f"User {username_to_check} already exists.")

# Example of adding a patient and a doctor relationship
patient_username = 'johndoe'
doctor_id_to_check = 1  # Replace with an actual doctor ID

# Get the patient object
patient = session.query(Patient).filter_by(user_id=existing_user.id).first()

# Check if the patient exists
if patient:
    # Check if doctor already exists in PatientDoctor relationship
    existing_relationship = session.query(PatientDoctor).filter_by(patient_id=patient.id, doctor_id=doctor_id_to_check).first()

    if existing_relationship is None:
        # Create a new PatientDoctor relationship
        new_relationship = PatientDoctor(patient_id=patient.id, doctor_id=doctor_id_to_check)
        session.add(new_relationship)
        session.commit()
        print(f"Relationship between patient {patient.id} and doctor {doctor_id_to_check} created successfully.")
    else:
        print(f"Relationship already exists between patient {patient.id} and doctor {doctor_id_to_check}.")
else:
    print("Patient not found.")













