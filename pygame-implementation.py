import pygame # you need XCode for download
import numpy as np
import random
import math

pygame.init()

# Creating game window
pygame.display.set_caption("gen-alg")
icon = pygame.image.load("Sketchpad.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1000, 1000))
background = pygame.image.load("bane.png")

# Rendering sprite
playerImg = pygame.image.load("reddot.png")
PlayerX = 72
PlayerY = 408

def player(x, y):
    screen.blit(playerImg, (x, y))


# Sprite DNA
xlist = []
ylist = []
DNA_size = 5000
spriteDNA = np.random.randint(low=0, high=5, size=DNA_size)


running = True
searhing_optimal = True
c = 0 # what variable does c represent?
generation = 0
movements = 0
step_change = 5
final_position = []


while searhing_optimal:
    while running:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Using DNA values ranging 0 - 4 to create movement
        if spriteDNA[movements] == 0:
            PlayerX += step_change
        if spriteDNA[movements] == 1:
            PlayerX -= step_change
        if spriteDNA[movements] == 2:
            PlayerY += step_change
        if spriteDNA[movements] == 4:
            PlayerY -= step_change


        # Using RGB value of course to kill movement
        print(screen.get_at((PlayerX, PlayerY)))

        if c == 0:
            if screen.get_at(((PlayerX), (PlayerY))) == (0, 0, 1, 255):
                c += 1
                print(PlayerX, PlayerY)
            elif screen.get_at((PlayerX + playerImg.get_width(), PlayerY)) == (0, 0, 1, 255):
                c += 1
                print(PlayerX, PlayerY)
            elif screen.get_at((PlayerX, PlayerY + playerImg.get_height())) == (0, 0, 1, 255):
                c += 1
                print(PlayerX, PlayerY)
            elif screen.get_at((PlayerX + playerImg.get_width(), PlayerY + playerImg.get_height())) == (0, 0, 1, 255):
                c += 1
                print(PlayerX, PlayerY)

            final_position.append((zip(PlayerX, PlayerY)))
            generation += 1
            player(PlayerX, PlayerY)

    movements += 1
    pygame.display.update()

    distance_X = []
    distance_Y = []
    goal = (700, 200)
    for idx in range(len(final_position)):
            delta_X = goal[0] - final_position[idx][0]
            delta_Y = goal[1] - final_position[idx][1]
            distance_X.append(delta_X)
            distance_Y.append(delta_Y)

            if distance_X <= 2 and distance_Y <= 2:
                print(final_position[idx])
                print(generation)
                searching_optimal = False

    fitness_scores = []
    for i in range(len(distance_X)):
        fitness_scores.append(10**5 / (math.sqrt(distance_X[i]**2 + distance_Y[i]**2)))

    tournament_winners = []
    tournament = []
    tournament_size = 5
    num_of_tournaments = int(len(final_position) / tournament_size)

    for n in range(num_of_tournaments):
        for index in range(tournament_size):

            rand = random.choice(fitness_scores)
            tournament.append(rand)
            i_rand = np.argwhere(fitness_scores == rand)
            np.delete(rand, i_rand)

            tournament_winners.append(max(tournament, key=lambda x: x[2]))
            tournament.clear()

    meldedDNA = []

    for i in range(len(fitness_scores)):
        rand1 = fitness_scores[i]
        for j in range(len(tournament_winners)):
            rand2 = tournament_winners
            if rand1 != rand2:
                meldedDNA.append((rand1[:(DNA_size / 2)] + rand2[(DNA_size / 2):]))

    mutation_probability = .01
    for child_object in meldedDNA:
        for _ in child_object:
            if np.random.random() <= mutation_probability:
                strand = np.random.choice(spriteDNA)






