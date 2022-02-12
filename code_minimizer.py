import random
import file_processing
import test_execution

global file_lines
global filename

# population is comprised initially of len(file_lines) individuals
# each initial individual has exactly 1 line deleted
# if no such individual is good, it means that we cannot delete any line => no solution
def init_population(popSize):
    population = []
    initial_element = [1] * len(file_lines)
    i = 0
    for _ in range(len(file_lines)):
        element = initial_element.copy()
        element[i] = 0
        population.append([element, -1]) # (chromosome, fitness)
        i += 1
    return population

# population sorted by fitness, descending
# elitism is used: only the fitest survive
def eval_population(population, popSize):
    for p in population:
        p[1] = fitness(p[0])
    population.sort(key = lambda i : i[1])
    population.reverse()
    return population[0:popSize]

# if the code is not correct or tests fail => fitness is 0
# if the code is correct and tests pass => fitness is the number of deleted lines
def fitness(chromosome):
    global filename
    if chromosome.count(0) == len(chromosome):
        return 0
    trimmed_lines = file_processing.delete_lines(file_lines, chromosome)
    file_processing.write_lines(filename, trimmed_lines)
    success = test_execution.try_run_tests(file_processing.get_test_module_name(filename))
    if success:
        return len(file_lines) - len(trimmed_lines)
    return 0

# dumb selection of parent: random
def select_parent(population):
    idx = random.randint(0, len(population) - 1)
    while population[idx][1] <= 0:
        idx = random.randint(0, len(population) - 1)
    return population[idx]

# lines deleted in any of the parents are deleted in the child (reunion of deleted lines)
def crossover(parent1, parent2):
    child = [parent1[0][i] & parent2[0][i] for i in range(len(parent1[0]))]
    return [child, 0]

# delete random line ast mutation
def mutate(child):
    idx = random.randint(0, len(child[0]) - 1)
    if child[0].count(0) == len(child[0]): # avoid looping indefinitely
        return
    while child[0][idx] == 0:
        idx = random.randint(0, len(child[0]) - 1)
    child[0][idx] = 0

def best_individual(population):
    return population[0][0]

# the usual genetic algorithm
def GA(noGenerations, popSize):
    population = init_population(popSize)
    while noGenerations > 0:
        population = eval_population(population, popSize)
        children = []
        size = popSize
        while size > 0:
            parent1 = select_parent(population)
            parent2 = select_parent(population)
            child = crossover(parent1, parent2)
            mutate(child)
            children.append(child)
            size -= 1
        population.extend(children)
        noGenerations -= 1
    eval_population(population, popSize)
    return best_individual(population)


def minimize_code(toProccessFilename):
    global file_lines
    global filename
    filename = toProccessFilename
    file_lines = file_processing.get_lines(toProccessFilename)
    file_processing.write_lines(f"{toProccessFilename}.backup", file_lines) # backup made because initial file is edited by the algorithm
    pop_size = len(file_lines)
    solution = GA(pop_size * 10, pop_size) # the examples used were small so it converges pretty fasts
    solution_lines = file_processing.delete_lines(file_lines, solution)
    file_processing.write_lines(f"sol_{toProccessFilename}", solution_lines)
    file_processing.write_lines(toProccessFilename, file_processing.get_lines(f"{toProccessFilename}.backup"))
