<div align="center">

# 🚀 Job Processing Application

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white" alt="Node.js" />
  <img src="https://img.shields.io/badge/Express.js-404D59?style=for-the-badge&logo=express" alt="Express.js" />
  <img src="https://img.shields.io/badge/Redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white" alt="Redis" />
  <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
</p>

A containerized multi-service job processing application built for the **HNG14 Stage 2 DevOps Assessment**.

</div>

---

## 📋 Overview

This repository features a complete, production-ready microservices stack that handles job creation and background processing. As part of the DevOps Stage 2 assessment, the application has been debugged, fully containerized using Docker, and integrated with a robust CI/CD pipeline.

### System Architecture
- **Frontend (`Node.js/Express`)**: Serves the UI for submitting and tracking jobs.
- **API (`Python/FastAPI`)**: Receives job requests and places them in a Redis queue.
- **Worker (`Python`)**: A background process that picks up queued jobs and simulates processing.
- **Redis**: The message broker linking the API and the worker, completely isolated from external networks.

---

## 🛠️ What Was Done (DevOps Improvements)

This application was initially provided with intentional bugs and bad practices. The following improvements have been made:

1. **Security & Configuration**:
   - `api/.env` containing plain-text secrets was entirely purged from Git history.
   - All connection strings and hardcoded configurations were moved to environment variables.
   - `.gitignore` and `.env.example` templates were added.

2. **Codebase Bug Fixes**:
   - Fixed missing Redis password authentication in API and Worker.
   - Replaced flawed sequential Redis commands with atomic `pipeline` executions.
   - Implemented `SIGINT/SIGTERM` graceful shutdowns for the Worker and Frontend servers.
   - Implemented comprehensive error handling and logging in the Frontend API calls.

3. **Containerization**:
   - Developed production-quality `Dockerfiles` using **multi-stage builds** to ensure minimal image footprints.
   - Enforced **non-root users** across all containers for elevated security.
   - Implemented customized `HEALTHCHECK`s for each service.

4. **Orchestration (`docker-compose`)**:
   - Restricted internal communication strictly to an `app-network`.
   - Utilized `depends_on: condition: service_healthy` to ensure dependent services wait for upstream systems to fully initialize.
   - Placed explicit `cpu` and `memory` limits on every service.

5. **Continuous Integration & Deployment (CI/CD)**:
   - Built a comprehensive GitHub Actions `.github/workflows/main.yml` pipeline with 6 strict stages:
     - **Lint**: Validates Python (`flake8`), JS (`eslint`), and Dockerfiles (`hadolint`).
     - **Test**: Automates API unit testing using `pytest` with mocked Redis, including coverage reports.
     - **Build**: Compiles, tags with SHA, and pushes Docker images to a localized service registry.
     - **Security Scan**: Utilizes Trivy to intercept any `CRITICAL` vulnerabilities and fail the build, outputting SARIF logs.
     - **Integration Test**: Spins up the full Docker Compose stack, submits a real job, polls for success, and gracefully tears it down.
     - **Deploy**: Simulates a rolling update on the `main` branch.

Detailed fixes for each service can be viewed in the [`FIXES.md`](./FIXES.md) document. Execution history is available in `TASK.md` and `WALKTHROUGH.md`.

---

## ⚙️ Running Locally From Scratch

To spin up this application on your machine, follow these instructions:

### Prerequisites
- [Git](https://git-scm.com/) installed
- [Docker Engine](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/install/) installed

### Setup & Startup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chukwukelu2023/hng14-stage2-devops.git
   cd hng14-stage2-devops
   ```

2. **Setup Environment Variables:**
   Create your local `.env` file from the example template:
   ```bash
   cp .env.example .env
   ```
   *Note: You can change the `REDIS_PASSWORD` within the `.env` file if desired.*

3. **Launch the Stack:**
   Bring the entire environment up in detached mode. This command builds all images automatically using multi-stage contexts.
   ```bash
   docker-compose up -d --build
   ```

### Verification & Testing

Once Docker starts, verify the services are up and healthy. The startup process guarantees that the worker and API won't boot until Redis is fully ready.

```bash
docker-compose ps
```

*Expected Output: 4 containers with `Up` status and `(healthy)` flags.*

- **Frontend Application**: [http://localhost:3000](http://localhost:3000)
- **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)

**Submit a Job**:
1. Open [http://localhost:3000](http://localhost:3000) in your web browser.
2. Click **Submit New Job**.
3. Watch the interface poll the API as the status transitions from `queued` to `completed`.
4. Run `docker-compose logs worker` to watch the backend process the job in real-time.

---

<div align="center">
  <i>Built with ❤️ for HNG14</i>
</div>
