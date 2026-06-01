import streamlit as st
import re
from datetime import date

from database import (
    add_patient,
    get_patients_dataframe,
    delete_patient,
    email_exists,
    get_patient_by_id,
    update_patient
)

from model import predict_health

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Health Prediction Application",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Health Prediction Application")

st.markdown("""
AI-powered patient management system with health risk prediction and
Gemini-generated medical remarks.
""")

# ==========================
# DASHBOARD METRIC
# ==========================

df_count = get_patients_dataframe()

st.metric(
    "Total Patients",
    len(df_count)
)

st.markdown("---")

# ==========================
# ADD PATIENT
# ==========================

st.subheader("➕ Add Patient Record")

with st.form("patient_form"):

    col1, col2 = st.columns(2)

    with col1:

        full_name = st.text_input("Full Name")

        dob = st.date_input(
            "Date of Birth",
            min_value=date(1900, 1, 1),
            max_value=date.today()
        )

        glucose = st.number_input(
            "Glucose",
            min_value=0.0,
            step=0.1
        )

    with col2:

        email = st.text_input("Email Address")

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

    submit_button = st.form_submit_button(
        "Predict & Save"
    )

if submit_button:

    if not full_name.strip():

        st.error("Full Name is required.")

    elif not email.strip():

        st.error("Email Address is required.")

    elif dob > date.today():

        st.error(
            "Date of Birth cannot be a future date."
        )

    elif not re.match(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
        email
    ):

        st.error(
            "Enter a valid email address."
        )

    elif email_exists(email):

        st.error(
            "Email already exists."
        )

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

        st.success(
            "Patient record saved successfully."
        )

        st.success(
            "AI Health Remark Generated"
        )

        st.info(
            remarks
        )

# ==========================
# DISPLAY RECORDS
# ==========================

st.markdown("---")

st.subheader("📋 Patient Records")

df = get_patients_dataframe()

if not df.empty:

    st.dataframe(
        df,
        width="stretch",
        height=300,
        hide_index=True
    )

else:

    st.warning(
        "No records available."
    )

# ==========================
# UPDATE PATIENT
# ==========================

st.markdown("---")

st.subheader("✏️ Update Patient Record")

update_id = st.number_input(
    "Enter Patient ID to Update",
    min_value=1,
    step=1,
    key="update_id"
)

if st.button("Load Patient"):

    patient = get_patient_by_id(update_id)

    if patient:

        st.session_state["patient_loaded"] = True
        st.session_state["patient_id"] = patient.id
        st.session_state["full_name"] = patient.full_name
        st.session_state["dob"] = patient.dob
        st.session_state["email"] = patient.email
        st.session_state["glucose"] = patient.glucose
        st.session_state["haemoglobin"] = patient.haemoglobin
        st.session_state["cholesterol"] = patient.cholesterol

    else:

        st.error("Patient not found.")

if st.session_state.get("patient_loaded", False):

    st.markdown("### Edit Patient Details")

    new_name = st.text_input(
        "Full Name",
        value=st.session_state["full_name"],
        key="edit_name"
    )

    new_email = st.text_input(
        "Email",
        value=st.session_state["email"],
        key="edit_email"
    )

    new_glucose = st.number_input(
        "Glucose",
        value=float(st.session_state["glucose"]),
        key="edit_glucose"
    )

    new_haemoglobin = st.number_input(
        "Haemoglobin",
        value=float(st.session_state["haemoglobin"]),
        key="edit_haemoglobin"
    )

    new_cholesterol = st.number_input(
        "Cholesterol",
        value=float(st.session_state["cholesterol"]),
        key="edit_cholesterol"
    )

    if st.button("Update Record"):

        if not new_name.strip():

            st.error("Full Name is required.")

        elif not new_email.strip():

            st.error("Email Address is required.")

        elif not re.match(
            r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
            new_email
        ):

            st.error(
                "Enter a valid email address."
            )

        else:

            remarks = predict_health(
                new_glucose,
                new_haemoglobin,
                new_cholesterol
            )

            update_patient(
                st.session_state["patient_id"],
                new_name,
                st.session_state["dob"],
                new_email,
                new_glucose,
                new_haemoglobin,
                new_cholesterol,
                remarks
            )

            st.success(
                "Patient updated successfully."
            )

            st.success(
                "AI Health Remark Regenerated"
            )

            st.info(
                remarks
            )

            st.session_state["patient_loaded"] = False

            st.rerun()

# ==========================
# DELETE PATIENT
# ==========================

st.markdown("---")

st.subheader("🗑️ Delete Patient Record")

patient_id = st.number_input(
    "Enter Patient ID",
    min_value=1,
    step=1,
    key="delete_id"
)

if st.button("Delete Record"):

    deleted = delete_patient(patient_id)

    if deleted:

        st.success(
            "Record deleted successfully."
        )

        st.rerun()

    else:

        st.error(
            "No patient found with that ID."
        )