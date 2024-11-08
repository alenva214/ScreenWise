from flask import Flask, request, redirect, url_for, session, send_from_directory, jsonify,render_template
import mysql.connector
from mysql.connector import Error
import hashlib
import os
from datetime import datetime, date
from calendar import monthrange



app = Flask(__name__)
app.secret_key = 'AlenVA'  # Change this to a random secret key

# Database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'screen_time_tracker'
}

def get_db_connection():
    try:
        return mysql.connector.connect(**db_config)
    except Error as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')
@app.route('/login')
def logi():
    return send_from_directory('public', 'login.html')


@app.route('/register')
def reg():
    return send_from_directory('public', 'register.html')
@app.route('/leaderboard')
def leader():
    return send_from_directory('public', 'leaderboard.html')

@app.route('/dashboard')
def user():
    return send_from_directory('public', 'dashboard.html')
@app.route('/profile')
def prof():
    return send_from_directory('public', 'profile.html')

@app.route('/marketplace')
def market():
    return send_from_directory('public', 'marketplace.html')
@app.route('/quest')
def quest():
    return send_from_directory('public', 'quest.html')



@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # Get JSON data from the request
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # Check if email and password are provided
        if not email or not password:
            return jsonify({"success": False, "message": "Email and password are required."}), 400

        # Connect to the MySQL database
        conn = get_db_connection()
        if conn is None:
            return jsonify({"success": False, "message": "Database connection failed"})
        
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users WHERE email = %s AND password_hash = %s", (email, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        # Check if the user was found
        if user:
            # Respond with a success message
            return jsonify({"success": True, "message": "Login successful"})
        else:
            # Respond with an error message if invalid credentials
            return jsonify({"success": False, "message": "Invalid credentials. Please try again."}), 401

    # If the request method is GET (for rendering the login page)
    return render_template('login.html')
# Register route
@app.route('/register1', methods=['POST'])
def register():
    if request.method == 'POST':
        # Get the data from the request body (assuming JSON format)
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        user= data.get('username')
        if not email or not password:
            return jsonify({"success": False, "message": "Email and password are required."})

        # Get database connection
        conn = get_db_connection()
        if conn is None:
            return jsonify({"success": False, "message": "Database connection failed"})
        
        cursor = conn.cursor(dictionary=True)
        
        # Insert the user data into the database
        cursor.execute("INSERT INTO users (username,email, password_hash) VALUES (%s, %s,%s)", (user,email, password))
        conn.commit()
        cursor.close()
        conn.close()

        # Return success response
        return jsonify({"success": True, "message": "Registration successful! Please login."})

    return jsonify({"success": False, "message": "Invalid request method."})
# Serve static files
@app.route('/public/<path:path>')
def serve_static(path):
    return send_from_directory('public', path)



if __name__ == "__main__":
    app.run(debug=True)