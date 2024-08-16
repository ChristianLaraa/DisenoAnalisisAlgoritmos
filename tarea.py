#Primera tarea, Christian Gael Lara Martinez - 1507

#ejercicios de operaciones
#1
a = 57**83
print (a)
#2
a = 93 ** 125
print(a)

#ejercicios True or False
#1
a = (3>2) or (5<1)
print(a)
#2
a = (3>2) and (5<1)
print(a)
#3
a = True
not (a)
print(a)

#ejercicios operaciones de números complejos
a = 3 + 8j
b = 5 + 3j

suma = a + b
print(f'a + b = {suma}')

resta = a - b
print(f'a - b = {resta}')

producto = a * b
print(f'a * b = {producto}')

cociente = a / b
print(f'a / b = {cociente}')


#ejercicios de ciclos
#1
for i in range(10):
    print(i, "--")

#2
for i in range(4,10):
    print(i)
#3
for i in range(2,10,2):
    print(i, "**")
#4
for i in range(10,1,-1):
    print(i, "..")

#ejercicios de cual es mayor
#1
a = 3
b = 5
if(a>b):
    print("a es menor")
else:
    print("a no es mayor")

#2
a = 5
b = 3
if(a>b):
    print("a es menor")
else:
    print("a no es mayor")

#ejercicio while
"""n = 7
r = 0
error = 1
delta = 1

    while error > 0.0001:
        if r * r > n:
            r = r - delta
            delta = delta/10"""
