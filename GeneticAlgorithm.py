# Implementation af metoder til selektion. Hver sprite tildeles en fitness score baseret på deres 
# afstand fra målet

class GeneticAlgorithm():

    def __init__(self, generationSize, DNAsize=50, mutationRate=50):
        self.generationSize = generationSize
        self.mutationRate = mutationRate
        self.DNAsize = DNAsize
        
    # generate initial population with random genotype and randomized movement
    # remove global variables
    def initialPopulation(self):

        global genotype
        global car_objects
        global index
        
        genotype = np.linspace(0, math.pi, self.generationSize).reshape(1, self.generationSize)
        genotype = np.ravel(genotype)
        object_list = []
        car_objects = object_list
        for i in range(self.generationSize):
            object_list.append([round(random.choice(genotype), 4) for n in range(self.DNAsize)])
        index = [i for i in range(len(car_objects))]

        return index, car_objects

      # returns position of car on grid (implemented in pyGame)
    def position(self, x, y):
        car_position = _
        return car_position

    def selectiveProcess(self, tournament_size=5):

        goal = tuple(list([240, 300]))  # goal position is fixed on 'map'
        z = tuple(list([100, 110]))  
        car_position = []
        for i in range(self.generationSize):
            car_position.append(z)

        # computing the distance from car_object to goal
        delta_x = []
        delta_y = []
        for idx in range(len(car_position)):
            goal_to_car_x = goal[0] - car_position[idx][0]
            delta_x.append(goal_to_car_x)
            goal_to_car_y = goal[1] - car_position[idx][1]
            delta_y.append(goal_to_car_y)

        # calcule fitness score (currently unweighted, expermentation allows for adjustment of parameters)
        fitness = []
        for i in range(len(car_position)):
            distance_to_goal = math.sqrt(delta_x[i]**2 + delta_y[i]**2)
            fitness.append(1 / distance_to_goal)
        fitness = np.array(fitness)
        print('Avg fitness score: ', np.average(fitness))
        fitness_score = list(zip(index, car_objects, fitness))
       
      
        # selection algorithm: Comparison of fitness score to determine probability of advancement of genes to next generation
        def tournament_selection():

            tournament_winners = []
            tournament = []
            # every car object is zipped with its fit-score in tuple like (idx, DNA, fitnessScore)
            num_of_tournaments = int(len(car_objects) / tournament_size)
            # chosing our five best car_objects based on fitness_score
            for n in range(num_of_tournaments):
                for i in range(tournament_size):
                    rand = random.choice(fitness_score)  
                    tournament.append(rand)
                    i_rand = np.argwhere(fitness_score == rand)
                    np.delete(rand, i_rand)
                tournament_winners.append(max(tournament, key=lambda x: x[2]))
                tournament.clear()

            return tournament_winners
       
     
        #6 tournament winners are used to crossover-mutate 
        def crossover_mutation():
            DNA_lens = self.DNAsize / 2
            meldedDNA = []

            # new population (gen N + 1) is created
            for i in range(len(tournament_selection())):
                rand1 = tournament_selection()[i][1]
                for j in range(len(tournament_selection())):
                    rand2 = tournament_selection()[j][1]
                    if rand1 != rand2:
                        meldedDNA.append((rand1[:13] + rand2[13:]))
           # DNA is mutated at some rate, given by our mutationRate kwargs
            probability = self.mutationRate
            for child_object in meldedDNA:
                for strand in child_object:
                    if np.random.random() <= probability:
                        strand = np.random.choice(genotype) 
            return meldedDNA

       crossover_mutation()
       
