from flask import Flask, render_template, request
from llm_agent import query_database

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    error  = None
    user_query = ""

    if request.method == "POST":

        user_query = request.form.get("query", "").strip()

        if user_query:
            try:
                result = query_database(user_query)
            except Exception as e:
                error = str(e)
        else:
            error = "Please enter a query."

    return render_template("index.html", result=result, error=error, user_query=user_query)

if __name__ == "__main__":
    app.run(debug=True)