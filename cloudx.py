from flask import Flask, jsonify, request, g
import sqlite3

app = Flask(__name__)
DATABASE = 'cloudx.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return "Welcome to the CloudX App!"

@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/api/data')
def api_data():
    return jsonify({
        "name": "CloudX",
        "version": "1.0",
        "features": ["Flask", "API", "JSON"]
    })

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! Welcome to CloudX."

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')

    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO data (key, value) VALUES (?, ?)', (key, value))
    db.commit()

    return jsonify({
        "message": "Data received and saved to database!",
        "data": data
    })

if __name__ == '__main__':
    app.run(debug=True)
