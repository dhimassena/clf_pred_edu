import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("model.joblib")
result_target = joblib.load("enc_target.joblib")

def prediction(data):
    """Making prediction

    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data

    Returns:
        str: Prediction result (Enrolled, Graduate, or Dropout)
    """
    result = model.predict(data)
    final_result = result_target.inverse_transform(result)
    return final_result