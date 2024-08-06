import dotenv
import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai

# Load environment variables securely (assuming a .env file exists)
dotenv.load_dotenv()

# Configure Google Generative AI using the API key from the environment
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, image):
    """Generates a response using the Gemini model, incorporating input text and image."""

    model = genai.GenerativeModel('gemini-pro-vision')
    if input_text:  # Check if input text is provided
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Image Demo", page_icon=":image:")  # Set a custom icon

def main():
    """Main function to organize the Streamlit app structure."""

    st.header("**Welcome to the Gemini Image App!**")  # Use bold and italics for emphasis

    uploaded_file = st.file_uploader("️ Choose an image...", type=["jpg", "jpeg", "png"])
    image = None

    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
        except Exception as e:
            st.error(f"Error opening image: {e}")  # Handle potential image opening errors

    input_text = st.text_input("  Input Prompt:", key="input")

    if submit := st.button("🪄 Tell me about the image"):
        if image:
            response = get_gemini_response(input_text, image)
            st.subheader("**The Response is:**")
            st.write(response)
        else:
            st.warning("Please upload an image to proceed.")

if __name__ == "__main__":
    main()
