import random

def run(jobs, num_machines):
    population = [sorted(jobs, key=lambda k: random.random()) for _ in range(10)]
    best_schedule = population[0]
    best_makespan = sum(job[1] for job in best_schedule)

    for _ in range(100):  # Run for 100 generations
        new_population = []
        for _ in range(5):  # Tournament selection of top 50%
            candidates = random.sample(population, 2)
            winner = min(candidates, key=lambda sched: sum(job[1] for job in sched))
            new_population.append(winner)

        # Crossover and mutation
        offspring = []
        for pair in zip(new_population[::2], new_population[1::2]):
            pivot = random.randint(1, len(jobs) - 1)
            child1 = pair[0][:pivot] + pair[1][pivot:]
            child2 = pair[1][:pivot] + pair[0][pivot:]
            offspring.extend([child1, child2])

        # Mutate by swapping two jobs
        for individual in offspring:
            if random.random() < 0.1:  # Mutation chance
                idx1, idx2 = random.sample(range(len(jobs)), 2)
                individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

        population.extend(offspring)
        current_best = min(population, key=lambda sched: sum(job[1] for job in sched))
        current_makespan = sum(job[1] for job in current_best)
        if current_makespan < best_makespan:
            best_makespan, best_schedule = current_makespan, current_best

    schedule = [(job[0], idx, idx + job[1], idx) for idx, job in enumerate(best_schedule)]
    makespan = max(job[2] for job in schedule)
    return schedule, makespan
