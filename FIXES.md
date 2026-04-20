## Issue 1
File: api/main.py  
Problem: Redis host is hardcoded to localhost, breaking container networking  
Fix: Replaced with environment variable REDIS_HOST with fallback to "redis"

## Issue 2
File: frontend/app.js  
Problem: API URL hardcoded to localhost preventing container communication  
Fix: Replaced with environment variable API_URL pointing to internal Docker service name## Issue 3

## Issue 3
File: worker/worker.py  
Problem: Redis host hardcoded to localhost causing failure in containerized environment  
Fix: Replaced with environment variables REDIS_HOST and REDIS_PORT for Docker compatibility
