# genetic-algorithm

Algoritmen er en klasse, der instantieres ved at genere et klasseobjekt, der tager ét positionelt argument og to nøgleordsargumenter

    _class GeneticAlgorithm(self, generationSize, DNAsize, mutationRate)_ 

For at genere en tilfældig population (Gen #1) benytter vi os af funktionen 'InitialPopulation' der ingen parametre tager.
Funktionerne kaldes automatisk ved at bruge 
  
    _mygen.selectiveProcess()_


Output er liste med N sprites der hver er en liste bestående af tal, der i PyGame omsættes til bevægelse.

OBS: Algoritmen er endnu ikke optimeret med NumPy eller Collections, og kan derfor være langsom for store generationer eller for lange DNA-sekvenser, men fungerer fint
for generationsstørrelser optil 100.


 
