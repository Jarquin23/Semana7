"""Pide al usuario un numero entero positivo
calcular su factorial"""
num = int(input("Dame un número: "))
factorial = 1
contador = 1
while contador <= num:
    factorial *= contador
    contador += 1
print(f"El factorial de {num} es {factorial}")