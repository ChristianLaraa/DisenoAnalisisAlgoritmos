import random
print("Programa piedra-papel-tijeras-lagarto-spock")
print("Piedra = 0")
print("Papel = 1")
print("Tijeras = 2")
print("Spock = 3")
print("Lagarto = 4")
nombres = ["Piedra", "Papel", "Tijeras", "Spock", "Lagarto"]

usuario = input("Escriba su elección (0, 1, 2, 3 ó 4): ")
compu = random.choice(['0', '1', '2', '3', '4'])
print("La computadora eligió", nombres[int(compu)])
if usuario == compu:
    print("Empate")
elif (int(usuario)-int(compu))%5 in [2, 4]:
    print('gana la computadora')
else:
    print('usted gana')