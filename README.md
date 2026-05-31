# 🩺 Health Prediction Application

An AI-powered health prediction and patient management system built using Streamlit, SQLite, SQLAlchemy, and Google's Gemini AI.

## Features

- Add patient records
- View patient records
- Update patient records
- Delete patient records
- Input validation
- SQLite database integration
- AI-generated health remarks using Gemini
- User-friendly Streamlit interface

## Tech Stack

- Python
- Streamlit
- SQLite
- SQLAlchemy
- Google Gemini API
- Pandas

## Project Structure

health_prediction_app/

├── app.py

├── database.py

├── model.py

├── requirements.txt

├── README.md

├── .gitignore

└── .env

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Gemini API Key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### Run Application

```bash
streamlit run app.py
```

## Example Health Analysis

Input:

- Glucose: 140
- Haemoglobin: 13.5
- Cholesterol: 180

Output:

- Elevated glucose detected
- Possible metabolic health risk
- Personalized recommendation generated using Gemini AI

## Future Enhancements

- Authentication system
- PDF health reports
- Health trend visualizations
- Cloud deployment

## Author

Yaminisri Thota