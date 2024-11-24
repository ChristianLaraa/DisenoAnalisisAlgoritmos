import matplotlib.pyplot as plt

# Lista de las frecuencias comunes en frances, para referencia
frecuencia_frances = ['E', 'A', 'S', 'I', 'N', 'T', 'R', 'U', 'L', 'O', 'D', 'M', 'C', 'P', 'V', 'Q', 'G', 'B', 'F', 'H',
                      'J', 'X', 'Y', 'Z', 'K', 'W']


# Función para cargar el diccionario de palabras en frances
def cargar_diccionario():
    with open('wordsfrances.txt', 'r') as archivo:
        palabras = archivo.read().split()
    print(f"Se han cargado {len(palabras)} palabras.")
    return set(palabras)


# Función para leer el texto cifrado
def cargar_texto_cifrado():
    with open('textocifradodos.txt', 'r') as archivo:
        return archivo.read()


# Calcular frecuencias de letras en el texto cifrado
def calcular_frecuencias(texto):
    frecuencias = {}
    for letra in texto:
        if letra.isalpha():
            letra = letra.lower()
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return sorted(frecuencias.items(), key=lambda item: item[1], reverse=True)


# Función para mostrar el gráfico de las frecuencias
def mostrar_grafico(frecuencias):
    letras = [item[0] for item in frecuencias]
    cantidad = [item[1] for item in frecuencias]

    plt.bar(letras, cantidad, color='red')
    plt.xlabel('Letras')
    plt.ylabel('Frecuencia')
    plt.title('Frecuencia de letras en el texto cifrado')
    plt.show()


# Función para descifrar el texto usando un diccionario de sustitución
def descifrar_texto(texto, sustitucion):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            resultado += sustitucion.get(letra.lower(), letra).lower()
        else:
            resultado += letra
    return resultado


# Cargar el diccionario de palabras y el texto cifrado
diccionario_palabras = cargar_diccionario()
texto_cifrado = cargar_texto_cifrado()

# Calcular las frecuencias de letras en el texto cifrado
frecuencias_letras = calcular_frecuencias(texto_cifrado)

# Definir el diccionario de sustitución
sustitucion = {
    'a': 'f',
    'b': 'a',
    'c': 'h',
    'd': 'm',
    'e': 'e',
    'f': 'y',
    'g': 'f',
    'h': 'd',
    'i': 't',
    'j': 'o',
    'k': 'x',
    'l': 'u',
    'm': 'a',
    'o': 'f',
    'p': 'g',
    'q': 'v',
    'r': 'p',
    's': 'c',
    'u': 'r',
    'v': 'l',
    'w': 'i',
    'x': 's',
    'y': 'n',
    'z': 'j',
}

# Descifrar el texto cifrado
texto_descifrado = descifrar_texto(texto_cifrado, sustitucion)
print("Texto descifrado:\n", texto_descifrado)

# Mostrar el gráfico con las frecuencias
mostrar_grafico(frecuencias_letras)