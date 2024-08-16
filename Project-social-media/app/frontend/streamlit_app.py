import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import base64

from model_names_repo import image_ai_model_names,llm_model_names


# python -m streamlit run streamlit_app.py

API_URL = "http://localhost:8000"


st.title("Social Media Post Generation App")
txt_model_option = st.selectbox("Change text generator model", llm_model_names)
img_model_option = st.selectbox("Change image generator model", image_ai_model_names)

# Text inputs
platform_name = st.text_input("Social Media Platform Name", placeholder="Write Social Media Platform Name")
topic = st.text_input("Topic", placeholder="Write topic here...")
details = st.text_area("Details", placeholder="Write details here...")

input_data = {
        "social": platform_name,
        "topic": topic,
        "details": details
    }

col1, col2 = st.columns(2)

if 'image' not in st.session_state:
    st.session_state.image = None

if 'output_text' not in st.session_state:
    st.session_state.output_text = ""

with col1:
    st.subheader("Image Result")

    if st.button("Generate Image"):
        
        response = requests.post(f"{API_URL}/query/image", json={"query": input_data,
                                                                      "model_option_name":img_model_option})
        if response.status_code == 200:
            img_data = response.json()["response"]
            st.session_state.image = Image.open(BytesIO(base64.b64decode(img_data)))
        else:
            st.warning(f"Http error: {response.status_code}")
                
    if st.session_state.image:
        st.image(st.session_state.image, caption="Generated Image", use_column_width=True)
        
        img_byte_arr = BytesIO()
        st.session_state.image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        st.download_button(
            label="Download Image (PNG)",
            data=img_byte_arr,
            file_name="output_image.png",
            mime="image/png"
        )

with col2:
    st.subheader("Output Text")
    if st.button("Generate Text"):
        response = requests.post(f"{API_URL}/query/text", json={"query": input_data,
                                                                      "model_option_name":txt_model_option})
        
        if response.status_code == 200:
            st.session_state.output_text = response.json()["response"]
        else:
            st.warning(f"Http error: {response.status_code}")

    st.write(st.session_state.output_text)
