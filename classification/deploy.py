import streamlit as st
import numpy as np
import pickle
from PIL import Image

# -------- PAGE CONFIG --------
st.set_page_config(page_title="Breast Cancer Prediction", layout="wide")

# -------- HEADER --------
st.markdown("""
<h1 style='text-align:center;'>🧬 Breast Cancer Prediction</h1>
<p style='text-align:center; color:gray;'>Early detection saves lives ❤️</p>
""", unsafe_allow_html=True)

# -------- SIDEBAR --------
st.sidebar.title("🧬 About App")
st.sidebar.info("""
This app predicts breast cancer risk using Machine Learning.

✔ 30 Medical Features  
✔ Instant Prediction  
✔ High Accuracy Model  
""")

# -------- IMAGE (FIX PATH) --------
image = Image.open(r"C:\Users\LENOVO\Downloads\Breast Cancer Prediction.png")  # keep image in project folder
st.image(image, use_container_width=True)

# -------- LOAD MODEL --------
model = pickle.load(open("model.pkl", "rb"))

# -------- FEATURE INPUT --------
st.markdown("## 📝 Enter Patient Details")

feature_names = [
'mean radius','mean texture','mean perimeter','mean area','mean smoothness',
'mean compactness','mean concavity','mean concave points','mean symmetry','mean fractal dimension',
'radius error','texture error','perimeter error','area error','smoothness error',
'compactness error','concavity error','concave points error','symmetry error','fractal dimension error',
'worst radius','worst texture','worst perimeter','worst area','worst smoothness',
'worst compactness','worst concavity','worst concave points','worst symmetry','worst fractal dimension'
]

# -------- COLUMNS (BETTER UI) --------
col1, col2, col3 = st.columns(3)

features = []
for i, name in enumerate(feature_names):
    if i % 3 == 0:
        value = col1.number_input(name, value=0.0)
    elif i % 3 == 1:
        value = col2.number_input(name, value=0.0)
    else:
        value = col3.number_input(name, value=0.0)
    features.append(value)

# -------- BUTTON STYLE --------
st.markdown("""
<style>
div.stButton > button {
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# -------- PREDICTION --------
if st.button("🔍 Predict Now"):
    input_data = np.array([features])
    prediction = model.predict(input_data)

    st.markdown("## 📊 Result")

    # -------- RESULT CARD --------
    if prediction[0] == 1:
        st.markdown("""
        <div style="
            background-color:#ff4d4d;
            padding:20px;
            border-radius:15px;
            text-align:center;
            color:white;
        ">
        <h2>🔴 Malignant (Cancer Detected)</h2>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="
            background-color:#2ecc71;
            padding:20px;
            border-radius:15px;
            text-align:center;
            color:white;
        ">
        <h2>🟢 Benign (No Cancer)</h2>
        </div>
        """, unsafe_allow_html=True)

    st.balloons()