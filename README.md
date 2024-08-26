# CloudX-App

**CloudX-App** is a simple web application built using the Flask framework in Python. This project demonstrates basic web development concepts, including routing, handling URL parameters, and returning JSON responses. Additionally, it integrates with an SQLite database to showcase data persistence.

## Project Structure

- **`cloudx.py`**: The main application file containing the Flask routes and logic.
- **`init_db.py`**: Script to initialize the SQLite database.
- **`requirements.txt`**: List of dependencies required for the project.

## Routes and Functionality

1. **Home Route**
   - **Route**: `/`
   - **Method**: `GET`
   - **Description**: Returns a welcome message: "Welcome to the CloudX App!".

2. **Hello World Route**
   - **Route**: `/hello`
   - **Method**: `GET`
   - **Description**: Returns a simple greeting: "Hello, World!".

3. **JSON Response Route**
   - **Route**: `/api/data`
   - **Method**: `GET`
   - **Description**: Returns a JSON object containing information about the app:
     ```json
     {
         "name": "CloudX",
         "version": "1.0",
         "features": ["Flask", "API", "JSON"]
     }
     ```

4. **Dynamic Greeting Route**
   - **Route**: `/greet/<name>`
   - **Method**: `GET`
   - **Description**: Accepts a URL parameter (`<name>`) and returns a personalized greeting. For example, visiting `/greet/John` will respond with "Hello, John! Welcome to CloudX.".

5. **Data Submission Route**
   - **Route**: `/submit`
   - **Method**: `POST`
   - **Description**: Accepts data sent in a POST request as JSON and saves it to the SQLite database. Responds with a confirmation message and echoes back the received data.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/j-imran/cloudx-app.git
   cd cloudx-app
