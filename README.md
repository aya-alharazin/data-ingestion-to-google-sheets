# Data Ingestion to Google Sheets

## 📌 Overview
This project is a **Flask-based web application** designed to automate the ingestion of unstructured student data into **Google Sheets**.

It was developed as a **freelancing solution** for **MET Academy**, where student information is typically received as free-text messages (for example via WhatsApp).  
Instead of manually copying, cleaning, and organizing this data, the application parses the messages and synchronizes them directly into a structured Google Sheet.

---

## 🚨 The Problem
MET Academy receives student data in **unstructured text format**, such as:

- Name
- University branch
- Major
- Section number
- Level
- WhatsApp contact
- Desired courses

### Manual Workflow Issues:
- ❌ Copy–paste errors  
- ❌ Inconsistent formatting  
- ❌ Time-consuming data entry  
- ❌ Difficult to analyze or filter later  

This manual process wastes time and increases the risk of data inconsistency.

---

## ✅ The Solution
This application automates the entire process by:

1. Accepting **raw text input** through a web form
2. **Parsing** the message into structured key–value pairs
3. **Validating and formatting** the data
4. **Synchronizing** the cleaned data into Google Sheets automatically

---

## 🧠 How It Works
1. The user pastes the full student message into a single input form
2. The Flask backend:
   - Splits the message line by line
   - Extracts fields using a `key: value` pattern
3. The parsed data is appended as a new row in Google Sheets
4. WhatsApp links are auto-generated for easy contact

---

## 🛠 Tech Stack
- **Python**
- **Flask**
- **Google Sheets API**
- **gspread**
- **Google Service Account Authentication**
- render

---

## 📂 Project Structure
```text
.
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignored files (credentials, venv, etc.)
├── README.md           # Project documentation
