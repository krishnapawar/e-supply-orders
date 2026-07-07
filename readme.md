# FastAPI E-Commerce API

A production-ready FastAPI backend project using PostgreSQL, SQLAlchemy, Alembic, Docker, JWT Authentication, and Repository Pattern.

---

# Prerequisites

Before starting, install:

- Python 3.11+
- Git
- Docker & Docker Compose
- PostgreSQL (Optional if using Docker)

---

# Create Virtual Environment

```bash
python -m venv venv
```

---

# Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

# Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

# Install FastAPI

```bash
pip install fastapi uvicorn
```

---

# Install Database Packages

```bash
pip install sqlalchemy alembic psycopg2-binary python-dotenv
```

### Package Explanation

| Package | Purpose |
|---------|---------|
| SQLAlchemy | ORM (similar to Laravel Eloquent) |
| Alembic | Database migrations (similar to Laravel migrations) |
| psycopg2-binary | PostgreSQL database driver |
| python-dotenv | Load environment variables from `.env` |

---

# Install Authentication Packages

```bash
pip install python-jose[cryptography] passlib[bcrypt] python-multipart
```

| Package | Purpose |
|---------|---------|
| python-jose | Create & Verify JWT Tokens |
| passlib | Password hashing using bcrypt |
| python-multipart | Handle form data for OAuth2 login |

---

# Igenerate it automatically requirements

```bash
pip freeze > requirements.txt
```
---

# Install All Packages

If using a requirements file:

```bash
pip install -r requirements.txt
```

---

# Verify Installed Packages

```bash
pip list
```

Or check individually:

```bash
pip show sqlalchemy
pip show psycopg2-binary
```

---

# Run Development Server

```bash
uvicorn app.main:app --reload
```

Default URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation

```
http://127.0.0.1:8000/redoc
```

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/ecommerce
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Database Migrations

## Create Migration

```bash
alembic revision --autogenerate -m "create users table"
```

## Apply Migration

```bash
alembic upgrade head
```

## Rollback Last Migration

```bash
alembic downgrade -1
```

## View Migration History

```bash
alembic history
```

---

# PostgreSQL

## Why PostgreSQL?

Most production FastAPI applications use PostgreSQL because it provides:

- Excellent performance
- ACID compliance
- JSON & JSONB support
- Array data types
- Powerful indexing
- Full-text search
- High scalability

### Comparison

| Database | Recommended For |
|----------|-----------------|
| SQLite | Learning & Small Projects |
| MySQL | PHP/Laravel Applications |
| PostgreSQL | FastAPI, Django, Enterprise Python Projects |

---

# Docker

## Connect PostgreSQL Container

```bash
docker exec -it ecommerce-db psql -U postgres -d ecommerce
```

---

# Package Management

## Uninstall Package

```bash
pip uninstall bcrypt
```

## Install Specific Version

```bash
pip install bcrypt==4.1.3
```

## Freeze Installed Packages

```bash
pip freeze > requirements.txt
```

---

# Project Progress

- ✅ FastAPI
- ✅ Virtual Environment
- ✅ PostgreSQL
- ✅ Docker
- ✅ SQLAlchemy
- ✅ Alembic
- ✅ Repository Pattern
- ✅ Service Layer
- ✅ Product CRUD
- ✅ JWT Authentication
- ✅ Password Hashing
- ✅ Environment Variables

---

# Suggested Project Structure

```
app/
│
├── api/
├── core/
├── database/
├── models/
├── repositories/
├── schemas/
├── services/
├── utils/
├── middleware/
├── main.py
│
alembic/
│
.env
alembic.ini
requirements.txt
README.md
docker-compose.yml
Dockerfile
```

---

# Useful Commands

## Create Requirements File

```bash
pip freeze > requirements.txt
```

## Install from Requirements

```bash
pip install -r requirements.txt
```

## Update pip

```bash
python -m pip install --upgrade pip
```

## Run Server

```bash
uvicorn app.main:app --reload
```

---

# Technologies Used

- FastAPI
- Python
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker
- JWT Authentication
- Passlib
- Uvicorn
- python-dotenv

---

# Upcoming Features

- ⏳ User Authentication
- ⏳ Role-Based Access Control (RBAC)
- ⏳ Category CRUD
- ⏳ Cart API
- ⏳ Order API
- ⏳ Payment Integration
- ⏳ File Upload
- ⏳ Redis Caching
- ⏳ Email Verification
- ⏳ Unit Testing
- ⏳ CI/CD
- ⏳ AWS Deployment

---

# License

This project is created for learning and production-ready FastAPI development.