# AppointMed - Patient Appointment Booking App

## Project Overview
**Owner:** Ronnie | **Phase:** 3 | **Cohort Grad:** 2025

**Project Title:** PatientConnect - Simplifying Healthcare Scheduling

### One-Sentence App Description:
AppointMed is an intuitive, secure appointment scheduling platform for patients and healthcare providers, streamlining booking processes, enhancing patient experience, and optimizing clinic management through real-time availability, reminders, and specialty-based doctor selection.

## Database Schema
### Database Tables:
- **Users**
  - **id:** Unique identifier for each user.
  - **username:** Username for login.
  - **password_hash:** Securely hashed password.
  - **role:** User role (patient or doctor).

- **UserProfile**
  - **id:** Unique identifier.
  - **user_id:** Links to User.
  - **first_name, last_name, phone_number, email, address:** Detailed contact info.

- **Doctors**
  - **id:** Unique identifier for each doctor.
  - **user_id:** Links to User.
  - **availability_schedule:** Doctor's available hours.

- **Specialties**
  - **id:** Unique identifier.
  - **name:** Specialty name (e.g., Cardiologist, Dermatologist).

- **DoctorSpecialty (Join Table)**
  - **doctor_id:** Links to Doctor.
  - **specialty_id:** Links to Specialty.

- **Patients**
  - **id:** Unique identifier for each patient.
  - **user_id:** Links to User.
  - **medical_history:** Patient medical background.

- **Appointments**
  - **id:** Unique identifier.
  - **doctor_id:** Links to Doctor.
  - **patient_id:** Links to Patient.
  - **specialty_id:** Links to Specialty.
  - **appointment_datetime:** Date and time for the appointment.
  - **duration:** Duration in minutes.
  - **status:** Appointment status (e.g., Confirmed, Pending, Canceled).

## API Routes
### GET Routes:
- `/doctors`: Retrieve all doctors and their specialties.
- `/specialties`: List available specialties.
- `/appointments`: Retrieve all appointments with related details (patient, doctor, specialty).
- `/patients`: List all patients and profiles.

### POST Routes:
- `/appointments`: Add a new appointment with date, time, and specialty.
- `/users`: Register new users (patients/doctors).

### PATCH Routes:
- `/appointments/:id`: Update appointment details like time, duration, and status.
- `/patients/:id`: Edit patient profile details.

### DELETE Routes:
- `/appointments/:id`: Delete an appointment from the system.

## MVP (Minimum Viable Product)
The AppointMed app will allow users to:
- **Book Appointments:** Patients can select doctors based on specialty and view available times.
- **View Appointment Schedules:** Patients and doctors can view upcoming appointments with real-time updates.
- **User Registration and Login:** Basic authentication with different access levels for patients and doctors.
- **Manage Appointment Details:** Doctors can adjust appointment statuses, and patients can reschedule if needed.

## Stretch Goals
- **Availability Filtering:** Enable patients to view only available slots for selected doctors.
- **Real-Time Notifications:** Implement email/SMS reminders for upcoming appointments and status updates.
- **Analytics Dashboard:** Allow clinic administrators to monitor appointment volume and manage resources.
- **Telemedicine Integration:** Include video consultation options for remote appointments, powered by Google Meet or Zoom.

## Validation Requirements
### Registration and Appointment Forms:
- Validate unique usernames.
- Ensure all required fields are filled.
- Display errors clearly on invalid entries, with user-friendly messaging.

## How to Run the Project
1. **Clone the repository:**
   ```bash
   git clone git@github.com:ronniearistil/AppointMed.git
   cd AppointMed

## Install dependencies:
- pipenv install
- pipenv shell

## Run the CLI:
- python lib/cli.py