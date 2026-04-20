# FIXES DOCUMENTATION

This document lists all issues found in the application and the fixes applied to make the system production-ready and container-compatible.

---

## Issue 1: Hardcoded Redis host in API

File: `api/main.py`  
Approx Line: 6–10

## Problem:
Redis connection was hardcoded to `localhost`, which works locally but fails inside Docker containers because services communicate over internal network names.

## Before:
```python
r = redis.Redis(host="localhost", port=6379)
```

## Fix:
Replaced hardcoded value with environment variables to support container networking.

## After:
```python
r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379))
)
```
---

## Issue 2: Hardcoded API URL in frontend
File: frontend/app.js
Approx Line: 1–3

## Problem:
Frontend was tightly coupled to localhost:8000, making it unusable in Docker or distributed environments.

## Before:
```javascript
const API_URL = "http://localhost:8000";
```

## Fix:
Replaced with environment-based configuration to support container-to-container communication.

## After:
```javascript
const API_URL = process.env.API_URL || "http://api:8000";
```

---

## Issue 3: Worker Redis connection not environment-aware
File: worker/worker.py
Approx Line: 4–8

## Problem:
Worker service was also hardcoded to localhost, preventing proper communication with Redis container in Docker network.

## Before:
```python
r = redis.Redis(host="localhost", port=6379)
```

## Fix:
Updated to use environment variables so it works in both local and container environments.

## After:
```python
r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379))
)
```
---

## Issue 4: Missing production-safe configuration handling
File: Multiple services

## Problem:
Services relied on hardcoded values instead of environment variables, reducing portability and violating production best practices.

## Fix:
Introduced .env.example and standardized environment-based configuration across all services.

---

## Issue 5: Container networking incompatibility
File: docker-compose.yml

## Problem:
Services were not consistently referencing internal Docker DNS names.

## Fix:
Ensured all services communicate using Docker service names (api, redis, worker) over a shared network (appnet).

---

## Summary of Improvements
Enabled full Docker-based service communication
Removed all hardcoded localhost dependencies
Improved production readiness and portability
Standardized environment variable configuration

