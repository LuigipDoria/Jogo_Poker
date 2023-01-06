class Jogador():

    def __init__(self):
        self.mao = []
        self.pontuacao = 0
        """

        o numero da carta é referente as cartas na mão do jogador

        carta alta                  = 0   + numero da carta alta                -> 0   ate 14
        dupla                       = 14  + numero da carta                     -> 16  ate 28
        2 duplas                    = 28  + numero da carta da maior dupla      -> 30  ate 42
        trinca                      = 42  + numero da carta                     -> 44  ate 56
        sequencia                   = 56  + numero mais alto da sequencia       -> 58  ate 72
        5 naipe igual               = 72  + numero da carta mais alta           -> 74  ate 86
        trinca e dupla              = 86  + numero da carta mais alta           -> 88  ate 100
        quadra                      = 100 + numero da carta                     -> 102 ate 114
        sequencia naipe igual       = 114 + numero da carta mais alta           -> 116 ate 128
        maior sequencia naipe igual = 130                                       -> 130

        """
        self.dinheiro = 0
        self.corre = False
        self.passou = False
        self.aposta = 0
        self.dinheiro_cobrir = 0
    
    def acoes(self, aposta_minima,fim_rodada, apostas, nova_aposta, cartas_mesa, turno):
        self.dinheiro_cobrir = aposta_minima - self.aposta
        while True:
            print("\n")
            print("Qual ação você deseja realizar?")
            print("1- Ver mão")
            print("2- Apostar")
            print("3- Cobrir (Quantia para cobrir a aposta: {})".format(self.dinheiro_cobrir))
            print("4- Correr")
            print("5- Passar")
            print("6- Ver quanto já foi apostado nessa rodada")
            print("7- Ver as cartas da mesa")

            acao = int(input("Digite o numero da ação: "))

            if acao == 1:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("Sua mão é: {} | {}".format(self.mao[0], self.mao[1]))
            elif acao == 2:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                aposta = self.apostar(aposta_minima)
                self.aposta += aposta
                nova_aposta = True
                self.passou = True
                return self.aposta, nova_aposta
            elif acao == 3:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                aposta = self.cobrir(self.dinheiro_cobrir)
                self.aposta += aposta
                nova_aposta = False
                self.passou = True
                return self.aposta, nova_aposta
            elif acao == 4:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                self.correr(fim_rodada)
                aposta = 0
                nova_aposta = False
                return aposta, nova_aposta
            elif acao == 5:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                self.passa(nova_aposta)
                aposta = 0
                nova_aposta = False
                return aposta, nova_aposta
            elif acao == 6:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("Nessa rodada já foi apostado: ", apostas)
            elif acao == 7:
                if turno == 0:
                    print("Não tem cartas na mesa ainda")
                else:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("As cartas da mesa são: ", end= " ")
                    for i in range(len(cartas_mesa)-1):
                        print(cartas_mesa[i], end=" | ")
                    print(cartas_mesa[len(cartas_mesa)-1])
            
    def apostar(self, aposta_minima):
        aposta = 0
        fim_rodada = False
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Valor minimo da aposta é: {} e o Valor maximo de aposta é: {}".format(self.dinheiro_cobrir+1, self.dinheiro))
        try:
            aposta = int(input("Quantia da aposta: "))
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            self.dinheiro -= aposta
        except ValueError:
            self.correr(fim_rodada)
            aposta = aposta_minima

        return aposta

    def cobrir(self,aposta_minima):
        aposta = aposta_minima
        self.dinheiro -= aposta
        return aposta
        
    def correr(self, fim_rodada):
        self.corre = True
        if fim_rodada == True:
            self.corre = False

    def add_pontuacao(self, pontos, fim_rodada):
        self.pontuação += pontos
        if fim_rodada == True or self.corre == True:
            self.pontuação = 0

    def rec_dinheiro(self, dinheiro):
        self.dinheiro += dinheiro

    def add_carta(self, carta):
        self.mao.append(carta)

    def get_dinheiro(self):
        return self.dinheiro
    
    def passa(self, nova_aposta):
        if nova_aposta == True:
            self.passou = False
        else:
            self.passou = True
