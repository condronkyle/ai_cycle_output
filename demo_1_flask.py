import flask
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Reuse the database connection function from CLI
def get_db_connection():
    conn = sqlite3.connect('friends.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-table', methods=['GET', 'POST'])
def create_table():
    if request.method == 'POST':
        table_name = request.form['tablename']
        columns = request.form['columns'].split(',')
        column_definitions = ', '.join([f"{col.strip()} TEXT" for col in columns])
        
        with get_db_connection() as conn:
            conn.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {column_definitions});")
        return redirect(url_for('index'))
    
    return render_template('create_table.html')

if __name__ == '__main__':
    app.run(debug=True)