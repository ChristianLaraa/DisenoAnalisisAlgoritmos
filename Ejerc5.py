# cifrado cesar
from operator import index

alfabeto = "abcdefghijklmnopqrstuvwxyz"
len(alfabeto)
print(len(alfabeto))

cad= "hola"

alfabeto[10]
print(alfabeto[10])

alfabeto.index('h')
print(alfabeto.index('h'))

pos=alfabeto.index('h')
print(pos)

llave=3

alfabeto[(pos+llave)]
print(alfabeto[(pos+llave)])

#codigo
def cifra_cesar(cad,llave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cifrada = ""
    for c in cad:
        if c in alfabeto:
            pos = alfabeto.index(c)
            cifrada = cifrada + alfabeto[(pos+llave)%26]
        else:
            cifrada += c
    a = 'hola buenos dias'
    b = a.split()
print(cifra_cesar("hola", 3))

