# Agentic-RAG-KnowXAI: Permanent Authentication & Operations Guide

## 1. Overview & Architectural Boundaries

| Layer | Responsibility | Persistence Model | Failure Manifestation |
|---|---|---|---|
| **Backend Availability** | FastAPI + Uvicorn server running on `http://127.0.0.1:8000` | Process lifecycle | `Unable to connect to remote server` (Port 8000 closed) |
| **Database Availability** | Supabase PostgreSQL cluster with pgvector | Remote cloud cluster | HTTP 503 `Database service is currently unavailable` |
| **Account Persistence** | `public.users` table storing email, employee_id, password hash | Permanent disk storage in PostgreSQL | Accounts persist permanently across computer/server restarts |
| **Token Session Expiry** | JWT Access Tokens issued upon login (24h lifespan) | Client `localStorage` + JWT expiration claim | HTTP 401 `Session token has expired. Please log in again.` |

---

## 2. Windows Startup Instructions

### Recommended Master Startup (Backend + Frontend Orchestration)
Run from PowerShell in the project root:
```powershell
cd c:\Users\themr\OneDrive\Desktop\Agentic-RAG-KnowXAI
.\.venv\Scripts\python.exe main.py
```
This automatically:
1. Validates the Python and Node.js environments.
2. Checks `.env` configuration (Database URL, JWT Secret Key, Embeddings, LLM).
3. Verifies PostgreSQL connectivity and `pgvector` extension.
4. Starts Uvicorn (`http://127.0.0.1:8000`) and the Vite React frontend (`http://localhost:5173`).
5. Performs real-time health checks on `/health`.

### Manual Startup of Individual Components

#### Backend (FastAPI + Uvicorn)
```powershell
cd c:\Users\themr\OneDrive\Desktop\Agentic-RAG-KnowXAI
.\.venv\Scripts\python.exe -m uvicorn api.main:app --host 127.0.0.1 --port 8000 --reload
```

#### Frontend (Vite + React)
```powershell
cd c:\Users\themr\OneDrive\Desktop\Agentic-RAG-KnowXAI\frontend
npm run dev
```

---

## 3. Environment Variable Configuration (`.env`)

Ensure the following variables are defined in your `.env` file:
```ini
# Application Secrets
JWT_SECRET_KEY=mk-infinite-ai-enterprise-secret-key-987654321
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Database
DATABASE_URL=postgresql://postgres.dfyhvwzgmtrvjavbngnm:oTpJiW9pmx4ST1PU@aws-0-ap-south-1.pooler.supabase.com:5432/postgres
DB_ECHO=false

# LLM & Embeddings
EMBEDDING_PROVIDER=local
EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
EMBEDDING_DIMENSIONS=384
LLM_PROVIDER=local
LOCAL_LLM_MODEL=llama3.1:8b
```

> [!IMPORTANT]
> The `JWT_SECRET_KEY` is stable and permanent. Setting this in `.env` guarantees that all user tokens remain verifiable across server restarts until their configured expiration time.

---

## 4. Supported Login Identifiers & Normalization

Users can log in using any of the following:
1. **Registered Corporate Email** (case-insensitive, whitespace-trimmed, e.g., `rajeshpatil123@gmail.com`)
2. **Employee ID** (trimmed, e.g., `101`, `123`, `121`)
3. **Username** (case-insensitive, e.g., `rajeshpatil123`)

### Enterprise Departments Supported
1. `IT Support` (also accepts code `IT`)
2. `Human Resources` (also accepts code `HR`)
3. `Finance & Claims` (also accepts code `Finance`)
4. `Project Department` (also accepts code `Project`)
5. `Management`

---

## 5. Database Backup and Recovery Procedure

### Backup User Accounts & Tables
To back up the user table safely on Windows without affecting existing data:
```powershell
.\.venv\Scripts\python.exe -c "from database.connection import engine; import pandas as pd; df = pd.read_sql('SELECT id, email, username, full_name, role, employee_id, department, created_at FROM users', engine); df.to_csv('users_backup.csv', index=False); print('Users backed up to users_backup.csv')"
```

### Safe Recovery Verification
To inspect user records without modifying the database:
```powershell
.\.venv\Scripts\python.exe -c "from database.connection import engine; from sqlalchemy import text; c = engine.connect(); print('Users count:', c.execute(text('SELECT count(*) FROM users')).scalar()); c.close()"
```

---

## 6. Health & Diagnostic Endpoints

- **Root Availability**: `GET http://127.0.0.1:8000/` -> `{"status": "ok"}`
- **System Health**: `GET http://127.0.0.1:8000/health` -> Reports database, pgvector, and LLM statuses
- **Readiness Check**: `GET http://127.0.0.1:8000/ready` -> Reports readiness for traffic
- **API Documentation**: `GET http://127.0.0.1:8000/docs` -> Interactive Swagger UI
