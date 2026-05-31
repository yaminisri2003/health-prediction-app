import streamlit as st
import re
from datetime import date

from database import (
    add_patient,
    get_patients_dataframe,
    delete_patient,
    email_exists
)

from model import predict_health


st.set_page_config(
    page_title="Health Prediction Application",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Health Prediction Application")

st.markdown("---")

# ==========================
# Patient Entry Form
# ==========================

st.subheader("Add Patient Record")

with st.form("patient_form"):

    full_name = st.text_input("Full Name")

    dob = st.date_input(
        "Date of Birth",
        min_value=date(1900, 1, 1),
        max_value=date.today()
    )

    email = st.text_input("Email Address")

    glucose = st.number_input(
        "Glucose",
        min_value=0.0,
        step=0.1
    )

    haemoglobin = st.number_input(
        "Haemoglobin",
        min_value=0.0,
        step=0.1
    )

    cholesterol = st.number_input(
        "Cholesterol",
        min_value=0.0,
        step=0.1
    )

    submit_button = st.form_submit_button("Predict & Save")

# ==========================
# Form Validation
# ==========================

if submit_button:

    if not full_name.strip():
        st.error("Full Name is required.")

    elif not email.strip():
        st.error("Email Address is required.")

    elif dob > date.today():
        st.error("Date of Birth cannot be a future date.")

    elif not re.match(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
        email
    ):
        st.error("Enter a valid email address.")

    elif email_exists(email):
        st.error("Email already exists.")

    else:

        remarks = predict_health(
            glucose,
            haemoglobin,
            cholesterol
        )

        add_patient(
            full_name,
            str(dob),
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )

        st.success("Patient record saved successfully.")
        st.info(f"Prediction: {remarks}")

# ==========================
# Display Records
# ==========================

st.markdown("---")

st.subheader("Patient Records")

df = get_patients_dataframe()

if not df.empty:

    st.dataframe(
        df,
        use_container_width=True
    )

else:
    st.warning("No records available.")

# ==========================
# Delete Record
# ==========================

st.markdown("---")

st.subheader("Delete Patient Record")

patient_id = st.number_input(
    "Enter Patient ID",
    min_value=1,
    step=1
)

if st.button("Delete Record"):

    delete_patient(patient_id)

    st.success("Record deleted successfully.")
    st.rerun()