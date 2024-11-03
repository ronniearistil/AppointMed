from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)

class UserProfile(Base):
    __tablename__ = 'UserProfile'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(Text)
    email = Column(Text)
    address = Column(Text)

class Doctor(Base):
    __tablename__ = 'Doctors'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    availability_schedule = Column(Text)

class Specialty(Base):
    __tablename__ = 'Specialties'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class DoctorSpecialty(Base):
    __tablename__ = 'DoctorSpecialty'
    doctor_id = Column(Integer, ForeignKey('Doctors.id'), primary_key=True)
    specialty_id = Column(Integer, ForeignKey('Specialties.id'), primary_key=True)

class Patient(Base):
    __tablename__ = 'Patients'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    medical_history = Column(Text)

class Appointment(Base):
    __tablename__ = 'Appointments'
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey('Doctors.id'))
    patient_id = Column(Integer, ForeignKey('Patients.id'))
    specialty_id = Column(Integer, ForeignKey('Specialties.id'))
    appointment_datetime = Column(DateTime)
    duration = Column(Integer)
    status = Column(String)

class PatientDoctor(Base):
    __tablename__ = 'PatientDoctor'
    
    patient_id = Column(Integer, ForeignKey('Patients.id'), primary_key=True)
    doctor_id = Column(Integer, ForeignKey('Doctors.id'), primary_key=True)

    # Establish relationships
    patient = relationship("Patient", back_populates="doctors")
    doctor = relationship("Doctor", back_populates="patients")

# Update relationships in Patient and Doctor classes
Patient.doctors = relationship("PatientDoctor", back_populates="patient")
Doctor.patients = relationship("PatientDoctor", back_populates="doctor")






