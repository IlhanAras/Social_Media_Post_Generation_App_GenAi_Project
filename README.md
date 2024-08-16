
# Social Media Post Generator App

This project is a web application that generates social media posts, including both text and images, using advanced AI models. The app is built using **FastAPI** for the backend, **Streamlit** for the frontend, and incorporates **LangChain** for text generation and Stable Diffusion for image creation. The application features **8 different LLM models** for generating text content and **2 image generation models** for creating visually appealing images.
# Screenshots

![Ekran görüntüsü 2024-08-16 140452](https://github.com/user-attachments/assets/e35e83f3-0d25-4f35-815f-095a08506aee)

![Ekran görüntüsü 2024-08-16 135850](https://github.com/user-attachments/assets/5590756c-d5ef-4991-828a-9cffb2c9024a)


#
## Features
* Text Generation:

    * Utilizes the following LLM models for generating high-quality, contextually relevant social media posts:
        * gemma-7b-it
        * gemma2-9b-it
        * llama-3.1-70b-versatile
        * llama-3.1-8b-instant
        * llama3-70b-8192
        * llama3-8b-8192
        * llama3-groq-70b-8192-tool-use-preview
        * mixtral-8x7b-32768
    * Users can customize the generated text based on the social media platform, topic, and additional details.
* Image Generation:

    * Generates visually engaging images using the following Stable Diffusion models:
        * dreamlike-art/dreamlike-diffusion-1.0
        * CompVis/stable-diffusion-v1-4
    * Customizable based on the topic and specific visual elements required.

* Streamlit Frontend:

    * Provides an intuitive and interactive UI for generating text and images.
    * Allows users to select different AI models for text and image generation.
* FastAPI Backend:

    * Handles API requests for text and image generation.
    * Processes and returns the generated content in a structured format.

# Getting Started

## Prerequisites
* Python 3.8+
* Pipenv or another package manager
* CUDA-compatible GPU (for optimal performance with the Stable Diffusion model)

# Installation

1.Clone the repository:

    https://github.com/IlhanAras/Social_Media_Post_Generation_App_GenAi_Project.git
    
    cd Social_Media_Post_Generation_App_GenAi_Project

2.Set up environment variables:
* Create a .env file in the root directory.
* Add your [Groq Api](https://groq.com) API key

3.Run the FastAPI server:

    python -m uvicorn fastapi_app:app --reload

4.Run the Streamlit app:

    python -m streamlit run streamlit_app.py
# 
