FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies (e.g. build-essential if needed for native extensions)
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for cache efficiency
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download the ML embedding model to avoid runtime downloads
# This caches it in the Docker image layers
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('BAAI/bge-small-en-v1.5')"

# Create non-root user for security
RUN adduser --disabled-password --gecos "" appuser

# Copy application source code
COPY . .

# Change ownership of the app directory
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose the port (Render provides $PORT dynamically, but default is 8000)
EXPOSE 8000

# Start FastAPI application
CMD uvicorn api.main:app --host 0.0.0.0 --port ${PORT:-8000}
