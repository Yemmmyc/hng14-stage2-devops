🚀 Job Processing Microservices (DevOps Stage 2)
📌 Overview

This project is a containerized microservices-based job processing system built as part of Stage 2 DevOps.

It consists of:

Frontend (Node.js) – Submit and track jobs
API (FastAPI) – Handles job creation and status
Worker (Python) – Processes jobs asynchronously
Redis – Queue and state management
🏗️ Architecture
Frontend → API → Redis → Worker

All services communicate over an internal Docker network.

⚙️ Prerequisites

Ensure the following are installed:

Docker
Docker Compose

Check:

docker --version
docker compose version
🚀 Getting Started

Clone the repository:

git clone https://github.com/Yemmmyc/hng14-stage2-devops.git
cd hng14-stage2-devops
🔧 Environment Setup

Copy environment variables:

cp .env.example .env

Edit .env if needed.

▶️ Run the Application
docker compose up --build
🌐 Access Services
Frontend → http://localhost:3000
API Docs → http://localhost:8000/docs
🧪 Testing the Flow
Open the frontend
Submit a job
Observe:
Job is created
Worker processes it
Status updates to completed
📦 Services
Service	Port	Description
frontend	3000	UI for job submission
api	8000	FastAPI backend
worker	—	Background processor
redis	6379	Queue (internal only)
🐳 Docker Features
Multi-container orchestration via Docker Compose
Internal networking (no exposed Redis)
Health checks for all services
Non-root container users
CPU & memory limits applied
🔄 CI/CD Pipeline

Implemented using GitHub Actions.

Stages:
Lint
flake8 (Python)
eslint (JavaScript)
hadolint (Dockerfiles)
Test
pytest with coverage report
Build
Docker images built and tagged
Security Scan
Trivy scans images
Pipeline fails on CRITICAL vulnerabilities
Integration Test
Full stack runs
Job submitted and validated
Deploy
Rolling update simulation
Health checks enforced
🛠️ Fixes Applied

All bugs and improvements are documented in:

FIXES.md

Includes:

Misconfigurations
Container issues
Networking fixes
Production improvements
🔐 Environment Variables

Example:

REDIS_HOST=redis
REDIS_PORT=6379
API_URL=http://api:8000
⚠️ Notes
.env is excluded from version control
No secrets are hardcoded
Designed for local + CI environments
✅ Expected Output

When running successfully:

All containers start without errors
Redis becomes healthy
API becomes healthy
Frontend loads
Jobs move from "pending" → "completed"
👨‍💻 Author

Yemisi (DevOps Engineer)

