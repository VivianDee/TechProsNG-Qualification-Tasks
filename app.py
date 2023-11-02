#!/usr/bin/python3
"""My Flask App"""
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated user data (you would replace this with your database)
users = [
    {"id": 1, "username": "user1", "password": "password1"},
    {"id": 2, "username": "user2", "password": "password2"},
]

courses = ["Course A", "Course B", "Course C"]

# Authentication endpoint
@app.route('/auth', methods=['POST'])
def authenticate_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = next((u for u in users if u['username'] == username and u['password'] == password), None)

    if user:
        return jsonify({"message": "Authentication successful"})
    else:
        return jsonify({"message": "Authentication failed"}, 401)

# Course enrollment endpoint
@app.route('/enroll', methods=['POST'])
def enroll_in_course():
    data = request.get_json()
    course = data.get('course')

    if course in courses:
        return jsonify({"message": "Enrollment successful"})
    else:
        return jsonify({"message": "Course not found"}, 404)

# User information retrieval endpoint
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_info(user_id):
    user = next((u for u in users if u['id'] == user_id), None)

    if user:
        return jsonify({"id": user['id'], "username": user['username']})
    else:
        return jsonify({"message": "User not found"}, 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000, debug=True)
