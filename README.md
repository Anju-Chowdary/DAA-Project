# **Optimizing Job Shop Scheduling: A Comparative Study of Metaheuristic Algorithms**

## Project Overview

In this project, we focus on comparing several metaheuristic algorithms used to optimize job shop scheduling, which is a key challenge in operations management. The main objective is to determine which algorithm can best organize job sequences and machine assignments to minimize the total completion time, or "makespan." To do this, we created a customized simulation tool to test how these algorithms perform.

Our findings are that each algorithm has its own strength and weakness. The choice of algorithm is subject to certain conditions and objectives. Different situations demand different approaches, and in this case, results show that metaheuristic algorithms can perform better than the traditional methods for the improvement of scheduling efficiency. This project is focused on the determination of which scheduling algorithm best fits the unique needs of the industry, ultimately leading to improved management of complex schedules.


## Methodology

The subject of this project will be **Job Shop Scheduling**, and it is supposed to minimize the total time of execution of all jobs, so the **makespan** will be the measure for the objective. In short, the task will be checking a few metaheuristic algorithms that can figure out which of them can more efficiently schedule the job on various machines to make the whole process as optimal as possible.

### Algorithms Used

We tested and compared several well-known algorithms to solve the scheduling problem:

**Ant Colony Optimization (ACO)**: The algorithm draws inspiration from how ants find paths to food. ACO uses an iterative approach where virtual "ants" deposit pheromone trails that help guide the algorithm toward better solutions. It's great for solving complex combinatorial problems like job shop scheduling.

**Genetic Algorithm (GA)**: Modeled after natural evolution, GA uses a population of solutions and applies genetic operations like selection, crossover, and mutation to evolve better solutions over generations. It's all about improving the current solution through these evolutionary steps.

**Simulated Annealing (SA)**: It is based on the annealing process in metallurgy, or heating and cooling of metal. The algorithm is a search technique that allows temporary worsening of the solution at first to help escape from local optima and then settle at a global optimum gradually.

The other approaches are the simpler, traditional First-In-First-Out (FIFO), in which jobs are processed in the order they arrive, with no regard to job complexity. It's simple to implement, but may lead to longer completion times in complex job shop environments.

**Round Robin**: This is the most widely used CPU scheduling algorithm. The Round Robin uses a fixed time slice for every job. Equal shares of machine time are allocated to each job before moving to the next in line. This ensures fairness, but it incurs overheads due to continuous switching between jobs.

**Tabu search**: This algorithm is a development of local search. A "tabu list" is maintained to keep track of recently visited solutions and avoid visiting them again in order to ensure that the locally optimal solution is explored more strongly and with increased probability of finding an even better solution.

**NSGA-II**: A genetic principle-based multi-objective algorithm, NSGA-II is an optimization algorithm used for optimizing conflicting goals. The algorithm maintains a diverse set of non-dominated solutions, which are Pareto-optimal. Therefore, it can be used on problems that involve balancing different objectives simultaneously.

### Experimental Setup

We designed a custom simulation tool that took data about jobs and machines to simulate the performance of these algorithms. Each job is attached to the machine it will be processed on and has an assigned duration. We used simulation to calculate the **makespan** that is, the total time taken to complete all jobs — as our main performance measure. Besides, we studied **time complexity** (the algorithm's speed of execution) and **space complexity** (amount of memory the algorithm consumes) to consider how efficiently these algorithms can solve computational problems.

### Results

Every algorithm was tested on the same set of jobs and machines. Performance was evaluated by looking at the ways in which each algorithm minimized the makespan, as well as how efficiently it ran in terms of time and memory. Additionally, **Gantt charts** and **dependency graphs** have been generated to give graphical evidence of what kind of jobs are scheduled on machines and how these jobs relate to each other.

Comparing these results provided insight into which type of algorithm works best in what type of condition, hence successfully choosing the best for optimizing job shop scheduling performance in a real-world environment.


























Paper Published for the above work
## **P, Anju Chowdary and Sri Hanish Kumar, Meka Sai and BG, Shresta and Mahithi Reddy, T. and Bindu Sree, Mandapati and Ramasamy, Gayathri, Optimizing Job Shop Scheduling: A Comparative Study of Metaheuristic Algorithms (November 15, 2024). Available at SSRN: https://ssrn.com/abstract=5091503 or http://dx.doi.org/10.2139/ssrn.5091503**






## To use this:

1. Download the ZIP file and extract it.
2. Run `trail.py`.
3. **Do not make any changes** to the directory or files inside the ZIP—keep the structure intact.
4. Make sure to adjust the file paths in the code to match the locations on your machine.
