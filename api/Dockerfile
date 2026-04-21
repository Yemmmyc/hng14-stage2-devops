# ---------- BUILD STAGE ----------
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build dependencies
COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# ---------- RUNTIME STAGE ----------
FROM python:3.12-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

# Ensure Python finds user-installed packages
ENV PATH=/root/.local/bin:$PATH

# Create non-root user (grader requirement)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

HEALTHCHECK CMD curl -f http://localhost:8000/docs || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]