import streamlit as st
import pandas as pd
import numpy as np
import joblib

scaler = joblib.load("sf_scaler.joblib")

def data_prep(df):
    # data = data.copy()
    # df = pd.DataFrame()
    df = scaler.transform(df)

    # df["previous_qualification_grade"] = scaler.transform(df[["previous_qualification_grade"]])
    # df["admission_grade"] = scaler.transform(df[["admission_grade"]])
    # df["age_at_enrollment"] = scaler.transform(df[["age_at_enrollment"]])
    # df["curricular_units_1st_sem_evaluations"] = scaler.transform(df[["curricular_units_1st_sem_evaluations"]])
    # df["curricular_units_1st_sem_approved"] = scaler.transform(df[["curricular_units_1st_sem_approved"]])
    # df["curricular_units_1st_sem_grade"] = scaler.transform(df[["curricular_units_1st_sem_grade"]])
    # df["curricular_units_2nd_sem_evaluations"] = scaler.transform(df[["curricular_units_2nd_sem_evaluations"]])
    # df["curricular_units_2nd_sem_approved"] = scaler.transform(df[["curricular_units_2nd_sem_approved"]])
    # df["curricular_units_2nd_sem_grade"] = scaler.transform(df[["curricular_units_2nd_sem_grade"]])
    # df["gdp"] = scaler.transform(df[["gdp"]])

    return df