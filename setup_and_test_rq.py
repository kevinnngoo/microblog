#!/usr/bin/env python3
"""Interactive script to set up RQ queue and test tasks"""

from redis import Redis
import rq

print("Setting up RQ queue...")
print(">>> from redis import Redis")
print(">>> import rq")
print(">>> queue = rq.Queue('microblog-tasks', connection=Redis.from_url('redis://'))")

# Create the queue
queue = rq.Queue('microblog-tasks', connection=Redis.from_url('redis://'))

print("\nQueue created successfully!")
print("Now you can run:")
print(">>> job = queue.enqueue('app.tasks.example', 23)")
print(">>> job.get_id()")
print(">>> job.meta")
print(">>> job.refresh()")
print(">>> job.meta")
print(">>> job.is_finished")

print("\nExecuting the commands automatically...")

# Execute the job
job = queue.enqueue('app.tasks.example', 23)
print(f"\n>>> job = queue.enqueue('app.tasks.example', 23)")
print(f"Job created with ID: {job.get_id()}")

print(f"\n>>> job.meta")
print(f"{job.meta}")

print(f"\n>>> job.is_finished")
print(f"{job.is_finished}")

print("\nNow refreshing and checking progress...")
import time

# Monitor progress
for i in range(25):  # Check for 25 seconds max
    time.sleep(1)
    job.refresh()
    print(f"\n>>> job.refresh()")
    print(f">>> job.meta")
    print(f"{job.meta}")
    print(f">>> job.is_finished")
    print(f"{job.is_finished}")
    
    if job.is_finished:
        print("\nTask completed!")
        break
