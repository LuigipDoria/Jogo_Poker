from Baralho import *
from Jogador import *

class Mesa():

    def __init__(self, nomes):
        self.turno = 0
        self.cartas_mesa = []
        self.dinheiro_mesa = 0
        self.nomes = nomes
        self.jogadores = [] 


    def comeca_partida(self):
        for _ in range(len(self.nomes)):
            self.jogadores.append(Jogador())

        for i in range(len(self.jogadores)):
            self.jogadores[i].rec_dinheiro(500)

    def distribui_cartas(self):
        if self.turno == 0:
            for _ in range(2):
                for i in range(len(self.jogadores)):    
                    self.jogadores[i].add_carta(self.baralho[0])
                    self.baralho.pop(0)

    def add_carta_mesa(self):
        if self.turno == 0:
            for i in range(3):
                self.cartas_mesa.append(self.baralho[0])
                self.baralho.pop(0)
        else:
            self.cartas_mesa.append(self.baralho[0])
            self.baralho.pop(0)

    def recolhe_cartas(self):
        for i in range(len(self.jogadores)):  
            self.jogadores[i].mao = []
        self.cartas_mesa = []

    def rodada(self):
        partida = self.vencedor_partida()
        self.comeca_partida()
        while partida == False:
            aposta_minima = 0
            apostas = 0
            deck = Baralho()
            self.baralho = deck.embaralha()
            n_pessoas_correu = 0
            nova_aposta = True
            n_pessoas_passou = 0
            for self.turno in range (3):
                self.distribui_cartas()
                self.add_carta_mesa()
                n_pessoas_correu = 0 
                fim_rodada = False
                for i in range(len(self.jogadores)):
                    self.jogadores[i].passou = False                            
                while fim_rodada == False:
                    for i in range(len(self.jogadores)):
                        if self.jogadores[i].corre == True:
                            n_pessoas_correu +=1
                    if n_pessoas_correu == len(self.jogadores) - 1:
                        pass
                    else:
                        for i in range(len(self.jogadores)):
                            print("\nTurno do(a): {}".format(self.nomes[i]))
                            print("Quantidade de fichas: {}".format(self.jogadores[i].dinheiro))
                            if self.jogadores[i].corre == False and self.jogadores[i].passou == False:
                                aposta, nova_aposta = self.jogadores[i].acoes(aposta_minima, fim_rodada, apostas, nova_aposta, self.cartas_mesa, self.turno)
                                if aposta > aposta_minima:
                                    aposta_minima  = aposta 
                                apostas += aposta
                                if nova_aposta == True:
                                    for ii in range(len(self.jogadores)):
                                        if ii != i:
                                            self.jogadores[ii].passou = False  
                            elif self.jogadores[i].corre == True:
                                print("{} correu".format(self.nomes[i]))
                            elif self.jogadores[i].passou == True:
                                pass
                    n_pessoas_passou = 0
                    for i in range(len(self.jogadores)):
                        if self.jogadores[i].passou == True:
                            n_pessoas_passou +=1
                        if self.jogadores[i].corre == True:
                            n_pessoas_passou +=1
                    if n_pessoas_passou == len(self.jogadores):
                        fim_rodada = True
                print("\n")
                print("Fim do turno {}".format(self.turno+1))
                print(self.cartas_mesa)
                print("\n")
            fim_rodada = False
            if n_pessoas_correu == len(self.jogadores) - 1:
                    pass
            else:
                while fim_rodada == False:
                    for i in range(len(self.jogadores)):
                        print("\nTurno do(a): {}".format(self.nomes[i]))
                        print("Quantidade de fichas: {}".format(self.jogadores[i].dinheiro))
                        if self.jogadores[i].corre == False:
                                aposta, nova_aposta = self.jogadores[i].acoes(aposta_minima, fim_rodada, apostas, nova_aposta, self.cartas_mesa, self.turno)
                                if aposta > aposta_minima:
                                    aposta_minima  = aposta
                                apostas += aposta
                                if nova_aposta == True:
                                    for ii in range(len(self.jogadores)):
                                        if ii != i:
                                            self.jogadores[ii].passou = False  
                        elif self.jogadores[i].corre == True:
                            print("{} correu".format(self.nomes[i]))
                        elif self.jogadores[i].passou == True:
                            pass
                    n_pessoas_passou = 0
                    for i in range(len(self.jogadores)):
                        if self.jogadores[i].passou == True:
                            n_pessoas_passou +=1
                        if self.jogadores[i].corre == True:
                            n_pessoas_passou +=1
                    if n_pessoas_passou == len(self.jogadores):
                        fim_rodada = True

            
            self.turno = 0
            vencedor = self.vencedor_rodada()
            for i in range(len(self.jogadores)):
                self.jogadores[i].correr(fim_rodada)
                self.jogadores[i].aposta = 0
            self.jogadores[vencedor].rec_dinheiro(apostas)
            fim_rodada = True
            for i in range(len(self.jogadores)):
                print("A mão do(a) {} era {}".format(self.nomes[i],self.jogadores[i].mao))
            print("As cartas da messa eram: {}".format(self.cartas_mesa))
            print()
            print()
            print("-------------------------------")
            print("--O vencedor da rodada foi {}--".format(self.nomes[vencedor]))
            print("-------------------------------")
            print()
            self.recolhe_cartas()
            print("------------------")
            print("--Fim-da-roadada--")
            print("------------------")

            partida = self.vencedor_partida()

    def vencedor_rodada(self):
        vencedor = 0
        maior_pontuacao = 0
        for i in range(len(self.jogadores)):
            n_duplas = 0
            n_trincas = 0
            n_quadra = 0
            naipe_igual_5 = False
            n_naipes_iguais = 0
            sequencia = False
            sequencia_naipe_igual = False
            maior_sequencia_naipe_igual = False
            cartas_sequencia = []
            naipes_sequencia = []
            naipe_carta_1_igual = 1
            naipe_carta_2_igual = 1
            carta_1 = self.jogadores[i].mao[0][0:2]
            carta_2 = self.jogadores[i].mao[1][0:2]
            naipe_carta_1 = self.jogadores[i].mao[0][-1]
            naipe_carta_2 = self.jogadores[i].mao[1][-1]        
            carta_alta_dupla = [0]
            carta_alta_trinca = [0]
            carta_alta_quadra = 0
            carta_alta_naipe_igual = 0
            carta_alta_sequencia = []
            carta_1 = int(carta_1)
            carta_2 = int(carta_2)
            if carta_1 == carta_2:
                dupla = True
                n_duplas += 1
                carta_alta_dupla.append(carta_1)
                for carta in self.cartas_mesa:
                    if carta_1 == carta[0:2]:
                        n_trincas += 1
                        n_duplas -= 1
                        carta_alta_dupla.remove(carta_1)
                        carta_alta_trinca = carta_1
            else:

                dupla = False

                for carta in self.cartas_mesa:
                    carta = int(carta[0:2])
                    if carta_1 == carta and dupla == False:
                        dupla = True
                        n_duplas += 1
                        carta_alta_dupla.append(carta_1)
                    elif carta_1 == carta and dupla == True:
                        n_duplas -= 1
                        n_trincas += 1
                        carta_alta_dupla.remove(carta_1)
                        carta_alta_trinca.append(carta_1)

                dupla = False
                for carta in self.cartas_mesa:
                    carta = int(carta[0:2])
                    if carta_2 == carta and dupla == False:
                        dupla == True
                        n_duplas += 1
                        carta_alta_dupla.append(carta_2)
                    if carta_2 == carta and dupla == True:
                        n_duplas -= 1
                        n_trincas += 1
                        carta_alta_dupla.remove(carta_1)
                        carta_alta_trinca.append(carta_2)
                    
                try:
                    carta_alta_dupla.sort(reverse=True)
                    carta_alta_dupla = carta_alta_dupla[0]
                except:
                    pass
                
                try:
                    carta_alta_trinca.sort(reverse=True)
                    carta_alta_trinca = carta_alta_trinca[0]   
                except:
                    pass

            if naipe_carta_1 == naipe_carta_2:
                n_naipes_iguais = 2
                for naipe in self.cartas_mesa:
                    naipe = naipe[-1]
                    if naipe == naipe_carta_1:
                        n_naipes_iguais += 1
            else:
                for naipe in self.cartas_mesa:
                    naipe = naipe[-1]
                    if naipe_carta_1 == naipe:
                        naipe_carta_1_igual += 1
                    if naipe_carta_2 == naipe:
                        naipe_carta_2_igual +=1          

            if n_naipes_iguais >= 5:
                naipe_igual_5 = True
                carta_alta_naipe_igual = carta_1
            elif naipe_carta_1_igual >= 5: 
                naipe_igual_5 = True
                carta_alta_naipe_igual = carta_1
            elif naipe_carta_2_igual >= 5:
                naipe_igual_5 = True
                carta_alta_naipe_igual = carta_2

            for carta in self.cartas_mesa:
                numero_carta = int(carta[0:2])
                naipe_carta = carta[-1]
                cartas_sequencia.append(numero_carta)
                naipes_sequencia.append(naipe_carta)
            
            cartas_sequencia.append(carta_1)
            cartas_sequencia.append(carta_2)
            naipes_sequencia.append(naipe_carta_1)
            naipes_sequencia.append(naipe_carta_2)

            cartas_sequencia, naipes_sequencia = zip(*sorted(zip(cartas_sequencia, naipes_sequencia)))

            n_cartas_seguidas = 0
            n_naipes_iguais = 0

            for xx in range(len(cartas_sequencia)-1):
                if cartas_sequencia[xx] != cartas_sequencia[xx]:
                    if cartas_sequencia[xx] == cartas_sequencia[xx+1]:
                        n_cartas_seguidas += 1
                        if naipes_sequencia[xx] == naipes_sequencia[xx+1]:
                            n_naipes_iguais += 1
                        else:
                           n_naipes_iguais = 0
                    else:
                        n_cartas_seguidas = 0
            
            if n_cartas_seguidas > 4:
                sequencia = True
                if n_naipes_iguais > 4:
                    sequencia_naipe_igual = True
                    if cartas_sequencia[xx+1] == 14:
                                maior_sequencia_naipe_igual = True

            cartas_sequencia = list(cartas_sequencia)
            naipes_sequencia = list(naipes_sequencia)

            cartas_sequencia.pop(5)
            cartas_sequencia.pop(5)
            naipes_sequencia.pop(5)
            naipes_sequencia.pop(5)

            for x in range(len(cartas_sequencia)):
                if carta_1 == cartas_sequencia[x]:
                    if naipe_carta_1 == naipes_sequencia[x]:
                        carta_alta_sequencia.append(carta_1)
                if carta_2 == cartas_sequencia[x]:
                    if naipe_carta_1 == naipes_sequencia[x]:
                        carta_alta_sequencia.append(carta_2)

            carta_alta_sequencia.sort(reverse=True)

            self.jogadores[i].pontuacao = max(carta_1, carta_2)
            
            if n_duplas == 1:
                try:
                    self.jogadores[i].pontuacao = 14 + carta_alta_dupla
                except:
                    self.jogadores[i].pontuacao = 14 + carta_alta_dupla[0]
            if n_duplas == 2:
                self.jogadores[i].pontuacao = 28 + carta_alta_dupla
            if n_trincas == 1:
                self.jogadores[i].pontuacao = 42 + carta_alta_trinca
            if sequencia == True:
               self.jogadores[i].pontuacao = 56 + carta_alta_sequencia[0]
            if naipe_igual_5 == True:
               self.jogadores[i].pontuacao = 72 + carta_alta_naipe_igual
            if n_trincas == 2 or (n_trincas == 1 and n_duplas == 1):
                self.jogadores[i].pontuacao = 86 + carta_alta_trinca
            if n_quadra == 1:
                self.jogadores[i].pontuacao = 100 + carta_alta_quadra
            if sequencia_naipe_igual == True:
               self.jogadores[i].pontuacao = 114 + carta_alta_sequencia[0]
            if maior_sequencia_naipe_igual == True:
               self.jogadores[i].pontuacao = 130

        for i in range(len(self.jogadores)):
            if self.jogadores[i].corre == False:
                if self.jogadores[i].pontuacao > maior_pontuacao:
                    maior_pontuacao = self.jogadores[i].pontuacao
                    vencedor = i
        return vencedor 

    def vencedor_partida(self):
        n_eliminados = 0
        acabou_partida = False
        for i in range(len(self.jogadores)):
            dinheiro = self.jogadores[i].get_dinheiro()
            if dinheiro <= 0:
                n_eliminados += 1
        if n_eliminados == len(self.jogadores)-1:
            acabou_partida = True
        if acabou_partida == True:
            for i in range(len(self.jogadores)):
                dinheiro = self.jogadores[i].get_dinheiro()
                if dinheiro > 0:
                    vencedor = i
            print()
            print("-------------------------------")
            print("--O vencedor da partida foi {}--".format(self.nomes[vencedor]))
            print("-------------------------------")
        return acabou_partida