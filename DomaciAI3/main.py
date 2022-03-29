import GrafTSP
import Hromozom
import Populacija
import time

def greedyAlgorithm(g, p):
    visited = []
    visited.append(g.pocetniGrad)
    minPut = 200
    minSusjed = 0
    suma = 0

    for i in range(g.n - 1):
        listaSusjeda = g.dictGradova[visited[len(visited) - 1]]
        for j in listaSusjeda:
            if(j[1] < minPut and j[0] not in visited):
                minPut = j[1]
                minSusjed = j[0]

        visited.append(minSusjed)
        suma += minPut
        minPut = 200

    for i in g.dictGradova[visited[len(visited) - 1]]:
        if(i[0] == g.pocetniGrad):
            suma += i[1]
    print(visited)
    return suma



p = Populacija.Populacija()
g = GrafTSP.GrafTSP()
g.ucitajGraf()
p.generisiPocetnuPopulaciju(g)
pocetnoVrijeme = time.time()
for i in range(1000):
    p.generisiNovuPopulaciju(g)

minFitnes = p.populacija[0].fitnes
minPut = p.populacija[0].geni
for i in range(len(p.populacija)):
    if(p.populacija[i].fitnes < minFitnes):
        minFitnes = p.populacija[i].fitnes
        minPut = p.populacija[i].geni

for i in g.dictGradova.items():
    print(i)
    print()

print(minPut, " ", minFitnes)
print(greedyAlgorithm(g, p), "Poredjenje sa obicnim greedy algoritmom")
krajnjeVrijeme = time.time()
print(krajnjeVrijeme - pocetnoVrijeme)
