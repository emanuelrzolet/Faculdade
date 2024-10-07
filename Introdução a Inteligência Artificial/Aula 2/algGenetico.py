import random

# Parâmetros
target = "Hello World"  # O objetivo que a evolução tenta chegar
population_size = 100  # Número de indivíduos na população
mutation_rate = 0.01  # Probabilidade de mutação de um gene
generations = 5000  # Número máximo de gerações

# Função Fitness
def fitness(individual):
    """
    Calcula o fitness de um indivíduo.
    O fitness é a quantidade de caracteres corretos nos lugares corretos.
    """
    score = 0
    for i in range(len(target)):
        if individual[i] == target[i]:
            score += 1
    return score

# Inicialização
def initialize_population():
    """
    Inicializa uma nova população com indivíduos aleatórios.
    Cada indivíduo é uma lista de caracteres.
    """
    population = []
    for _ in range(population_size):
        individual = []
        for _ in target:
            gene = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ, !")
            individual.append(gene)
        population.append(individual)
    return population

# Seleção
def select(population):
    """
    Seleciona os melhores indivíduos da população.
    Os melhores são os que têm maior fitness.
    """
    population.sort(key=lambda x: fitness(x), reverse=True)
    top_20_percent = int(0.2 * population_size)
    return population[:top_20_percent]  # Seleciona os 20% melhores

# Crossover/Cruzamento
def crossover(parent1, parent2):
    """
    Realiza o crossover entre dois pais para criar dois novos filhos.
    """
    crossover_point = random.randint(1, len(target) - 2)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutação
def mutate(individual):
    """
    Realiza mutações aleatórias em um indivíduo.
    """
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ, !")

# Main Loop
# Inicializa a população
population = initialize_population()

# Loop através das gerações
for generation in range(generations):
    # Seleciona os melhores indivíduos
    selected = select(population)

    # Realiza o crossover e a mutação para criar a nova geração
    offspring = []
    while len(offspring) < population_size:
        parent1, parent2 = random.sample(selected, 2)
        child1, child2 = crossover(parent1, parent2)
        mutate(child1)
        mutate(child2)
        offspring.extend([child1, child2])

    # Atualiza a população com os novos filhos
    population = offspring[:population_size]

    # Encontra o melhor indivíduo da geração atual
    best_match = max(population, key=fitness)
    best_match_string = "".join(best_match)
    print(f"Generação {generation}: Melhor Membro '{best_match_string}' com fitness {fitness(best_match)}")

    # Verifica se o melhor indivíduo atingiu o objetivo
    if best_match_string == target:
        print(f"Objetivo '{target}' atingido! Generação: {generation}")
        break
