import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Streamlit page
st.set_page_config(
    page_title="AI Business Analyst",
    page_icon="💼",
    layout="centered"
)

# Initialize Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.warning("⚠️ GEMINI_API_KEY not found. Please add it to your .env file.")

def generate_ba_document(requirement: str) -> str:
    """
    Calls the Gemini API to generate structured BA documentation based on the user's requirement.
    """
    # Use the recommended model for general text tasks
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    
    prompt = f"""
You are an expert Business Analyst. A client has provided the following raw business requirement or idea:

"{requirement}"

Your task is to analyze this requirement and produce a structured Business Analysis document.
Please format your response using Markdown, with the following clearly defined sections:

## 1. Project Summary
## 2. Business Objective
## 3. Functional Requirements
## 4. Non-Functional Requirements
## 5. User Stories
## 6. Acceptance Criteria
## 7. Suggested Workflow
## 8. Suggested Tech Stack
## 9. Risks/Challenges

Keep the language professional, clear, and actionable. Avoid unnecessary jargon.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred while generating the document: {e}"

# UI Elements
st.title("💼 AI-Powered Business Analyst")
st.markdown("""
Welcome! Enter a raw business idea or requirement below, and the AI will convert it into a structured Business Analysis document.
""")

# Input section
user_requirement = st.text_area(
    "Enter your business requirement:",
    height=150,
    placeholder="Example: I want customers to receive WhatsApp notifications after placing an order."
)

# Generation button
if st.button("Generate Analysis", type="primary"):
    if not api_key:
        st.error("Please configure your GEMINI_API_KEY first.")
    elif not user_requirement.strip():
        st.error("Please enter a business requirement before generating.")
    else:
        with st.spinner("Analyzing requirement and drafting documentation..."):
            result = generate_ba_document(user_requirement)
            
            st.success("Analysis Complete!")
            
            # Display the result in an expander or container
            with st.container():
                st.markdown("---")
                st.markdown(result)
                st.markdown("---")
                
            # Allow user to download the generated markdown
            st.download_button(
                label="Download as Markdown",
                data=result,
                file_name="Business_Analysis_Document.md",
                mime="text/markdown"
            )
