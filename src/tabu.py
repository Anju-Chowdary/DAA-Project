import random
from collections import deque

def run(jobs, num_machines, tenure=5, iterations=100):
    def calculate_makespan(schedule):
        return max(job[2] for job in schedule)

    def generate_initial_solution(jobs):
        schedule = []
        current_time = 0
        for job in sorted(jobs, key=lambda x: x[1]):
            machine_id, duration = job
            start_time = current_time
            finish_time = start_time + duration
            job_id = jobs.index(job)
            schedule.append((machine_id, start_time, finish_time, job_id))
            current_time += duration
        return schedule

    def get_neighbors(schedule):
        neighbors = []
        for i in range(len(schedule)):
            for j in range(i + 1, len(schedule)):
                neighbor = schedule[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
        return neighbors

    initial_solution = generate_initial_solution(jobs)
    best_solution = initial_solution
    best_makespan = calculate_makespan(best_solution)

    tabu_list = deque(maxlen=tenure)
    current_solution = initial_solution

    for _ in range(iterations):
        neighbors = get_neighbors(current_solution)
        neighbors = [neighbor for neighbor in neighbors if neighbor not in tabu_list]

        if not neighbors:
            break

        current_solution = min(neighbors, key=calculate_makespan)
        current_makespan = calculate_makespan(current_solution)

        if current_makespan < best_makespan:
            best_solution, best_makespan = current_solution, current_makespan

        tabu_list.append(current_solution)

    return best_solution, best_makespan
