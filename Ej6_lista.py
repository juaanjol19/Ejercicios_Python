#

# Ejercicio 6: Obtener un conjunto de numeros separados por coma y crear una lista

entrada = input("Escriba numeros separados por coma: ")
print(entrada)
print(type(entrada))
print(60*'*')
lista = entrada.split()
print(lista)
print(type(lista))
print(60*'*')
lista2 = entrada.split(',')
print(lista2)
print(type(lista2))

