# AI-Powered Business Analyst

A simple, modern Streamlit application that converts raw business ideas or requirements into structured Business Analysis documentation using the Gemini API.

## Features
- Minimalist, one-page modern UI.
- Powered by `gemini-1.5-pro` via the Google Generative AI SDK.
- Automatically generates essential BA sections: Project Summary, Business Objective, User Stories, Acceptance Criteria, Tech Stack, and more.
- One-click download of the generated documentation as Markdown.

## Setup Instructions

### 1. Clone or Download the Repository
Navigate to the project directory:
```bash
cd Business-Analyst
```

### 2. Create a Virtual Environment (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
- Copy the `.env.example` file to a new file named `.env`:
  ```bash
  cp .env.example .env
  ```
  *(On Windows, you can simply rename the file or copy it using File Explorer)*
- Open `.env` and add your Google Gemini API Key:
  ```
  GEMINI_API_KEY=your_actual_api_key_here
  ```
  *(You can get a Gemini API key from Google AI Studio)*

### 5. Run the Application
```bash
streamlit run app.py
```
The application will open in your default browser at `http://localhost:8501`.
