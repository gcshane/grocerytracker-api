# 🛒 Grocery Tracker (API)

A RESTful API for tracking groceries, managing shopping lists, and monitoring item expiry dates — built with **FastAPI** and **PostgreSQL**.

## ✨ Features

- **User Authentication** — Secure login with OAuth2 password flow, JWT access tokens, and Argon2 password hashing
- **Shopping Lists** — Create and manage personalised grocery lists
- **Item Tracking** — Track items with quantities and configurable stock alerts
- **Expiry Monitoring** — Log item batches with expiry dates and set alert thresholds to reduce food waste

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Framework** | [FastAPI](https://fastapi.tiangolo.com/) |
| **ORM** | [SQLModel](https://sqlmodel.tiangolo.com/) |
| **Database** | PostgreSQL (via [Supabase](https://supabase.com/)) |
| **Auth** | [PyJWT](https://pyjwt.readthedocs.io/) + [pwdlib](https://github.com/frankie567/pwdlib) (Argon2) |
| **Deployment** | [Railway](https://railway.com/) |

## 📁 Project Structure

```
grocerytrackingapp/
├── app/
│   ├── api/v1/          # Route handlers
│   │   ├── auth.py      # Authentication endpoints
│   │   └── lists.py     # List endpoints
│   ├── core/
│   │   └── config.py    # Environment configuration
│   ├── db/
│   │   ├── database.py  # Engine & session management
│   │   └── schema.py    # SQLModel table definitions
│   ├── models/          # Pydantic request/response models
│   ├── services/        # Business logic layer
│   │   ├── auth_services.py
│   │   └── user_services.py
│   ├── dependencies.py  # FastAPI dependency injection
│   └── main.py          # App entrypoint
├── design/              # Database design diagrams
├── tests/
├── requirements.txt
└── railway.json         # Railway deployment config
```

## 📊 Database Schema

```
┌──────────────┐       ┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│    User      │       │    List      │       │    Item      │       │  ItemBatch   │
├──────────────┤       ├──────────────┤       ├──────────────┤       ├──────────────┤
│ user_id (PK) │──┐    │ list_id (PK) │──┐    │ item_id (PK) │──┐    │ expiry_date  │
│ name         │  └───>│ list_name    │  └───>│ item_name    │  └───>│   (PK)       │
│ username     │       │ user_id (FK) │       │ list_id (FK) │       │ item_id      │
│ email        │       └──────────────┘       │ total_qty    │       │   (PK, FK)   │
│ password     │                              │ qty_limit    │       │ quantity     │
│ alert        │                              │ alert_days   │       └──────────────┘
└──────────────┘                              └──────────────┘
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL database (or a [Supabase](https://supabase.com/) project)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/gcshane/grocerytrackingapp.git
   cd grocerytrackingapp
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the `app/` directory:

   ```env
   SUPABASE_URL=postgresql://user:password@host:port/dbname
   JWT_SECRET_KEY=your-secret-key
   JWT_ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

5. **Run the development server**

   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://localhost:8000`.

### API Documentation

FastAPI auto-generates interactive docs:

- **Swagger UI** — [http://localhost:8000/docs](http://localhost:8000/docs)

## 🔑 API Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `GET` | `/` | Health check | ✗ |
| `POST` | `/auth/login` | Login & receive JWT | ✗ |
| `GET` | `/lists` | Get user's lists | ✓ |

> **Authentication:** Include the JWT in the `Authorization` header:
> ```
> Authorization: Bearer <access_token>
> ```

## 🌐 Deployment

This project is configured for deployment on [Railway](https://railway.com/) using Railpack. The configuration is defined in `railway.json`:

```json
{
  "build": { "builder": "RAILPACK" },
  "deploy": { "startCommand": "uvicorn app.main:app --host 0.0.0.0" }
}
```

## 📄 License

This project is for personal use.