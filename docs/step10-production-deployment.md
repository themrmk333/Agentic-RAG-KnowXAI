# Step 10 — Production Deployment & Hardening

## Overview
This document describes the production deployment architecture for the **Agentic-RAG-KnowXAI** application. The backend is designed for high availability, security, and scalability using Docker and Render.

## Architecture & Render Deployment
The deployment utilizes Render's standard web services blueprint (`render.yaml`).
The API runs in a container built from `Dockerfile` utilizing `python:3.11-slim`.

**Key production features:**
1. **Model Caching:** To prevent slow cold starts or runtime API limits, the embedding model (`BAAI/bge-small-en-v1.5`) is pre-downloaded and baked into the Docker layers during the build step.
2. **Global Exception Masking:** In `production`, internal 500 errors and stack traces are suppressed and replaced with safe generic error messages. They are securely logged using Python's `logging` module.
3. **CORS Hardening:** `CORS_ORIGINS` is configured through the environment, allowing precise restriction of allowed frontend clients.
4. **Non-Root Execution:** The application executes under a restricted `appuser` inside the container.
5. **Render Dynamic Port Binding:** The application listens on `0.0.0.0` at the port specified by the `$PORT` environment variable injected by Render.

## Deployment Checklist & Configuration

### Build & Start Commands
- **Build:** `docker build -t agentic-rag-knowxai .`
- **Start:** `docker run -p 8000:8000 --env-file .env agentic-rag-knowxai` (or via Render automatic execution of `uvicorn api.main:app --host 0.0.0.0 --port $PORT`).

### Required Environment Variables
You must configure the following in the Render Dashboard (or via your `.env` for local testing):
- `APP_ENV=production`
- `DATABASE_URL=postgresql+psycopg2://...` (Must point to the active PGVector database)
- `GEMINI_API_KEY=...`
- `APP_SECRET_KEY=...`
- `CORS_ORIGINS=["https://your-frontend-domain.com"]`
- `EMBEDDING_PROVIDER=local`
- `DB_ECHO=false`

### Health & Readiness Probes
- **Readiness:** `/api/v1/system/ready` (Returns 200 OK once Postgres/PGVector is connected). This is used by Render to route traffic only when the application is fully online.
- **Health:** `/api/v1/system/health`

## Database Connection & Integrity
The database connection utilizes SQLAlchemy and async psycopg2 seamlessly.
The HNSW Cosine Index and vector dimensionalities (384) are guaranteed by `pgvector`. **Destructive database actions or automatic migrations are intentionally disabled in production.** All chunk data and indices populated in Step 5 remain active.

## Troubleshooting & Rollback
- **Missing Embeddings/Dimension errors:** Verify `EMBEDDING_MODEL` and `PGVECTOR_DIMENSIONS` are aligned.
- **CORS Issues:** Ensure `CORS_ORIGINS` matches the exact string payload (valid JSON list) of your front-end deployment URL.
- **Rollback:** Re-deploy the previous successful image tag in Render or trigger a revert commit if new configuration breaks the environment variables.
