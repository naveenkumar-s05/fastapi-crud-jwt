# FastAPI CRUD Application with JWT Authentication

## Project Overview

A REST API built using FastAPI and PostgreSQL that supports user registration, login, JWT-based authentication, and task management. Each authenticated user can manage their own tasks.

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT authentication using python-jose
- Passlib and bcrypt for password hashing
- Uvicorn
- python-dotenv

## Features

- User registration with password hashing
- User login and JWT access token generation
- Protected endpoints using JWT authentication
- Create, read, update, and delete tasks
- User-specific task ownership
- Request validation using Pydantic
- Interactive API documentation using Swagger UI

## Project Structure

```text
fastapi_crud_project/
├── app/
│   ├── routers/
│   │   ├── auth.py
│   │   ├── tasks.py
│   │   └── users.py
│   ├── auth.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd fastapi_crud_project
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and update the values for your local environment.

### 5. Create the PostgreSQL database

Create a database named `fastapi_crud` and configure your PostgreSQL username, password, host, and port in `.env`.

### 6. Start the application

```powershell
uvicorn app.main:app --reload
```

### 7. Open Swagger UI

Visit http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/auth/register` | Register a user |
| POST | `/auth/login` | Authenticate and obtain a JWT |
| GET | `/users/me` | Retrieve the current user |
| POST | `/tasks/` | Create a task |
| GET | `/tasks/` | List tasks |
| GET | `/tasks/{task_id}` | Retrieve a task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Security

- Passwords are hashed before storage.
- Protected endpoints require JWT authentication.
- Environment variables are stored in `.env`.
- The real `.env` file must never be committed to version control.

## Author

Naveen Kumar S