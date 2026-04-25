from flask import Flask, render_template
from model import init_db, get_all_students

app = Flask(__name__)

@app.route("/")
def index():
    students = get_all_students()       # fetch from Model
    return render_template("index.html", students=students)  # send to View

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
