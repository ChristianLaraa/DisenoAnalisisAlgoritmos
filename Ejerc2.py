#Christian Gael Lara Martinez
#270824
print('------------------------------------------------------------------')
print('Clase 27/08/24')
import random
n = 24500
list = []
while len(list) < n:
    ale = random.randint(1, n)
    if ale not in list:
        list.append(ale)

print(list)
inicio = time.time()

for j in range(n):
    for i in range(n - 1):
        if (list[i] > list[i + 1]):
            temporal = list[i]
            list[i] = list[i + 1]
            list[i + 1] = temporal
print(list)
fin = time.time()
print(fin - inicio)
a = [1,2,3,4]
print(len(a))

a.append(0)
print(a)