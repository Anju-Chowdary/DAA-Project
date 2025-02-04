def run(jobs, num_machines):
    schedule = []
    current_time = 0
    for job in jobs:
        machine_id, duration = job
        start_time = current_time
        finish_time = start_time + duration
        job_id = jobs.index(job)
        schedule.append((machine_id, start_time, finish_time, job_id))
        current_time += duration
    makespan = max(job[2] for job in schedule)
    return schedule, makespan
