import random as rd

"""carta = "10 P"
naipe = carta[-1]
carta = int(carta[0:2])


print(carta)
print(naipe)"""

#print(len([1,2,3,4]))

"""for i in range(10):
    dealer = rd.randint(0,3)
    print(dealer)"""

cartas_sequencia = []
naipes_sequencia = []

cartas_mesa = ["5 P", "6 M", "2 C", "14 E"]

for carta in cartas_mesa:
    numero_carta = int(carta[0:2])
    naipe_carta = carta[-1]
    cartas_sequencia.append(numero_carta)
    naipes_sequencia.append(naipe_carta)

cartas_sequencia, naipes_sequencia = zip(*sorted(zip(cartas_sequencia, naipes_sequencia)))

print(list(cartas_sequencia))
print(list(naipes_sequencia))

lista1 = [5, 3, 4 ,9 ,2]
lista1.sort()
print(lista1)