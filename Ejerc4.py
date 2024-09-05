# Lara Martinez Christian Gael 3/09/2024

#Ordenamiento burbuja o(^2)
#Adivinar un numero por biparticion 0log(n)
#Ordenamiento Rápido 0 (n log_2n)

#Preguntas                             tamaño del problema
# 0                  2^0=                      1
# 1                  2^1=                      2
# 2                  2^2=                      4
# 3                  2^3=                      8
# 4                  2^4=                      16
# 5                  2^5=                      32

# 2^x=n -> x=log_2(n)

#Agregar en una cola tiene un coste 0(1)
#Quitar un elemento de una cola tiene un coste 0(1)

#Quitar o agregar un elemento en una pila tiene un coste 0(1)

#Ejemplo de orden constante

#costo computacional que tenga agregar un elemento en una pila

#tenemos paquetes de 5, 8 y 24 plumas, si alguien quiere 1,2,3,4,6,7,9,11,12,14,17,...,etc. nose puede armar el paquete, solo se pueden armar paquetes con las suma de los paquetes completos, encntrar un algoritmos que dado un numero se pueda armar el paquete completo

#Cifrados de Cesar

#A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z

#26 letras

#Cifrar hola con un desplazamiento de 3
# 3---> krod
# <---3 hola
#O(26)

print('-----------------------------------------------------------------------------------------------------------------')

def doble(algo):
    return (algo*2)

def triple(algo):
    return (algo*3)

print(doble(2))
print(doble(1.1))
print(doble("hola"))
print(doble(True))

print(doble(triple(2)))

print(triple("holaholahola"))

print(triple(triple(doble(1.1))))

print("-----------------------------------------------------------------------------------------------------------------")

def cifrado_cesar(texto):
    resultado = ""

    for letra in texto:
        if letra.isalpha():  # Verifica si es una letra
            nueva_letra = chr((ord(letra) + 3))
            resultado += nueva_letra
        else:
            resultado += letra  # Deja los caracteres no alfabéticos sin cambios

    return resultado

# Ejemplo de uso:
texto_original = "hola"
texto_cifrado = cifrado_cesar(texto_original)
print(texto_cifrado)  # Salida: "krod"

print("-----------------------------------------------------------------------------------------------------------------")

def cifra_cesar(cad,llave):
    cad_cifrada = ""
    for letra in cad:
        if letra.isalpha():
            valor = ord(letra)
            valor = valor + llave
            if valor > ord('z'):
                valor = valor - 26
            nueva_letra = chr(valor)
            cad_cifrada = cad_cifrada + nueva_letra
        else:
            cad_cifrada = cad_cifrada + letra
    return cad_cifrada


alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
len(alfabeto)
26
cad = "hola"
alfabeto[10]
alfabeto.index('h')
pos = alfabeto.index('h')
pos
llave = 3
alfabeto[pos + llave]

def cifra_cesar1(cad, llave):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    cifrada = ""
    for c in cad:
        pos = alfabeto.index(c)
        cifrada = cifrada + alfabeto[pos + llave]

print(cifra_cesar1("yo", 3))