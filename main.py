import random
import numpy as np
import math
import GeneticAlgorithm

    """
    what we have now is a generation #2 which is improved from the random objects initialized in gen #1. To improve on 
    our gen #2 and to approach an optimal solution, we must run this sequence a N number of times! This can be done in 
    a for-loop
    """

# creating class instance, initialising 1st generation and running our GA
mygen = GeneticAlgorithm(25)
mygen.initialPopulation()
print(mygen.selectiveProcess())









