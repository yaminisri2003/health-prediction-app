import pandas as pd

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Database connection URL
DATABASE_URL = "sqlite:///health_data.db"

# Create database engine
engine = create_engine(DATABASE_URL)

# Base class for ORM models
Base = declarative_base()


# Patient Table Model
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    dob = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    glucose = Column(Float, nullable=False)
    haemoglobin = Column(Float, nullable=False)
    cholesterol = Column(Float, nullable=False)
    remarks = Column(String)


# Session Factory
SessionLocal = sessionmaker(bind=engine)


# Create Tables
Base.metadata.create_all(bind=engine)


# Get Database Session
def get_db():
    return SessionLocal()


# CREATE
def add_patient(
    full_name,
    dob,
    email,
    glucose,
    haemoglobin,
    cholesterol,
    remarks
):
    db = get_db()

    patient = Patient(
        full_name=full_name,
        dob=dob,
        email=email,
        glucose=glucose,
        haemoglobin=haemoglobin,
        cholesterol=cholesterol,
        remarks=remarks
    )

    db.add(patient)
    db.commit()
    db.close()


# READ
def get_all_patients():
    db = get_db()

    patients = db.query(Patient).all()

    db.close()

    return patients


# UPDATE
def update_patient(
    patient_id,
    full_name,
    dob,
    email,
    glucose,
    haemoglobin,
    cholesterol,
    remarks
):
    db = get_db()

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if patient:
        patient.full_name = full_name
        patient.dob = dob
        patient.email = email
        patient.glucose = glucose
        patient.haemoglobin = haemoglobin
        patient.cholesterol = cholesterol
        patient.remarks = remarks

        db.commit()

    db.close()


# DELETE
def delete_patient(patient_id):
    db = get_db()

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if patient:
        db.delete(patient)
        db.commit()

    db.close()


# Convert Data to DataFrame for Streamlit
def get_patients_dataframe():
    patients = get_all_patients()

    data = []

    for patient in patients:
        data.append(
            {
                "ID": patient.id,
                "Full Name": patient.full_name,
                "Date of Birth": patient.dob,
                "Email": patient.email,
                "Glucose": patient.glucose,
                "Haemoglobin": patient.haemoglobin,
                "Cholesterol": patient.cholesterol,
                "Remarks": patient.remarks,
            }
        )

    return pd.DataFrame(data)