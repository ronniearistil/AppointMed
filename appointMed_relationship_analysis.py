"""
Revised Relationship Analysis

Users and UserProfile
Relationship Type: One-to-One
Explanation: Each user has exactly one user profile, and each user profile is associated with one user.

Users and Doctor
Relationship Type: One-to-One
Explanation: Each user can be a doctor, and each doctor is linked to one user account.

Doctors and DoctorSpecialty
Relationship Type: One-to-Many
Explanation: A doctor can have multiple specialties, but each entry in the DoctorSpecialty table links back to one doctor.

Specialties and DoctorSpecialty
Relationship Type: One-to-Many
Explanation: Each specialty can be associated with multiple doctors (many doctors can share the same specialty), but each entry in DoctorSpecialty refers to one specialty.

Patients and Users
Relationship Type: One-to-One
Explanation: Each patient is linked to one user account, and each user can be a patient.

Appointments and Patients
Relationship Type: One-to-Many
Explanation: A patient can have multiple appointments with different doctors.

Appointments and Doctors
Relationship Type: One-to-Many
Explanation: A doctor can have multiple appointments, but each appointment is tied to one doctor.

Patients and Doctors
Relationship Type: Many-to-Many
Explanation: A patient can see multiple doctors, and a doctor can see multiple patients. This relationship would typically be managed by an additional linking table (e.g., PatientDoctor) to track the connections between patients and doctors.

Appointments and Specialties
Relationship Type: One-to-Many
Explanation: An appointment can be associated with one specialty, while each specialty can apply to multiple appointments.

Summary of Relationships
One-to-One: Users ↔ UserProfile, Users ↔ Doctor, Patients ↔ Users
One-to-Many: Doctors ↔ DoctorSpecialty, Specialties ↔ DoctorSpecialty, Patients ↔ Appointments, Doctors ↔ Appointments, Appointments ↔ Specialties
Many-to-Many: Patients ↔ Doctors (managed through a linking table like PatientDoctor)
"""
