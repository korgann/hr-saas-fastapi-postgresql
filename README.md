# HR SaaS Backend (FastAPI + PostgreSQL)

This is an internal HR management backend service built using FastAPI, PostgreSQL, and SQLAlchemy (async). It covers employee task assignment, workload tracking, and secure role-based access control using ABAC logic.

## 🧰 Tech Stack

- FastAPI (async)
- PostgreSQL
- SQLAlchemy (async) + Alembic
- ABAC permission logic
- Docker
- JWT Auth

## 🧾 Features

- HR process API (assignments, workload, access)
- Async patterns & scalable DB logic
- Alembic migrations
- Clean ABAC permissions (roles + units)
- Frontend integration via JSON endpoints

## 🚀 Run locally

```bash
git clone https://github.com/korgann/hr-saas-fastapi-postgresql.git
cd hr-saas-fastapi-postgresql
docker-compose up --build
```