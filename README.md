# DBWhisperer-AI
Meaning: “Ask the database in natural language and it responds intelligently.”

# QueryMind — Natural Language Database Interaction with LLMs

> **Experiment 8** | AI Lab Project  
> Ask your MySQL database questions in plain English — powered by Google Gemini AI.

---

## Overview

QueryMind is a Flask web application that lets users interact with a MySQL database using natural language. It uses the **Google Gemini API** to convert plain English questions into SQL queries, executes them against the database, and returns a human-friendly summary of the results.


![Image](https://github.com/Bishakha0808/DBWhisperer-AI/blob/main/Screenshot%202026-03-06%20201343.png)


### How It Works

```
User Question
     │
     ▼
Gemini AI → generates SQL query
     │
     ▼
MySQL Database → executes query → raw results
     │
     ▼
Gemini AI → summarises results in plain English
     │
     ▼
Answer displayed in browser
```

---

## Features

- Natural language to SQL conversion using Gemini Flash
- Direct MySQL query execution via SQLAlchemy
- Plain-English answer summarisation
- Professional responsive UI with Bootstrap 5
- Clickable sample query suggestions
- Loading spinner while AI is processing
- Error handling for invalid queries

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, Bootstrap 5, Bootstrap Icons |
| Backend | Python, Flask |
| AI / LLM | Google Gemini API (`gemini-flash-latest`) |
| Database | MySQL |
| ORM / DB Driver | SQLAlchemy, mysql-connector-python |

---

## Project Structure

```
├── app.py              # Flask routes & request handling
├── llm_agent.py        # Gemini AI integration & SQL execution
├── sql.sql             # Database schema & seed data
├── requirements.txt    # Python dependencies
└── templates/
    └── index.html      # Frontend UI
```

---

## Database Schema

```sql
CREATE TABLE students (
    id         INT PRIMARY KEY AUTO_INCREMENT,
    name       VARCHAR(50),
    department VARCHAR(50),
    marks      INT
);
```

**Sample data:** Rahul (CSE, 85), Ananya (IT, 90), Rohit (CSE, 78), Priya (ECE, 88), Arjun (CSE, 92)

---

## Setup & Installation

### Prerequisites

- Python 3.10+
- MySQL Server running locally
- A Google Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/querymind.git
cd querymind
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

### 4. Set up the MySQL database

Open MySQL and run:

```sql
CREATE DATABASE student_portal;
USE student_portal;
SOURCE sql.sql;
```

### 5. Configure credentials

Edit `llm_agent.py` and update:

```python
DB_PASSWORD = "your_mysql_password"
client = genai.Client(api_key="your_gemini_api_key")
```

Or set environment variables:

```bash
# Windows PowerShell
$env:DB_PASSWORD = "your_mysql_password"
$env:GOOGLE_API_KEY = "your_gemini_api_key"
```

### 6. Run the application

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

---

## Example Queries

| Natural Language | Generated SQL |
|---|---|
| List all students | `SELECT * FROM students` |
| Who is in CSE? | `SELECT * FROM students WHERE department = 'CSE'` |
| Who scored the highest marks? | `SELECT * FROM students ORDER BY marks DESC LIMIT 1` |
| Average marks by department | `SELECT department, AVG(marks) FROM students GROUP BY department` |

---

## Requirements

```
flask>=3.0.0
google-genai>=1.0.0
mysql-connector-python>=8.0.0
sqlalchemy>=2.0.0
```


