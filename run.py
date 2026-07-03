from app import create_app
from app.config import get_db_connection
from flask import render_template

app = create_app()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test-db")
def test_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 'Database Connected!'")
    result = cursor.fetchone()
    conn.close()
    return result[0]

if __name__ == "__main__":
    app.run(debug=True)