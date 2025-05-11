import streamlit as st
import pandas as pd
import numpy as np
from preprocessing import *
import prediction
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

data = pd.DataFrame()

previous_qualification_grade = int(st.number_input(label='previous_qualification_grade', value=120))
data["previous_qualification_grade"] = previous_qualification_grade

admission_grade = int(st.number_input(label='admission_grade', value=150))
data["admission_grade"] = admission_grade

age_at_enrollment = int(st.number_input(label='age_at_enrollment', value=28))
data["age_at_enrollment"] = age_at_enrollment

curricular_units_1st_sem_evaluations = int(st.number_input(label='curricular_units_1st_sem_evaluations', value=10))
data["curricular_units_1st_sem_evaluations"] = curricular_units_1st_sem_evaluations

curricular_units_1st_sem_approved = int(st.number_input(label='curricular_units_1st_sem_approved', value=5))
data["curricular_units_1st_sem_approved"] = curricular_units_1st_sem_approved

curricular_units_1st_sem_grade = int(st.number_input(label='curricular_units_1st_sem_grade', value=6))
data["curricular_units_1st_sem_grade"] = curricular_units_1st_sem_grade

curricular_units_2nd_sem_evaluations = int(st.number_input(label='curricular_units_2nd_sem_evaluations', value=4))
data["curricular_units_2nd_sem_evaluations"] = curricular_units_2nd_sem_evaluations

curricular_units_2nd_sem_approved = int(st.number_input(label='curricular_units_2nd_sem_approved', value=8))
data["curricular_units_2nd_sem_approved"] = curricular_units_2nd_sem_approved

curricular_units_2nd_sem_grade = int(st.number_input(label='curricular_units_2nd_sem_grade', value=9))
data["curricular_units_2nd_sem_grade"] = curricular_units_2nd_sem_grade

gdp = int(st.number_input(label='gdp', value=5))
data["gdp"] = gdp



with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

if st.button('Prediksi'):
    st.info(data)
    new_data = data_prep(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Hasil Prediksi: {}".format(prediction(new_data)))