import streamlit as st
from openai import OpenAI

# Load OpenAI API Key from Streamlit secrets
api_key = st.secrets["openai"]["api_key"]

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Streamlit UI
st.title("DALL·E Image Generator")
st.write("Enter a prompt to generate an AI image!")

# User input for image prompt
prompt = st.text_input("Enter your prompt:", "a white siamese cat")

# Generate Image Button
if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            image_url = response.data[0].url  # Get the image URL
            st.image(image_url, caption=prompt, use_container_width=True)
        except Exception as e:
            st.error(f"Error: {e}")