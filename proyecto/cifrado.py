import matplotlib.pyplot as plt

# Lista de las frecuencias comunes en inglés, para referencia
frecuencia_ingles = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B',
                     'V', 'K', 'J', 'X', 'Q', 'Z']


# Función para cargar el diccionario de palabras en inglés
def cargar_diccionario():
    with open('words.txt', 'r') as archivo:
        palabras = archivo.read().split()
    print(f"Se han cargado {len(palabras)} palabras.")
    return set(palabras)


# Función para leer el texto cifrado
def cargar_texto_cifrado():
    with open('textocidradouno.txt', 'r') as archivo:
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

    plt.bar(letras, cantidad, color='blue')
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
    'a': 'h',
    'b': 'p',
    'c': 'r',
    'd': 'w',
    'e': 'k',
    'f': 'q',
    'g': 'y',
    'h': 'f',
    'i': 'c',
    'j': 'i',
    'k': 'v',
    'l': 'e',
    'm': 'u',
    'n': 's',
    'o': 'a',
    'p': 'x',
    'q': 't',
    'r': 'l',
    's': 'b',
    't': 'g',
    'u': 'j',
    'v': 'm',
    'w': 'z',
    'x': 'o',
    'y': 'n',
    'z': 'd',
}

# Descifrar el texto cifrado
texto_descifrado = descifrar_texto(texto_cifrado, sustitucion)
print("Texto descifrado:\n", texto_descifrado)

# Mostrar el gráfico con las frecuencias
mostrar_grafico(frecuencias_letras)