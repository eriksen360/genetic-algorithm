# genetic-algorithm
Den genetiske algoritme skal modellere en fysisk evolutionær proces ved at chancen for videreførelse af gener til næste generation er 
proportionel med distansen fra et mål. Målet kan i denne instans repræsentere en vilkårlig parameter, men for at kunne modellere udviklingen
i PyGame er en fysisk distance anvendt. 
Algoritmen er heuristisk og grådig, og der ligges derfor vægt på at populutionen ikke nødvendigvis udvikler sig mest optimalt over få generationer
men at der med tid vil opstå en naturlig favorisering af sprites med favourable træk.


Algoritmen er en klasse, der instantieres ved at genere et klasseobjekt, der tager ét positionelt argument og to nøgleordsargumenter

    _class GeneticAlgorithm(self, generationSize, DNAsize, mutationRate)_ 

For at genere en tilfældig population (Gen #1) benytter vi os af funktionen 'InitialPopulation' der ingen parametre tager.
Funktionerne kaldes automatisk ved at bruge 
  
    _mygen.selectiveProcess()_


Output er liste med N sprites der hver er en liste bestående af tal, der i PyGame omsættes til bevægelse.

OBS: Algoritmen er endnu ikke optimeret med NumPy eller Collections, og kan derfor være langsom for store generationer eller for lange DNA-sekvenser, men fungerer fint
for generationsstørrelser optil 100.


 
