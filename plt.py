import matplotlib.pyplot as plt

histo1 = {}
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
for c in alfabeto:
    histo1[c] = 0
print(histo1)

cad = "Esta es una prueba de texto en la clase"\
    "diseño y analisis de algoritmos, es importate"\
    "ya que se importan librerias de la clase"\
    "es un codigo corto pero que demuestran los algoritmos"
print(cad)
for c in cad:
    if c in alfabeto:
        histo1[c]+=1
print(histo1)
plt.plot(histo1.values())
plt.show()