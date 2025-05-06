"""Pide una lista de numeros
calcule la suma de los numeros pares
calcule la suma de los numeros impares"""
lista_num = int(input("Dime un numero: "))
pares = 0
impares = 0
while lista_num != 0 and lista_num != -1:
    if lista_num %2 == 0:
        pares += lista_num
    lista_num = int(input("Dime un numero: "))
print(f"La suma de los pares es: {pares}")
print(f"La suma de los impares es: {impares}")