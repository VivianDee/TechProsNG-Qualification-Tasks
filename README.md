# Task 1: Database Optimization

This is a comprehensive database optimization strategy for a large-scale online learning platform. The goal is to improve query performance and overall database efficiency.

# Task 2: RESTful API Development

This is a simple Flask API for user authentication yand course enrollment. It provides three endpoints: authentication, course enrollment, and user information retrieval. Users can authenticate using their username and password, enroll in courses, and retrieve their user information.

## Getting Started

These instructions will help you set up and run the API on your local machine.

### Prerequisites

- Python 3.5 or higher
- Flask (Install with `pip install Flask`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/VivianDee/TechProsNG-Qualification-Tasks.git
   ```

2. Change into the project directory:

   ```bash
   cd TechProsNG-Qualification-Tasks
   ```

### Usage

To run the API, use the following command:

```bash
python3 -m app
```

The API will start locally at `http://0.0.0.0:5000/`.

## API Endpoints

1. Authentication `/auth`
2. Course Enrollment `/enroll`
3. User Information Retrieval `/user/<int:user_id>`

## Example

You can use a tool like [curl](https://curl.se/) to interact with the API. Here's an example of how to authenticate a user using curl:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "user1", "password": "password1"}' http://0.0.0.0:5000/auth
```
