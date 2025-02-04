import random

class Individual:
    def __init__(self, schedule):
        self.schedule = schedule
        self.rank = None
        self.dom_set = []
        self.dom_count = 0
        self.crowd_dist = 0

def run(jobs, num_machines, population_size=50, generations=100):
    def calculate_objectives(schedule):
        try:
            makespan = max(job[2] for job in schedule)
            total_idle_time = sum(job[1] for job in schedule) - makespan
            return makespan, total_idle_time
        except Exception as e:
            print("Error in calculate_objectives:")
            print(schedule)
            raise e

    def generate_initial_population(jobs):
        population = []
        for _ in range(population_size):
            schedule = []
            current_times = [0] * num_machines
            for job in sorted(jobs, key=lambda k: random.random()):
                machine_id, duration = job
                start_time = current_times[machine_id]
                end_time = start_time + duration
                job_id = jobs.index(job)
                schedule.append((machine_id, start_time, end_time, job_id))
                current_times[machine_id] = end_time
            population.append(schedule)
        return population

    def non_dominated_sorting(population):
        fronts = [[]]
        for i, ind1 in enumerate(population):
            ind1_dominates = []
            ind1_dominated_by = 0
            for j, ind2 in enumerate(population):
                if i != j:
                    if dominates(ind1.schedule, ind2.schedule):
                        ind1_dominates.append(j)
                    elif dominates(ind2.schedule, ind1.schedule):
                        ind1_dominated_by += 1
            if ind1_dominated_by == 0:
                fronts[0].append(i)
                ind1.rank = 0
            ind1.dom_set = ind1_dominates
            ind1.dom_count = ind1_dominated_by

        current_front = 0
        while len(fronts[current_front]) > 0:
            next_front = []
            for i in fronts[current_front]:
                for j in population[i].dom_set:
                    population[j].dom_count -= 1
                    if population[j].dom_count == 0:
                        next_front.append(j)
                        population[j].rank = current_front + 1
            current_front += 1
            fronts.append(next_front)

        return fronts[:-1]

    def dominates(schedule1, schedule2):
        obj1_1, obj1_2 = calculate_objectives(schedule1)
        obj2_1, obj2_2 = calculate_objectives(schedule2)
        return (obj1_1 <= obj2_1 and obj1_2 <= obj2_2) and (obj1_1 < obj2_1 or obj1_2 < obj2_2)

    def crowding_distance_assignment(front, population):
        distances = [0] * len(front)
        for m in range(2):  # Two objectives
            front.sort(key=lambda x: calculate_objectives(population[x].schedule)[m])
            min_val = min(calculate_objectives(population[j].schedule)[m] for j in front)
            max_val = max(calculate_objectives(population[j].schedule)[m] for j in front)
            if max_val > min_val:
                for i in range(1, len(front) - 1):
                    distances[i] += (calculate_objectives(population[front[i + 1]].schedule)[m] -
                                     calculate_objectives(population[front[i - 1]].schedule)[m]) / (max_val - min_val)
        return distances

    population = generate_initial_population(jobs)
    population = [Individual(schedule) for schedule in population]

    for _ in range(generations):
        offspring = []
        while len(offspring) < population_size:
            parent1, parent2 = random.sample(population, 2)
            pivot = random.randint(1, len(jobs) - 1)
            child1 = parent1.schedule[:pivot] + parent2.schedule[pivot:]
            child2 = parent2.schedule[:pivot] + parent1.schedule[pivot:]
            offspring.extend([Individual(child1), Individual(child2)])

        for ind in offspring:
            if random.random() < 0.1:  # Mutation chance
                idx1, idx2 = random.sample(range(len(jobs)), 2)
                ind.schedule[idx1], ind.schedule[idx2] = ind.schedule[idx2], ind.schedule[idx1]

        population.extend(offspring)
        fronts = non_dominated_sorting(population)
        new_population = []
        for front in fronts:
            if len(new_population) + len(front) > population_size:
                distances = crowding_distance_assignment(front, population)
                front = sorted(front, key=lambda x: distances[x], reverse=True)
                new_population.extend(front[:population_size - len(new_population)])
                break
            new_population.extend(front)
        population = [population[i] for i in new_population]

    best_individual = min(population, key=lambda ind: calculate_objectives(ind.schedule))
    return best_individual.schedule, calculate_objectives(best_individual.schedule)
