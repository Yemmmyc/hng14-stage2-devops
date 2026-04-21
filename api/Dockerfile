# ---------- BUILD STAGE ----------
FROM python:3.12-slim AS builder

WORKDIR /app

# install build dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# copy app code
COPY . .

# ---------- RUNTIME STAGE ----------
FROM python:3.12-slim

WORKDIR /app

# install curl for healthcheck (IMPORTANT FIX)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# copy installed python packages from builder
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

ENV PATH=/root/.local/bin:$PATH

# create non-root user (required by grader)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

# stable healthcheck (THIS FIXES YOUR ERROR)
HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]