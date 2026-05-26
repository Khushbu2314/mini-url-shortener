# Mini URL Shortener

A small FastAPI-based URL shortener project with authentication and URL redirection.

## Repository Structure

```text
mini-url-shortener/
├── .gitignore
├── README.md
├── requirements.txt
├── .env
├── app/
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models/
│   │   ├── url.py
│   │   └── user.py
│   ├── routes/
│   │   ├── auth_routes.py
│   │   └── url_routes.py
│   ├── schemas/
│   │   ├── url_schema.py
│   │   └── user_schema.py
│   ├── services/
│   ├── utils/
│   │   ├── auth_bearer.py
│   │   ├── hash.py
│   │   ├── jwt_handler.py
│   │   └── shortener.py
│   └── screenshots/
└── venv/
```

## What each item does

- `.gitignore` - Excludes virtual environment files, caches, environment secrets, and local editor files from Git.
- `README.md` - Project overview, setup instructions, and GitHub upload guidance.
- `requirements.txt` - Python dependencies needed to run the project.
- `.env` - Local environment variables (keep private, do not commit).
- `app/config.py` - Configuration values used by the application.
- `app/database.py` - Database connection setup.
- `app/main.py` - FastAPI app entrypoint and route registration.

### Models
- `app/models/url.py` - URL data model for shortened links.
- `app/models/user.py` - User data model for authentication.

### Routes
- `app/routes/auth_routes.py` - Authentication endpoints for login/register.
- `app/routes/url_routes.py` - URL creation and redirect endpoints.

### Schemas
- `app/schemas/url_schema.py` - Request and response validation for URL operations.
- `app/schemas/user_schema.py` - Request and response validation for user/auth operations.

### Utilities
- `app/utils/auth_bearer.py` - Authentication dependency for protecting routes.
- `app/utils/hash.py` - Password hashing and verification.
- `app/utils/jwt_handler.py` - JWT generation and validation.
- `app/utils/shortener.py` - URL shortening and expansion logic.

### Services
- `app/services/` - Reserved for business logic and service-level helpers.

## Setup Instructions

1. Clone or download the repository.

2. Create and activate a Python virtual environment:

```powershell
python -m venv venv
.\\venv\\Scripts\\activate
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with values such as:

```text
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your_secret_key_here
```

5. Run the application with Uvicorn:

```powershell
uvicorn app.main:app --reload
```

6. Open the API in your browser or API client at:

```text
http://127.0.0.1:8000
```

## Task / Workflow Explanation

This project is built around a simple URL shortener workflow:

1. User authentication:
   - Users register and log in using the auth endpoints.
   - A JWT token is issued for authenticated requests.

2. URL shortening:
   - Authenticated users submit a full URL.
   - The service creates a short alias and stores it in the database.

3. Redirect handling:
   - When a short URL is visited, the app looks up the full URL.
   - The app redirects the user to the original destination.

4. Project structure workflow:
   - Models define the database objects.
   - Schemas define request/response validation.
   - Routes define the API endpoints.
   - Utils and services contain shared logic for auth, hashing, JWTs, and URL generation.


## Notes

- Keep `venv/`, `.env`, and `__pycache__/` out of Git.
- Update `README.md` when you add new features.
- Use meaningful commit messages for each change.
