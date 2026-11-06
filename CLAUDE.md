# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Grocery Tracker API - A FastAPI-based RESTful backend for grocery tracking with shopping lists and expiry date monitoring. Python 3.13.3+.

## Commands

```bash
# Install dependencies
uv sync

# Run development server
uv run uvicorn app.main:app --reload

# Run all tests
uv run pytest -v

# Run specific test file
uv run pytest tests/api/v1/test_auth.py -v

# Lint code
uvx ruff check .
```

## Architecture

**Layered Architecture:** Routes (HTTP) → Services (Business Logic) → Data Access (ORM) → Database

```
app/
├── api/v1/           # HTTP endpoints (auth_api.py, lists_api.py)
├── core/config.py    # Environment configuration
├── db/
│   ├── database.py   # SQLModel engine, session, init
│   └── schema.py     # Table definitions (User, List, Item, ItemBatch)
├── models/           # Pydantic request/response DTOs
├── services/         # Business logic (auth, lists, users)
├── dependencies.py   # FastAPI dependency injection
└── main.py           # App factory with lifespan management

tests/
├── api/v1/           # Integration tests
└── services/         # Unit tests
```

## Database Schema

- **User**: user_id, name, username (indexed), email (indexed), password, alert
- **List**: list_id, list_name, user_id (FK→User)
- **Item**: item_id, item_name, list_id (FK→List), total_quantity, quantity_limit, alert_days_limit
- **ItemBatch**: expiry_date (PK), item_id (PK, FK→Item), quantity

Production uses PostgreSQL (Supabase); tests use SQLite in-memory.

## Environment Variables

- `DATABASE_URL` - PostgreSQL or SQLite connection string
- `JWT_SECRET_KEY` - Min 32 characters for HS256 (required)
- `JWT_ALGORITHM` - Signing algorithm (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Token expiration (default: 30)

## Authentication

JWT-based auth with Argon2 password hashing (pwdlib). Protected routes require `Authorization: Bearer <token>` header. Signup and login both return JWT tokens.

## Testing Patterns

- Unit tests use mocks and SQLite in-memory databases
- Integration tests use `app.dependency_overrides` for FastAPI dependencies
- Auth service tests cover JWT encode/decode, password verification, token expiry

## Git Workflow

- `main` branch: production (auto-deploys to FastAPI Cloud)
- `dev` branch: development
- CI runs tests + lint on dev pushes and PRs to main

## Development Guidelines

- Always update README.md when making changes that affect usage, setup, or API endpoints
- Always update the Bruno collection (`bruno/`) when adding, modifying, or removing API endpoints
- Always sync the Notion project document when making API changes
