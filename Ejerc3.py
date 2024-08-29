# Christian Gael Lara Martinez, 29/08/24
import time
from random import random, randint

z = '-------------------------------------------------------------------------'
print('------------------------------------------------------------------')
print('Clase 29/08/24')

for c in range(10, 1, -2):
    print(c)

a = 10
print(a)

print(z)
n = 10
lista = []
while len(lista) < n:
    ale = randint(0,n)
    if not (ale in lista):
        lista.append(ale)
inicio = time.time()
for j in range(n):
    for i in range(n-1):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
fin = time.time()
print(fin - inicio)

print('----------------------------------------------------------------')
inicio = time.time()
listaA = []
listaB = []
for e in lista:
        if e>(n/2):
            listaB.append(e)
        else:
            listaA.append(e)
#ordena la lista A
for j in range(len(listaA)):
        for i in range(len(listaA)-1):
            if listaA[i]>listaA[i+1]:
                listaA[i], listaA[i+1] = listaA[i+1], listaA[i]
#ordena la lista B
for j in range(len(listaB)):
    for i in range(len(listaB)-1):
        if listaB[i]>listaB[i+1]:
            listaB[i], listaB[i+1] = listaB[i+1], listaB[i]
fin= time.time()
print(fin-inicio)

