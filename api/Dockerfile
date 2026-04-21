# ---------------- BUILDER STAGE ----------------
FROM python:3.12-slim AS builder

WORKDIR /app

# Install dependencies in builder layer
COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

# ---------------- RUNTIME STAGE ----------------
FROM python:3.12-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY . .

# Make sure python can find user-installed packages
ENV PATH=/root/.local/bin:$PATH

EXPOSE 8000

# IMPORTANT: correct uvicorn startup (no broken path)
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]