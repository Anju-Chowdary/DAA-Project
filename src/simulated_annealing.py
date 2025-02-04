import random
import numpy as np

def run(jobs, num_machines):
    current_solution = jobs[:]
    current_cost = sum(job[1] for job in current_solution)
    temp = 1000
    best_solution = current_solution[:]
    best_cost = current_cost

    for _ in range(1000):  # Cooling steps
        i, j = random.sample(range(len(jobs)), 2)
        new_solution = current_solution[:]
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        new_cost = sum(job[1] for job in new_solution)

        if new_cost < current_cost or random.random() < np.exp((current_cost - new_cost) / temp):
            current_solution, current_cost = new_solution, new_cost
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost

        temp *= 0.99  # Reduce temperature

    schedule = [(job[0], idx, idx + job[1], idx) for idx, job in enumerate(best_solution)]
    makespan = max(job[2] for job in schedule)
    return schedule, makespan
