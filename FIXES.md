# Bug Fixes Documentation

This file documents all the misconfigurations, bad practices, and missing production requirements found in the starter application, along with the implemented fixes.

## 1. Security & Configuration
- **File**: `api/.env`
- **Line**: Entire file
- **Problem**: The `.env` file containing the `REDIS_PASSWORD` secret was tracked in Git history, exposing sensitive credentials.
- **Fix**: Removed the `.env` file from Git history using `git rm --cached` and rewrote the initial commit (`git commit --amend`). Created a `.gitignore` file to prevent tracking of environment files and created a safe `.env.example` placeholder.

## 2. API Service (`api/main.py`)
- **File**: `api/main.py`
- **Line**: 8 (`r = redis.Redis(host="localhost", port=6379)`)
- **Problem**: The Redis connection parameters were hardcoded to `localhost`, which fails in a containerized environment (Docker), and did not include a password for authentication.
- **Fix**: Replaced hardcoded parameters with environment variables `REDIS_HOST`, `REDIS_PORT`, and `REDIS_PASSWORD` using `os.environ.get()`.
  
- **File**: `api/main.py`
- **Line**: 13-14 (`r.lpush(...)`, `r.hset(...)`)
- **Problem**: Bad Practice - Job creation logic used sequential Redis commands instead of a transactional pipeline. If `hset` failed after `lpush`, the queue would be in an inconsistent state.
- **Fix**: Wrapped the `lpush` and `hset` operations within a Redis `pipeline()` and executed them atomically.

## 3. Worker Service (`worker/worker.py`)
- **File**: `worker/worker.py`
- **Line**: 6 (`r = redis.Redis(host="localhost", port=6379)`)
- **Problem**: The Redis connection parameters were hardcoded, failing in Docker, and missing password authentication.
- **Fix**: Updated connection parameters to use `os.environ.get()` for `REDIS_HOST`, `REDIS_PORT`, and `REDIS_PASSWORD`.

- **File**: `worker/worker.py`
- **Line**: 4 (`import signal`), 14 (`while True:`)
- **Problem**: Missing Production Requirement - `signal` was imported but unused. The worker could not be gracefully shut down, potentially terminating midway through processing a job if the container was stopped.
- **Fix**: Implemented `handle_sigint` signal handlers for `SIGINT` and `SIGTERM`. Introduced a `shutdown_flag` to allow the worker loop to cleanly exit after finishing its current job.

## 4. Frontend Service (`frontend/app.js`)
- **File**: `frontend/app.js`
- **Line**: 6 (`const API_URL = "http://localhost:8000";`)
- **Problem**: The `API_URL` was hardcoded, preventing the frontend from communicating with the API across different hostnames or within Docker networks.
- **Fix**: Updated the code to read `API_URL` from the `process.env.API_URL` environment variable, falling back to `http://localhost:8000`.

- **File**: `frontend/app.js`
- **Line**: 16, 25 (`res.status(500).json({ error: "something went wrong" });`)
- **Problem**: Bad Practice - Generic error handling without internal logging made it impossible to debug failed API requests.
- **Fix**: Added `console.error` logs to capture `err.message` in the catch blocks.

- **File**: `frontend/app.js`
- **Line**: 29 (`app.listen(...)`)
- **Problem**: Missing Production Requirement - No graceful shutdown of the HTTP server, which can cause connection drops during deployment rollouts.
- **Fix**: Handled `SIGTERM` and `SIGINT` to call `server.close()`, ensuring open connections are handled before the process exits.
