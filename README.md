# Job Processing Application - DevOps Stage 2

This repository contains a containerized multi-service job processing application, built for the HNG14 Stage 2 DevOps assessment.

## Prerequisites

To run this application on a clean machine from scratch, you will need:
- [Docker](https://docs.docker.com/get-docker/) installed.
- [Docker Compose](https://docs.docker.com/compose/install/) (usually included with Docker Desktop).
- Git.

## How to Bring the Stack Up

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chukwukelu2023/hng14-stage2-devops.git
   cd hng14-stage2-devops
   ```

2. **Setup Environment Variables:**
   Create a `.env` file from the provided example:
   ```bash
   cp .env.example .env
   ```
   Open `.env` and set a strong `REDIS_PASSWORD`.

3. **Start the Application:**
   Bring up the entire stack using Docker Compose:
   ```bash
   docker-compose up -d --build
   ```

## What a Successful Startup Looks Like

After running the `docker-compose up` command, Docker will build the images for the `api`, `worker`, and `frontend` services using multi-stage builds.

You can verify the status by running:
```bash
docker-compose ps
```

You should see all 4 containers (`frontend`, `api`, `worker`, `redis`) in a `Up` and `healthy` state. The services start in order based on health checks: Redis -> API -> Frontend & Worker.

- The Frontend will be available at `http://localhost:3000`.
- The API will be available at `http://localhost:8000`.

To test the system, open `http://localhost:3000` in your browser, click "Submit New Job", and you will see the status update from "queued" to "completed" as the background worker processes it.

## Architecture & CI/CD
- **Frontend**: Node.js serving static HTML/JS.
- **API**: Python FastAPI handling job submission.
- **Worker**: Python process picking up jobs from Redis.
- **CI/CD Pipeline**: GitHub Actions automatically lints, tests, builds, scans (with Trivy), integration tests, and deploys the application.
