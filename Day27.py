
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("happiness_survey_dataset.csv")
    return df

df = load_data()

# Preprocess data
le_stress = LabelEncoder()
df["stress_level"] = le_stress.fit_transform(df["stress_level"])
df["has_supportive_relationships"] = df["has_supportive_relationships"].astype(int)
df["feels_purpose_in_life"] = df["feels_purpose_in_life"].astype(int)
df["meditates_or_relaxes_regularly"] = df["meditates_or_relaxes_regularly"].astype(int)

X = df.drop("happiness_index", axis=1)
y = df["happiness_index"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Streamlit UI
st.title("Happiness Index Predictor")
st.write("Answer the following questions:")

sleep = st.slider("How many hours do you sleep per day?", 0.0, 12.0, 7.0)
exercise = st.slider("How often do you exercise per week?", 0, 7, 3)
stress = st.selectbox("Your current stress level:", le_stress.classes_)
supportive = st.checkbox("Do you have supportive relationships?", value=True)
finance = st.slider("Rate your financial satisfaction (1-10):", 1, 10, 5)
worklife = st.slider("Rate your work-life balance (1-10):", 1, 10, 5)
purpose = st.checkbox("Do you feel a sense of purpose in life?", value=True)
social = st.slider("Meaningful social interactions per week:", 0, 20, 5)
health = st.slider("Rate your health (1-10):", 1, 10, 7)
meditate = st.checkbox("Do you meditate or relax regularly?", value=False)

input_data = np.array([[
    sleep,
    exercise,
    le_stress.transform([stress])[0],
    int(supportive),
    finance,
    worklife,
    int(purpose),
    social,
    health,
    int(meditate)
]])

if st.button("Predict Happiness Index"):
    prediction = model.predict(input_data)[0]
    st.success(f"🎯 Your predicted Happiness Index is: **{round(prediction, 2)} / 10**")
