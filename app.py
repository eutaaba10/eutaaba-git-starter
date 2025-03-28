import streamlit as st
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

# Vertex AI setup
PROJECT_ID = "eutaabatechx25-450919" 
LOCATION = "us-central1"  # Or another supported location
vertexai.init(project=PROJECT_ID, location=LOCATION)

st.title("Find your neighboring states")
users_state = st.text_input("Enter your state")

# Section A: Add in your Vertex AI API call below

if users_state:
    model = GenerativeModel("gemini-pro")
    prompt = f"What are the neighboring states of {users_state}?"
    response = model.generate_content(prompt)
    neighboring_states = response.text

# End of Section A

st.write("The neighboring states are:")

# Section B: Output the results to the user below

if users_state:
  st.write(neighboring_states)

# End of Section B