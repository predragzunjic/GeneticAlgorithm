import random

class GrafTSP:
    def __init__(self):
        self.n = 0 #broj gradova
        self.pocetniGrad = 2
        self.dictGradova = {}

        {
            1: lista1((2, 11), (3, 15))
            2:
        }

    def ucitajGraf(self):
        print("Unos broja gradova: ")
        self.n = int(input())
        listaSusjeda = []

        for i in range(self.n):
            for j in range(i + 1, self.n):
                listaSusjeda.append((j, random.randint(1, 100)))
            self.dictGradova[i] = listaSusjeda
            listaSusjeda = []

        for i in range(1, self.n):
            for j in range(i):
                for k in range(len(self.dictGradova[j])):
                    if(self.dictGradova[j][k][0] == i):
                        self.dictGradova[i].append((j, self.dictGradova[j][k][1]))
                        
