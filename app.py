import streamlit as st
import joblib 
import numpy as np

model=joblib.load("forest_fire_model.pkl")
st.title("🔥 Forest Fire Risk Prediction System")
st.write("Enter environmental conditions to predict wildfire risk")

temperature=st.number_input("Temperature (°C)")
rh=st.number_input("Relative Humidity (RH)")
ws = st.number_input("Wind Speed")
rain = st.number_input("Rain")
ffmc = st.number_input("FFMC")
dmc = st.number_input("DMC")
dc = st.number_input("DC")
isi = st.number_input("ISI")
bui = st.number_input("BUI")
fwi = st.number_input("FWI")

if st.button("Predict Fire Risk"):
  input_data=np.array([temperature, rh, ws, rain,
        ffmc, dmc, dc, isi, bui, fwi
    ])
  prediction = model.predict([input_data])[0]
  probability = model.predict_proba([input_data])[0][1]
  if probability < 0.3:
    st.success("LOW RISK")
  elif probability < 0.7:
    st.warning("MODERATE RISK")
  else:
    st.error("HIGH RISK")
  st.write("Fire Probability:", round(probability * 100, 2), "%")
