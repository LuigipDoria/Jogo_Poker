import random as rd

class Baralho():

    def __init__(self):
        self.naipes = ["P", "C", "E", "M"] # P -> Paus, C -> Copas, E -> Espadas, M -> Moles
        self.n_cartas = 15
        self.baralho = []

    def cria_baralho(self):
        for naipe in self.naipes:
            for i in range(2, self.n_cartas):
                self.baralho.append(str(i) + " " + naipe)

    def embaralha(self):
        self.cria_baralho()
        rd.shuffle(self.baralho)
        return self.baralho