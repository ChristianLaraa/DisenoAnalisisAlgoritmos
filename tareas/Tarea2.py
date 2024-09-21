# Tarea 2, Christian Gael Lara Martinez, 1507
def cargar_palabras():
    with open('words.txt', 'r') as archivo:
        contenido = archivo.readline()
    lista_palabras = contenido.split()
    print(len(lista_palabras), 'palabras cargadas')
    return lista_palabras

def cargar_texto_cifrado():
    with open('textoCifrado.txt', 'r') as archivo:
        texto_cifrado = archivo.readline()
    return texto_cifrado

def cifrado_cesar(texto, desplazamiento):
    if desplazamiento < 0:
        desplazamiento = 26 - desplazamiento
    texto_cifrado = ""
    abecedario = 'abcdefghijklmnopqrstuvwxyz'

    for letra in texto:
        if letra in abecedario:
            indice = abecedario.index(letra)
            nueva_letra = abecedario[(indice + desplazamiento) % 26]
            texto_cifrado += nueva_letra
        else:
            texto_cifrado += letra
    return texto_cifrado

def descifrar_cesar(texto, desplazamiento):
    return cifrado_cesar(texto, 26 - desplazamiento)

def contar_aciertos(lista_palabras, diccionario):
    aciertos = 0
    for palabra in lista_palabras:
        if palabra in diccionario:
            aciertos += 1
    return aciertos

palabras = cargar_palabras()
texto = cargar_texto_cifrado()
max_aciertos = 0
mejor_llave = 0

for llave in range(26):
    texto_descifrado = descifrar_cesar(texto, llave)
    lista_palabras_descifradas = texto_descifrado.split()
    aciertos = contar_aciertos(lista_palabras_descifradas, palabras)

    if aciertos > max_aciertos:
        max_aciertos = aciertos
        mejor_llave = 26 - llave

print("La llave encontrada es:", mejor_llave)
print("Texto descifrado:")
print(cifrado_cesar(texto, mejor_llave))
