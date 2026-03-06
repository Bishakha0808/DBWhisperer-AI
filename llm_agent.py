import os
from urllib.parse import quote_plus
from google import genai
from sqlalchemy import create_engine, text

# ── Database configuration ──────────────────────────────────────────────────
DB_USER     = os.getenv("DB_USER",     "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "Bb#2004@")
DB_HOST     = os.getenv("DB_HOST",     "localhost")
DB_NAME     = os.getenv("DB_NAME",     "student_portal")

engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}/{DB_NAME}"
)

# ── Gemini client ────────────────────────────────────────────────────────────
client = genai.Client(api_key="AIzaSyBA4bzi9JrgU_OWZLCzZSP3h8hlh2Iu_GE")
MODEL = "gemini-flash-latest"

DB_SCHEMA = """
Table: students
Columns:
  id         INT  PRIMARY KEY AUTO_INCREMENT
  name       VARCHAR(50)
  department VARCHAR(50)   -- values: CSE, IT, ECE
  marks      INT
"""

# ── Core function ────────────────────────────────────────────────────────────
def query_database(user_query: str) -> str:
    try:
        # Step 1: natural language → SQL
        sql_prompt = f"""You are a MySQL expert. Convert the user question into a valid MySQL SELECT query for the schema below.
Return ONLY the raw SQL query — no markdown, no code fences, no explanation.

Schema:
{DB_SCHEMA}

Question: {user_query}"""

        sql_resp = client.models.generate_content(model=MODEL, contents=sql_prompt)
        sql_query = sql_resp.text.strip().strip("```sql").strip("```").strip()

        # Step 2: execute SQL
        with engine.connect() as conn:
            result = conn.execute(text(sql_query))
            columns = list(result.keys())
            rows    = result.fetchall()

        if not rows:
            return "No results found."

        # Step 3: format raw table
        header = " | ".join(columns)
        divider = "-" * len(header)
        body    = "\n".join(" | ".join(str(v) for v in row) for row in rows)
        raw_table = f"{header}\n{divider}\n{body}"

        # Step 4: ask Gemini to explain in plain English
        explain_prompt = f"""The user asked: "{user_query}"
SQL executed: {sql_query}
Result:
{raw_table}

Summarise this result in one or two clear, friendly sentences."""

        explain_resp = client.models.generate_content(model=MODEL, contents=explain_prompt)
        return explain_resp.text.strip()

    except Exception as e:
        return f"Error processing query: {e}"
