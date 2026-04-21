# -------- BUILD STAGE --------
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# -------- RUNTIME STAGE --------
FROM python:3.12-slim

WORKDIR /app

# copy installed packages
COPY --from=builder /root/.local /root/.local

# copy app code
COPY . .

# add non-root user
RUN useradd -m appuser && chown -R appuser /app
USER appuser

ENV PATH=/root/.local/bin:$PATH

EXPOSE 8000

HEALTHCHECK CMD curl -f http://localhost:8000/docs || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]