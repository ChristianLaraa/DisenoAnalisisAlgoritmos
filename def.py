def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(es_par(2))


#Par o no
def es_paar(num):
    return (num % 2) == 0
print(es_paar(2))

# Palindrome 1
def es_palindrome (palabra):
    for i in palabra:
        if palabra == palabra[::-1]:
            return True
        else:
            return False
print(es_palindrome("reconocer"))

#Palindorme 2
def es_palindrome2(palabra):
    temp = ''
    for i in range (len(palabra)):
        temp += palabra[-(i+1)]
    if temp == palabra:
        return True
    else:
        return False
print(es_palindrome2("saul"))

#Palindorme 3
def es_palindrome3(palabra):
    if len(palabra) == 0 or len(palabra) == 1:
        return True
    else:
        return palabra[0] == palabra[-1] and es_palindrome3(palabra[1:-1])
    return False
print(es_palindrome3("radar"))

# Factorial
def factorial(num):
    resultado = 1
    for n in range (num):
        resultado *= n+1
    return resultado
print(factorial(5))
