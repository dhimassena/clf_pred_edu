import streamlit as st
import pandas as pd
import numpy as np
import joblib

scaler = joblib.load("num_col_scaler.joblib")

def data_prep(data):
    data = data.copy()
    df = pd.DataFrame()
    
    df["previous_qualification_grade"] = scaler.transform(data[["previous_qualification_grade"]])
    df["admission_grade"] = scaler.transform(np.asarray(data["admission_grade"]).reshape(-1,1))[0]
    df["age_at_enrollment"] = scaler.transform(np.asarray(data["age_at_enrollment"]).reshape(-1,1))[0]
    df["curricular_units_1st_sem_evaluations"] = scaler.transform(np.asarray(data["curricular_units_1st_sem_evaluations"]).reshape(-1,1))[0]
    df["curricular_units_1st_sem_approved"] = scaler.transform(np.asarray(data["curricular_units_1st_sem_approved"]).reshape(-1,1))[0]
    df["curricular_units_1st_sem_grade"] = scaler.transform(np.asarray(data["curricular_units_1st_sem_grade"]).reshape(-1,1))[0]
    df["curricular_units_2nd_sem_evaluations"] = scaler.transform(np.asarray(data["curricular_units_2nd_sem_evaluations"]).reshape(-1,1))[0]
    df["curricular_units_2nd_sem_approved"] = scaler.transform(np.asarray(data["curricular_units_2nd_sem_approved"]).reshape(-1,1))[0]
    df["curricular_units_2nd_sem_grade"] = scaler.transform(np.asarray(data["curricular_units_2nd_sem_grade"]).reshape(-1,1))[0]
    df["gdp"] = scaler.transform(np.asarray(data["gdp"]).reshape(-1,1))[0]

    return df