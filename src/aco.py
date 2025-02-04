import random
import numpy as np

def run(jobs, num_machines):
    # A simple placeholder for an Ant Colony Optimization algorithm
    schedule = []
    current_time = 0
    for job in sorted(jobs, key=lambda x: x[1]):  # Sort by duration as a placeholder
        machine_id, duration = job
        start_time = current_time
        finish_time = start_time + duration
        job_id = jobs.index(job)
        schedule.append((machine_id, start_time, finish_time, job_id))
        current_time += duration  # Update time; simple serial scheduling
    makespan = max(job[2] for job in schedule)
    return schedule, makespan
