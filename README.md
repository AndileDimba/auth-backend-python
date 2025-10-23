## Overview

This is the backend API built with FastAPI and MySQL. It provides user authentication, registration, and profile management.

---

## Prerequisites

- Python 3.10 or later  
- MySQL server (or compatible)  
- Virtual environment tool (recommended)

---

## Setup

1. Clone the repository (if not done already):

```bash
git clone https://github.com/AndileDimba/auth-backend-python.git
cd backend
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# On Linux/macOS
source venv/bin/activate
# On Windows (cmd)
venv\Scripts\activate.bat
# On Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the backend root directory with the following variables:

```env
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Adjust values as needed.

---

## Running the Development Server

Start the FastAPI server with auto-reload:

```bash
uvicorn app.main:app --reload
```

The API will be available at [http://localhost:8000](http://localhost:8000).

---

## API Endpoints

- `POST /auth/register` — Register a new user  
- `POST /auth/login` — Login and receive JWT token  
- `GET /me` — Get current user info (requires authentication)  
- `PATCH /user/update` — Update user profile (requires authentication)  

---

## Database

- Uses MySQL with SQLAlchemy ORM  
- Ensure your database is running and accessible with the credentials in `.env`  
- Tables are created automatically on app startup  

---

## Environment Variables

- `DATABASE_HOST`, `DATABASE_PORT`, `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD` — MySQL connection  
- `SECRET_KEY` — JWT secret key (keep this secure)  
- `ALGORITHM` — JWT algorithm (default: HS256)  
- `ACCESS_TOKEN_EXPIRE_MINUTES` — Token expiration time in minutes  

---

## Authentication Flow

- User registers via `/auth/register`  
- User logs in via `/auth/login` and receives JWT token  
- Token is used in `Authorization: Bearer <token>` header for protected endpoints  
- `/me` and `/user/update` require valid token  

---

## Notes

- Passwords are hashed securely using bcrypt or argon2  
- No user deletion endpoint implemented yet  
- Ensure CORS is configured to allow frontend origin  

---

## Trade-offs
- I used name for first_name and username for last_name because I was using a hosted database on a free site, and I cannot make a lot of changes to the table structure.

## Troubleshooting

- If database connection fails, verify `.env` credentials and MySQL server status  
- Check logs for detailed error messages  
- Use Postman or curl to test endpoints independently  
- Clear tokens or restart server if authentication issues occur  

---
