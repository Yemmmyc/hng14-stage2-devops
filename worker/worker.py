import redis
import time
import os

print("WORKER STARTED", flush=True)

r = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

def process_job(job_id):
    print(f"Processing job {job_id}", flush=True)
    time.sleep(2)
    print(f"Done job {job_id}", flush=True)

while True:
    print("Waiting for job...", flush=True)

    job = r.brpop("job", timeout=5)

    if job:
        _, job_id = job
        process_job(job_id)