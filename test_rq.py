#!/usr/bin/env python3
"""Test script to demonstrate RQ task execution"""

from redis import Redis
import rq
import time

# Create connection to Redis and RQ queue
print("Connecting to Redis...")
queue = rq.Queue('microblog-tasks', connection=Redis.from_url('redis://'))

# Enqueue the example task
print("Enqueueing task...")
job = queue.enqueue('app.tasks.example', 5)

print(f"Job ID: {job.get_id()}")
print(f"Job is finished: {job.is_finished}")

# Monitor the job progress
print("\nMonitoring job progress...")
while not job.is_finished:
    job.refresh()
    print(f"Job is finished: {job.is_finished}")
    if hasattr(job, 'meta') and job.meta:
        progress = job.meta.get('progress', 0)
        print(f"Progress: {progress}%")
    time.sleep(1)

print("Job completed!")
print(f"Final status: {job.is_finished}")
