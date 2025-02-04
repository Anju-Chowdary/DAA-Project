def run(jobs, num_machines):
    schedule = []
    current_time = [0] * num_machines
    job_queue = jobs[:]

    while job_queue:
        for machine_id in range(num_machines):
            if job_queue:
                job = job_queue.pop(0)
                machine_id, duration = job
                start_time = current_time[machine_id]
                finish_time = start_time + duration
                job_id = jobs.index(job)  # Track job by its original index
                schedule.append((machine_id, start_time, finish_time, job_id))
                current_time[machine_id] = finish_time

    makespan = max(current_time)
    return schedule, makespan
