import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Student Predictor", layout="centered")

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Student Performance Predictor")
st.markdown("Predict a student's **math score** based on academic and background details.")

# Inputs
st.subheader("Enter Student Details")

gender = st.selectbox("Gender", ["Female", "Male"])
race = st.selectbox("Race/Ethnicity", ["Group A", "Group B", "Group C", "Group D", "Group E"])
parent_edu = st.selectbox("Parental Education",
                          ["Some High School", "High School", "Some College",
                           "Associate Degree", "Bachelor Degree", "Master Degree"])
lunch = st.selectbox("Lunch Type", ["Standard", "Free/Reduced"])
test_prep = st.selectbox("Test Preparation Course", ["None", "Completed"])

reading = st.slider("Reading Score", 0, 100)
writing = st.slider("Writing Score", 0, 100)

# Convert to numerical (IMPORTANT)
gender = 0 if gender == "Female" else 1
race = ["Group A", "Group B", "Group C", "Group D", "Group E"].index(race)
parent_edu = ["Some High School", "High School", "Some College",
              "Associate Degree", "Bachelor Degree", "Master Degree"].index(parent_edu)
lunch = 0 if lunch == "Standard" else 1
test_prep = 0 if test_prep == "None" else 1

# Prediction
if st.button("Predict Score"):
    features = np.array([[gender, race, parent_edu, lunch, test_prep, reading, writing]])
    prediction = model.predict(features)

    st.success(f"Predicted Math Score: {prediction[0]:.2f}")