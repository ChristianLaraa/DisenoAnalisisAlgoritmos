import string
import matplotlib.pyplot as plt

def count_letter_frequency(text):
    # Inicializar un diccionario para almacenar la frecuencia de cada letra
    frequency = {letter: 0 for letter in string.ascii_lowercase}

    # Contar la frecuencia de cada letra en el texto
    for char in text.lower():
        if char in frequency:
            frequency[char] += 1

    return frequency


def plot_top_letters(frequency, top_n=10):
    # Ordenar el diccionario de frecuencias por valor en orden descendente
    sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

    # Obtener las top N letras y sus frecuencias
    top_letters = sorted_frequency[:top_n]

    # Separar las letras y sus frecuencias para graficar
    letters, counts = zip(*top_letters)

    # Crear un gráfico de barras
    plt.bar(letters, counts)
    plt.xlabel('Letras')
    plt.ylabel('Frecuencia')
    plt.title(f'Letras Más Frecuentes')
    plt.show()


file_path = 'textocidradouno.txt'
with open(file_path, 'r') as file:
    text = file.read()

letter_frequency = count_letter_frequency(text)

most_frequent_letter = max(letter_frequency, key=letter_frequency.get)
print(f'La letra más frecuente es: {most_frequent_letter}')

plot_top_letters(letter_frequency, top_n=10)