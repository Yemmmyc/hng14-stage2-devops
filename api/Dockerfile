# ---------------- BUILDER STAGE ----------------
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ---------------- RUNTIME STAGE ----------------
FROM python:3.12-slim

WORKDIR /app

# copy installed packages from builder
COPY --from=builder /install /usr/local

# copy application code
COPY . .

# create non-root user
RUN useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

# SAFE ENTRYPOINT (fixes your uvicorn crash)
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]