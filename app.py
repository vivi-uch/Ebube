from flask import Flask, render_template, request
import sqlite3
from calc import create_db, save_record 
from size import calculate_real_size

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    create_db()
    result = None
    if request.method == 'POST':
        try:
            username = request.form['username']
            microscope_size = float(request.form['microscope_size'])
            magnification = float(request.form['magnification'])
            actual_size = calculate_real_size(microscope_size, magnification)
            save_record(username, microscope_size, magnification, actual_size)
            result = f"Real-life size: {actual_size:.2f} mm"
        except ValueError:
            result = "Invalid input. Please enter valid numbers."
    return render_template('index.html', result=result)

@app.route("/result")
def view_data():
    conn = sqlite3.connect("specimen_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM specimens")
    data = cursor.fetchall()
    conn.close()
    return render_template("result.html", data=data)
