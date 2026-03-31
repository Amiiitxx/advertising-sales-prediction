import streamlit as st
import pickle
import numpy as np
from PIL import Image

st.set_page_config(page_title="Ad Sales Predictor", layout="wide")

st.markdown("""
<h1 style='text-align:center;'>📊 Advertising Sales Prediction</h1>
<p style='text-align:center; color:gray;'>Predict sales based on marketing budget</p>
""", unsafe_allow_html=True)

st.sidebar.title("📌 About")
st.sidebar.info("""
This app predicts product sales based on advertising spend.

Channels:
✔ TV 📺  
✔ Radio 📻  
✔ Newspaper 📰  
""")


image = Image.open(r"C:\Users\LENOVO\Downloads\Advertising Dataset.png")  
st.image(image, use_container_width=True)


model = pickle.load(open("advertising_model.pkl","rb"))
st.markdown("## 💰 Enter Advertising Budget")
#pickle.dump(model,open("advertising_model.pkl","wb"))
#pickle.dump(grid,open("advertising_grid.pkl","wb"))
col1, col2, col3 = st.columns(3)

with col1:
    tv = st.slider("📺 TV Budget", 0.0, 300.0, 0.0)

with col2:
    radio = st.slider("📻 Radio Budget", 0.0, 50.0, 0.0)

with col3:
    news = st.slider("📰 Newspaper Budget", 0.0, 120.0, 0.0)

st.markdown("""
<style>
div.stButton > button {
    background: linear-gradient(to right, #ff7e5f, #feb47b);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)
if st.button("🚀 Predict Sales"):

    data = np.array([[tv, radio, news]])
    prediction = model.predict(data)[0]

    st.markdown("## 📈 Prediction Result")
    st.markdown(f"""
    <div style="
        background-color:#1f77b4;
        padding:25px;
        border-radius:15px;
        text-align:center;
        color:white;
        box-shadow: 0 0 20px rgba(0,0,0,0.2);
    ">
    <h2>💰 Predicted Sales</h2>
    <h1>{prediction:.2f}</h1>
    </div>
    """, unsafe_allow_html=True)

    st.progress(int(prediction * 5))

    st.balloons()