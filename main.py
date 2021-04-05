import random
import numpy as np
import math


class GeneticAlgorithm():

    def __init__(self, generationSize, DNAsize=26, mutationRate=26):
        self.generationSize = generationSize
        self.mutationRate = mutationRate
        self.DNAsize = DNAsize


    # generate initial population
    def initialPopulation(self):

        # array of possible actions, used in creating a sequence of DNA
        global genotype
        genotype = np.linspace(0, math.pi, self.generationSize).reshape(1, self.generationSize)
        genotype = np.ravel(genotype)


        # creating cars in generation 1 with each car having 26 randomized movements to begin with, chosen based on
        # possible movements in a 180 FOW
        global car_objects
        object_list = []
        car_objects = object_list

        for i in range(self.generationSize):
            object_list.append([round(random.choice(genotype), 4) for n in range(self.DNAsize)])

        # indexing our objects
        global index
        index = [i for i in range(len(car_objects))]

        return index, car_objects

    # POSITION FUNC NOT DONE YET
    def position(self, x, y):
        # input for gen 2 = car_objects
        # input for gen 2 = meldedDNA

        car_position = _

        # output = position of car from gen 2

        return car_position

    def selectiveProcess(self, tournament_size=5):

        goal = tuple(list([240, 300]))  # goal position is fixed on 'map'
        z = tuple(list([100, 110]))  # must be changed to input from game!
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

        # calculating our fitness score for each car
        fitness = []

        for i in range(len(car_position)):
            distance_to_goal = math.sqrt(delta_x[i]**2 + delta_y[i]**2)
            fitness.append(1 / distance_to_goal)
            # should we scale ( 1 / d ) by factor k so absolute score gets bigger?

        fitness = np.array(fitness)

        print('Avg fitness score: ', np.average(fitness))
        fitness_score = list(zip(index, car_objects, fitness))

        def tournament_selection():

            tournament_winners = []
            tournament = []

            # every car object is zipped with its fit-score in tuple like (idx, DNA, fitnessScore)
            num_of_tournaments = int(len(car_objects) / tournament_size)

            # chosing our five best car_objects based on fitness_score
            for n in range(num_of_tournaments):
                for i in range(tournament_size):

                    # appending 5 random tuples from fitness_score to our tournament
                    rand = random.choice(fitness_score) # calls self.fit_calc!!!
                    tournament.append(rand)
                    i_rand = np.argwhere(fitness_score == rand)
                    np.delete(rand, i_rand)

                tournament_winners.append(max(tournament, key=lambda x: x[2]))
                tournament.clear()

            return tournament_winners
        """
        only the 6 tournament winners (6 most fit) are used to crossover-mutate 
        """

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

                #tournament_selection()[2].remove(rand1) # tuples are immutable!


           # DNA is mutated at some rate, given by our mutationRate kwargs
            probability = self.mutationRate
            for child_object in meldedDNA:
                for strand in child_object:
                    if np.random.random() <= probability:
                        strand = np.random.choice(genotype) # do we actually change the meldedDNA? Our only copy list?

            # a nested list with 22 new elements all with 26 strands of modified DNA
            return meldedDNA

        crossover_mutation()

    """
    what we have now is a generation #2 which is improved from the random objects initialized in gen #1. To improve on 
    our gen #2 and to approach an optimal solution, we must run this sequence a N number of times! This can be done in 
    a for-loop
    """

# creating class instance, initialising 1st generation and running our GA
mygen = GeneticAlgorithm(25)
mygen.initialPopulation()
print(mygen.selectiveProcess())

# our melded_DNa must be of same data structure as init_pop, to make it work iteratively in PyGame
# position function needs to be improved upon, hereunder the breakj mechanism for when one car_object reaches its goal








