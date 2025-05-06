"""Pide la cantidad N de numeros
solicita cada numero"""
cant_num = int(input("Dime una cantidad de numeros: "))
mayor = 0
menor = 0
for i in range(cant_num):
    num = float(input(f"Ingrese el numero {i+1} "))
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num
print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}")