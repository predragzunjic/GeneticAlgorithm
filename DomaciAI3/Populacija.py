import random
import Hromozom
import GrafTSP


class Populacija:
    def __init__(self):
        self.velicinaPopulacije = 50
        self.populacija = []

    def generisiPocetnuPopulaciju(self, g):
        baznaLista = []

        for i in range(g.n):
            baznaLista.append(i)

        baznaLista.remove(g.pocetniGrad)

        for i in range(self.velicinaPopulacije):
            random.shuffle(baznaLista)
            baznaLista = [g.pocetniGrad] + baznaLista
            h = Hromozom.Hromozom(baznaLista, g)
            self.populacija.append(h)
            baznaLista.remove(g.pocetniGrad)


    def generisiNovuPopulaciju(self, g):
        brojUcesnikaTurnira = int(self.velicinaPopulacije / 3)
        par = []
        listaDjece = []

        for i in range(self.velicinaPopulacije):
            listaUcesnikaTurnira = []
            checkLista = []
            for j in range(brojUcesnikaTurnira):
                indeksUcesnika = random.randint(0, self.velicinaPopulacije - 1)
                while(indeksUcesnika in checkLista):
                    indeksUcesnika = random.randint(0, self.velicinaPopulacije - 1)

                checkLista.append(indeksUcesnika)
                listaUcesnikaTurnira.append(self.populacija[indeksUcesnika])

            minFitnes = listaUcesnikaTurnira[0].fitnes
            putMinFitnes = listaUcesnikaTurnira[0].geni

            for j in range(len(listaUcesnikaTurnira)):
                if(listaUcesnikaTurnira[j].fitnes < minFitnes):
                    minFitnes = listaUcesnikaTurnira[j].fitnes
                    putMinFitnes = listaUcesnikaTurnira[j].geni

            par.append(putMinFitnes)
            djeca = ()

            if(i % 2 == 1):
                hr1 = Hromozom.Hromozom(par[0], g)
                hr2 = Hromozom.Hromozom(par[1], g)
                djeca = hr1.razmnozavanje(hr1, hr2, g)
                par = []
                listaDjece.append(djeca[0])
                listaDjece.append(djeca[1])

        self.populacija.clear()
        for i in listaDjece :
            self.populacija.append(i)
