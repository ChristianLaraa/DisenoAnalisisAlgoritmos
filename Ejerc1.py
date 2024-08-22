#Christian Gael Lara Martinez
#22/08/24
a = "hola"
print(a)


b = 'hola'
print(b)

d = "alan"
print(len(d))
print(d[0])

e = "jkfjnkjfmkldkjdklnd"
print(e[len(e)-1])
#dos versiones
print(e[-1])

m = "marcelo"
print(m[0])
print(m[1])
print(m[2])
print(m[3])
print(m[4])
print(m[5])

m = 'Marcelo'
print(m[0])
for c in range(len(m)):
    print(m[c])
for c in range(3):
    print(m[c])

print(m[1:4])
print(m[:4])
print(m[2:])
print(m[:])
print(m[::2])
print(m[::1])

print("-------------------------------------")

for c in m:
    print(c)

print("LISTAS EN PYTHON +++++++++++++")
#LISTAS EN PYTHON
a = [1,3,4,5,6,7,8]
#todas las listas empiezan en 0
a.append(2)
print(a)
a.sort() #ordena
print(a)

print("-----------------------")
b = [1, 2, "hola", True, 2.43]
print(len(b))
#
c = [1, 2, 3]

b.append(c)

print(len(b))


print(b[-1][2])
