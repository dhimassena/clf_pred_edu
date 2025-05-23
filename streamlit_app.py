import streamlit as st
import pandas as pd
import numpy as np
from preprocessing import *
from prediction import *
# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
"""
# :sparkles: Proyek Jaya Jaya Institut (Prototype)

**Dicoding IDCamp 2025**

"""

st.info(
    """
    Nama: [Dhimas Sena Rahmantara]\n
    Email: [dhimassr@gmail.com]\n
    ID Dicoding: [dhimassena]
    """
)
# data = pd.DataFrame()

col1, col2 = st.columns(2)
with col1:
    previous_qualification_grade = int(st.number_input(label='previous_qualification_grade', value=120))
    # data["previous_qualification_grade"] = previous_qualification_grade
with col2:
    admission_grade = int(st.number_input(label='admission_grade', value=150))
    # data["admission_grade"] = admission_grade

col3, col4 = st.columns(2)
with col3:
    age_at_enrollment = int(st.number_input(label='age_at_enrollment', value=28))
    # data["age_at_enrollment"] = age_at_enrollment
with col4:
    curricular_units_1st_sem_evaluations = int(st.number_input(label='curricular_units_1st_sem_evaluations', value=10))
    # data["curricular_units_1st_sem_evaluations"] = curricular_units_1st_sem_evaluations

col5, col6 = st.columns(2)
with col5:
    curricular_units_1st_sem_approved = int(st.number_input(label='curricular_units_1st_sem_approved', value=5))
    # data["curricular_units_1st_sem_approved"] = curricular_units_1st_sem_approved
with col6:
    curricular_units_1st_sem_grade = int(st.number_input(label='curricular_units_1st_sem_grade', value=6))
    # data["curricular_units_1st_sem_grade"] = curricular_units_1st_sem_grade

col7, col8 = st.columns(2)
with col7:
    curricular_units_2nd_sem_evaluations = int(st.number_input(label='curricular_units_2nd_sem_evaluations', value=4))
    # data["curricular_units_2nd_sem_evaluations"] = curricular_units_2nd_sem_evaluations
with col8:
    curricular_units_2nd_sem_approved = int(st.number_input(label='curricular_units_2nd_sem_approved', value=8))
    # data["curricular_units_2nd_sem_approved"] = curricular_units_2nd_sem_approved

col9, col10 = st.columns(2)
with col9:
    curricular_units_2nd_sem_grade = int(st.number_input(label='curricular_units_2nd_sem_grade', value=9))
    # data["curricular_units_2nd_sem_grade"] = curricular_units_2nd_sem_grade
with col10:
    gdp = int(st.number_input(label='gdp', value=5))
    # data["gdp"] = gdp

data = {
    "previous_qualification_grade": [previous_qualification_grade],
    "admission_grade": [admission_grade],
    "age_at_enrollment": [age_at_enrollment],
    "curricular_units_1st_sem_evaluations": [curricular_units_1st_sem_evaluations],
    "curricular_units_1st_sem_approved": [curricular_units_1st_sem_approved],
    "curricular_units_1st_sem_grade": [curricular_units_1st_sem_grade],
    "curricular_units_2nd_sem_evaluations": [curricular_units_2nd_sem_evaluations],
    "curricular_units_2nd_sem_approved": [curricular_units_2nd_sem_approved],
    "curricular_units_2nd_sem_grade": [curricular_units_2nd_sem_grade],
    "gdp":gdp
}

df = pd.DataFrame(data)

with st.expander("Data Inputan"):
    st.dataframe(data=df, width=800, height=10)

if st.button('Prediksi'):
    # st.info(df)
    new_data = data_prep(df=df)
    hasil = prediction(new_data)
    # hasil = hasil.map({0: "Dropout", 1: "Enrolled", 2: "Graduate"})
    if(hasil == 0):
        hasil = "Dropout"
    elif(hasil == 1):
        hasil = "Enrolled"
    elif(hasil == 2):
        hasil = "Graduate"
    # st.write("Hasil Prediksi: {}".format(prediction(new_data)))
    st.write(f"Hasil Prediksi: {hasil}")