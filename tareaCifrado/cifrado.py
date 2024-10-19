import matplotlib.pyplot as plt

# Frecuencia más común en palabras en inglés
frecuencia_ingles = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']

def load_words():
    try:
        with open('words.txt', 'r') as archivo:
            palabras = archivo.read().split()
        print(len(palabras), 'palabras leídas')
        return set(palabras)
    except FileNotFoundError:
        print("Error: El archivo 'words.txt' no se encuentra.")
        return set()

def load_encrypted_text():
    try:
        with open('Lara.txt', 'r') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print("Error: El archivo 'Lara.txt' no se encuentra.")
        return ""

def get_correct_words_count(words_list, dictionary):
    num_correct = sum(1 for word in words_list if word.upper() in dictionary)
    return num_correct

def verify_words(decrypted_text, dictionary):
    words = decrypted_text.split()
    num_correct = get_correct_words_count(words, dictionary)
    return num_correct, len(words)

def calculate_frequency(text):
    frequencies = {}
    total_letters = 0
    for letter in text:
        if letter.isalpha():
            letter = letter.upper()
            total_letters += 1
            frequencies[letter] = frequencies.get(letter, 0) + 1

    # Ordenar frecuencias de mayor a menor
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    return sorted_frequencies, total_letters

def plot_frequency(frequency_list):
    letters = [item[0] for item in frequency_list]
    frequencies = [item[1] for item in frequency_list]
    plt.figure(figsize=(10, 6))
    plt.bar(letters, frequencies, color='skyblue')
    plt.xlabel('Letras')
    plt.ylabel('Frecuencia')
    plt.title('Frecuencia de las letras en el texto')
    plt.show()  # Descomentado para mostrar el gráfico

sustitucion = {
    'd': 'e',
    'l': 't',
    'g': 'a',
    'c': 'o',
    'y': 'n',
    't': 'h',
    'a': 'i',
    'j': 's',
    'f': 'l',
    'p': 'r',
    'x': 'f',
    'o': 'd',
    'q': 'w',
    'm': 'm',
    's': 'c',
    'n': 'y',
    'h': 'g',
    'v': 'u',
    'k': 'k',
    'z': 'b',
    'r': 'p',
    'w': 'v',
    'e': 'x'
}

def decrypt_text(text, substitution):
    decrypted_text = ""
    for letter in text:
        if letter in substitution:
            decrypted_text += substitution[letter].lower()
        else:
            decrypted_text += letter.lower() if letter.isalpha() else letter

    return decrypted_text

dictionary_words = load_words()
encrypted_text = load_encrypted_text()

frequencies_letters, total = calculate_frequency(encrypted_text)

decrypted_text = decrypt_text(encrypted_text, sustitucion)
print("Texto descifrado:", decrypted_text)

plot_frequency(frequencies_letters)
