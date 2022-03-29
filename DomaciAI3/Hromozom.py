import random
import GrafTSP
class Hromozom:
    def __init__(self, geni, g):
        self.geni = []
        for i in geni:
            self.geni.append(i)
        self.fitnes = self.fitness(g)
        self.pragMutacije = 0.08

    def fitness(self, g):
        suma = 0
        for i in range(len(self.geni) - 1):
            listaSusjeda = g.dictGradova[self.geni[i]]
            for j in listaSusjeda:
                if(j[0] == self.geni[i + 1]):
                    suma += j[1]
                    break

        for i in g.dictGradova[self.geni[0]]:
            if(i[0] == self.geni[g.n - 1]):
                suma += i[1]
                break
        return suma

    def mutacija(self, h, g):
        sansaZaMutaciju = random.random()

        if(sansaZaMutaciju <= self.pragMutacije):
            indeks1 = random.randint(0, g.n - 2)
            indeks2 = random.randint(0, g.n - 2)

            while(indeks1 == indeks2):
                indeks2 = random.randint(0, g.n - 2)

            h[indeks1], h[indeks2] = h[indeks2], h[indeks1]

        return h


    def razmnozavanje(self, hr1, hr2, g):
        h1 = []
        for i in hr1.geni:
            h1.append(i)
        h1.remove(g.pocetniGrad)

        h2 = []
        for i in hr2.geni:
            h2.append(i)
        h2.remove(g.pocetniGrad)

        dijete1 = []
        dijete2 = []
        granica1 = random.randint(1, g.n - 1)
        granica2 = random.randint(1, g.n - 1)

        while(granica1 == granica2):
            granica2 = random.randint(1, g.n - 1)

        if(granica1 > granica2):
            granica1, granica2 = granica2, granica1

        h1Temp = []
        h2Temp = []
        krajListe1 = []
        krajListe2 = []
        dijete1 = []
        dijete2 = []
        potrebnaDuzinaNaKraj1 = 0
        potrebnaDuzinaNaKraj2 = 0
        trenutnaDuzinaNaKraj1 = 0
        trenutnaDuzinaNaKraj2 = 0

        for i in range(granica1, granica2):
            dijete1.append(h1[i])
            dijete2.append(h2[i])

            h1Temp.append(h2[i])
            h2Temp.append(h1[i])

        for i in range(granica2, g.n - 1):
            krajListe1.append(h1[i])
            krajListe2.append(h2[i])

        potrebnaDuzinaNaKraj1 = len(krajListe1)
        potrebnaDuzinaNaKraj2 = len(krajListe2)

        for i in range(len(h1Temp)):
            h1.remove(h1Temp[i])
            h2.remove(h2Temp[i])

            if(h1Temp[i] in krajListe1):
                krajListe1.remove(h1Temp[i])

            if(h2Temp[i] in krajListe2):
                krajListe2.remove(h2Temp[i])

        trenutnaDuzinaNaKraj1 = len(krajListe1)
        trenutnaDuzinaNaKraj2 = len(krajListe2)
        h1Temp = []
        h2Temp = []

        for i in range(len(krajListe1)):
            if(krajListe1[i] in h1):
                h1.remove(krajListe1[i])


        for i in range(len(krajListe2)):
            if(krajListe2[i] in h2):
                h2.remove(krajListe2[i])


        for i in range(potrebnaDuzinaNaKraj1 - trenutnaDuzinaNaKraj1):
            krajListe1.append(h1[i])
            h1Temp.append(h1[i])


        for i in range(potrebnaDuzinaNaKraj2 - trenutnaDuzinaNaKraj2):
            krajListe2.append(h2[i])
            h2Temp.append(h2[i])


        for i in range(len(h1Temp)):
            h1.remove(h1Temp[i])


        for i in range(len(h2Temp)):
            h2.remove(h2Temp[i])


        dijete1 = dijete1 + krajListe2
        dijete2 = dijete2 + krajListe1
        dijete1 = h2 + dijete1
        dijete2 = h1 + dijete2

        dijete1 = self.mutacija(dijete1, g)
        dijete2 = self.mutacija(dijete2, g)

        dijete1 = [g.pocetniGrad] + dijete1
        dijete2 = [g.pocetniGrad] + dijete2

        hr1 = Hromozom(dijete1, g)
        hr2 = Hromozom(dijete2, g)

        return (hr1, hr2)
