#  Health Prediction Application

An AI-powered patient management system that collects blood test results, stores patient records, and generates intelligent health remarks using **Google Gemini 2.5 Flash**.

---

## Features

- **CRUD operations** — Create, Read, Update, and Delete patient records
- **AI-generated health remarks** — Powered by Google Gemini 2.5 Flash; falls back to rule-based logic if the API is unavailable
- **Input validation** — Email format check, future date prevention, numeric blood value enforcement, and duplicate email detection
- **Persistent storage** — SQLite database via SQLAlchemy ORM
- **Clean UI** — Built with Streamlit; no frontend setup required

---

## Tech Stack

| Layer | Technology | Reason |
|---|---|---|
| Frontend / UI | Streamlit | Rapid Python-native UI; no JavaScript required |
| Backend | Python 3.11+ | Core language for all logic |
| Database | SQLite + SQLAlchemy | Lightweight, file-based, ORM-managed |
| AI API | Google Gemini 2.5 Flash | Fast inference, free-tier access, concise medical remarks |
| Config | python-dotenv | Keeps API keys out of source code |

---

## Patient Record Fields

| Field | Type | Notes |
|---|---|---|
| Full Name | Text | Required |
| Date of Birth | Date | Cannot be a future date |
| Email Address | Text | Must be valid format; unique per record |
| Glucose | Float | mg/dL; must be numeric |
| Haemoglobin | Float | g/dL; must be numeric |
| Cholesterol | Float | mg/dL; must be numeric |
| Remarks | Text | AI-generated health assessment |

---

## Project Structure

```
health-prediction-app/
├── app.py            # Streamlit UI — all pages and form logic
├── database.py       # SQLAlchemy models and CRUD functions
├── model.py          # Gemini API integration and fallback prediction
├── requirements.txt  # Python dependencies
├── .env              # API key (not committed to Git)
├── .gitignore        # Excludes .env, *.db, __pycache__
└── README.md
```

---

## Setup & Installation

### Prerequisites

- Python 3.11 or above
- A [Google AI Studio](https://aistudio.google.com/) account for a free Gemini API key

### 1. Clone the repository

```bash
git clone hhttps://github.com/yaminisri2003/health-prediction-app
cd health-prediction-app
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

>  Never commit `.env` to Git. It is listed in `.gitignore`.

### 5. Run the application

```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

---

## AI Integration

When a patient record is saved or updated, the application sends the blood test values to **Gemini 2.5 Flash** with a healthcare-focused prompt:

```
Patient Blood Test Results:
  Glucose: {value}
  Haemoglobin: {value}
  Cholesterol: {value}

Provide a short health assessment, possible risks, and a recommendation.
Keep it under 40 words as a single concise paragraph.
```

If the API call fails for any reason, the app falls back to a simple rule-based prediction:

| Condition | Remark |
|---|---|
| Glucose > 125 | High risk of Diabetes |
| Cholesterol > 240 | High Cholesterol Risk |
| Haemoglobin < 12 | Possible Anaemia Risk |
| Otherwise | Healthy |

---

## Data Validation Rules

| Field | Rule |
|---|---|
| Full Name | Cannot be empty |
| Email | Must match standard email format; must be unique |
| Date of Birth | Cannot be today or a future date |
| Glucose / Haemoglobin / Cholesterol | Must be numeric (≥ 0) |

---

## Dependencies

```
streamlit
pandas
sqlalchemy
python-dotenv
google-genai
```

Install all with:

```bash
pip install -r requirements.txt
```

---

## Security Notes

- The API key is loaded from a `.env` file using `python-dotenv` and is never hardcoded
- `.env` and `health_data.db` are excluded from version control via `.gitignore`
- No sensitive data is logged or exposed in the UI

---

## Known Limitations

- The application is designed for demonstration purposes and is not a substitute for professional medical advice
- SQLite is used for simplicity; a production deployment would use PostgreSQL or MySQL
- Gemini API responses may vary; the 40-word prompt constraint helps ensure consistency

---

