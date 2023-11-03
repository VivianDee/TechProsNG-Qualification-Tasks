#!/usr/bin/python3
"""My Flask App"""
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated user data (will be replaced with a database)
users = [
    {"id": 1, "username": "user1", "password": "password1"},
    {"id": 2, "username": "user2", "password": "password2"},
]

courses = ["Course A", "Course B", "Course C"]

# Authentication
@app.route('/auth', methods=['POST'])
def authenticate_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = None

    for u in users:
        if u['username'] == username and u['password'] == password:
            user = u
            break

    if user:
        return jsonify({"message": "Authentication successful"})
    else:
        return jsonify({"message": "Authentication failed"})

# Course enrollment
@app.route('/enroll', methods=['POST'], strict_slashes=False)
def enroll_in_course():
    data = request.get_json()
    course = data.get('course')

    if course in courses:
        return jsonify({"message": "Enrollment successful"})
    else:
        return jsonify({"message": "Course not found"})

# User information retrieval
@app.route('/user/<int:user_id>', methods=['GET'], strict_slashes=False)
def get_user_info(user_id):
    user = None

    for u in users:
        if u['id'] == user_id:
            user = u
            break

    if user:
        return jsonify({"id": user['id'], "username": user['username']})
    else:
        return jsonify({"message": "User not found"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
