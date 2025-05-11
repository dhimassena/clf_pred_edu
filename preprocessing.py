import streamlit as st
import pandas as pd
import numpy as np
import joblib

scaler = joblib.load("num_col_scaler.joblib")

def data_prep(data):
    data = data.copy()
    df = pd.DataFrame()
    
    df["previous_qualification_grade"] = scaler.transform(data[["previous_qualification_grade"]])
    df["admission_grade"] = scaler.transform(data[["admission_grade"]])
    df["age_at_enrollment"] = scaler.transform(data[["age_at_enrollment"]])
    df["curricular_units_1st_sem_evaluations"] = scaler.transform(data[["curricular_units_1st_sem_evaluations"]])
    df["curricular_units_1st_sem_approved"] = scaler.transform(data[["curricular_units_1st_sem_approved"]])
    df["curricular_units_1st_sem_grade"] = scaler.transform(data[["curricular_units_1st_sem_grade"]])
    df["curricular_units_2nd_sem_evaluations"] = scaler.transform(data[["curricular_units_2nd_sem_evaluations"]])
    df["curricular_units_2nd_sem_approved"] = scaler.transform(data[["curricular_units_2nd_sem_approved"]])
    df["curricular_units_2nd_sem_grade"] = scaler.transform(data[["curricular_units_2nd_sem_grade"]])
    df["gdp"] = scaler.transform(data[["gdp"]])

    return df