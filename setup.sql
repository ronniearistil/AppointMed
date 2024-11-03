-- Create the Users table
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL
);

-- Create the UserProfile table
CREATE TABLE IF NOT EXISTS UserProfile (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone_number TEXT,
    email TEXT,
    address TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- Create the Doctors table
CREATE TABLE IF NOT EXISTS Doctors (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    availability_schedule TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- Create the Specialties table
CREATE TABLE IF NOT EXISTS Specialties (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- Create the DoctorSpecialty join table
CREATE TABLE IF NOT EXISTS DoctorSpecialty (
    doctor_id INTEGER,
    specialty_id INTEGER,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(id),
    FOREIGN KEY (specialty_id) REFERENCES Specialties(id),
    PRIMARY KEY (doctor_id, specialty_id)
);

-- Create the Patients table
CREATE TABLE IF NOT EXISTS Patients (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    medical_history TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- Create the Appointments table
CREATE TABLE IF NOT EXISTS Appointments (
    id INTEGER PRIMARY KEY,
    doctor_id INTEGER,
    patient_id INTEGER,
    specialty_id INTEGER,
    appointment_datetime DATETIME,
    duration INTEGER,
    status TEXT,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(id),
    FOREIGN KEY (patient_id) REFERENCES Patients(id),
    FOREIGN KEY (specialty_id) REFERENCES Specialties(id)
);

-- PatientDoctor join table
CREATE TABLE IF NOT EXISTS PatientDoctor (
    patient_id INTEGER,
    doctor_id INTEGER,
    FOREIGN KEY (patient_id) REFERENCES Patients(id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(id),
    PRIMARY KEY (patient_id, doctor_id)
);


