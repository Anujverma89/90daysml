import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Generate synthetic data
def load_data():
    np.random.seed(42)
    n_samples = 500
    humidity = np.random.uniform(20, 100, n_samples)
    pressure = np.random.uniform(980, 1050, n_samples)
    wind_speed = np.random.uniform(0, 15, n_samples)
    temperature = 30 - 0.1 * humidity + 0.05 * pressure - 0.3 * wind_speed + np.random.normal(0, 2, n_samples)
    df = pd.DataFrame({
        'Humidity': humidity,
        'Pressure': pressure,
        'Wind Speed': wind_speed,
        'Temperature': temperature
    })
    return df

# Load and train
df = load_data()
X = df[['Humidity', 'Pressure', 'Wind Speed']]
y = df['Temperature']
model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.title("🌡️ Temperature Prediction App")

st.write("Provide the following inputs and click **Predict** to estimate the temperature:")

# Inputs
humidity = st.slider("Humidity (%)", 20.0, 100.0, 60.0)
pressure = st.slider("Pressure (hPa)", 980.0, 1050.0, 1013.0)
wind_speed = st.slider("Wind Speed (m/s)", 0.0, 15.0, 5.0)

# Predict button
if st.button("🔍 Predict"):
    input_data = np.array([[humidity, pressure, wind_speed]])
    predicted_temp = model.predict(input_data)[0]
    st.success(f"🌡️ Predicted Temperature: **{predicted_temp:.2f} °C**")
