import streamlit as st
import pickle
import pandas as pd
from PIL import Image
import urllib.parse
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent

# Load CSS for styling
with open(APP_DIR / 'css' / 'style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with (APP_DIR / 'medicine_records.pkl').open('rb') as medicine_file:
    medicines_dict = pickle.load(medicine_file)
medicines = pd.DataFrame(medicines_dict)

with (APP_DIR / 'medicine_neighbors.pkl').open('rb') as neighbors_file:
    medicine_neighbors = pickle.load(neighbors_file)

def recommend(medicine):
    matches = medicines.index[medicines['Drug_Name'] == medicine]
    if matches.empty:
        return []

    neighbor_indices = medicine_neighbors[int(matches[0])]
    return medicines.iloc[neighbor_indices]['Drug_Name'].tolist()

# Title
st.markdown('<h1 style="font-size: 38.5px;" class="stTitle">JanAushadhi Medicine Recommender</h1>', unsafe_allow_html=True)

# Searchbox
selected_medicine_name = st.selectbox(
    'Type your medicine name whose alternative is to be recommended',
    medicines['Drug_Name'].values
)

# Recommendation Program
if st.button('Recommend Medicine', key='recommend', help="Click to get recommendations"):
    recommendations = recommend(selected_medicine_name)
    for idx, medicine in enumerate(recommendations, 1):
        # Encode the medicine name for URL
        encoded_medicine = urllib.parse.quote_plus(medicine)
        st.markdown(f"""
            <div class="recommendation">
                <p>{idx}. {medicine}</p>
                <ul>
                    <li><a href="https://janaushadhistore.online/?s={encoded_medicine}" target="_blank">Buy on Janaushadhi Store</a></li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

# Image load
image = Image.open(APP_DIR / 'images' / 'bg.webp')
st.image(image, caption='Recommended Medicines', use_column_width=True)
