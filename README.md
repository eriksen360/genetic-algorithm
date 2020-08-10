# genetic-algorithm

Algoritmen er en klasse, der instantieres ved at genere et klasseobjekt, der tager ét positionelt argument og to nøgleordsargumenter

----

class GeneticAlgorithm(self, generationSize, DNAsize=, mutationRate=)

----

For at genere en tilfældig population (Gen #1) benytter vi os af funktionen 'InitialPopulation' der ingen parametre tager.
Funktionerne kaldes automatisk ved at bruge

----

mygen.selectiveProcess()

----

Outputtet her bliver således en liste med N antal objekter / sprites der hver er en liste bestående af tal, der i Pygame omsættes til bevægelse.

OBS: Algoritmen er endnu ikke optimeret med NumPy eller Collections, og kan derfor være langsom for store generationer eller for lange DNA-sekvenser


 
