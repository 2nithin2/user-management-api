# User Management API

## Description

This project is a simple REST API built using the Django framework and Django REST Framework. It provides basic Create, Read, Update, and Delete (CRUD) operations for managing user data.

## Prerequisites

- Python 3.6+
- Pip (Python package installer)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/2nithin2/user-management-api.git
cd user-management-api
```

### 2. Create a virtual environment (recommended)

```bash
# On Linux/macOS
python -m venv venv
source venv/bin/activate
```

```powershell
# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Usage

### 1. Run the development server

```bash
python manage.py runserver
```

### 2. Access the API

The API will be available at **`http://localhost:8000/`**.  
You can use tools like **Postman**, **Insomnia**, or `curl` to interact with the API.

## API Endpoints

| Method  | Endpoint             | Description               | Request Body                                  | Response Body                                  |
|---------|----------------------|---------------------------|-----------------------------------------------|-----------------------------------------------|
| **GET**    | `/api/users/`      | Retrieve all users        | None                                          | JSON array of user objects                    |
| **POST**   | `/api/users/create/` | Create a new user        | `{"name": "John Doe", "age": 30}`             | JSON representation of the created user       |
| **GET**    | `/api/users/<id>/`  | Retrieve a specific user | None                                          | JSON representation of the user               |
| **PUT**    | `/api/users/<id>/`  | Update a specific user   | `{"name": "Jane Doe", "age": 35}`             | JSON representation of the updated user       |
| **DELETE** | `/api/users/<id>/`  | Delete a specific user   | None                                          | No content                                    |

## Database

⚠ **Do not commit `db.sqlite3` to the repository.**  
For production, use **PostgreSQL** or another robust database.

## Author

**Nithin Raj K.**  
GitHub: [2nithin2](https://github.com/2nithin2)
