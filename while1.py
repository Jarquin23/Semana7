"""Leer una palabra diferente a fin y convertirla a mayúscula"""
palabra = input("Dime una palabra: ")
while palabra.lower() != "fin":
    print(f"{palabra.upper()} tiene {len(palabra)} letras")
    palabra = input("Dime la palabra")
else:
    print("Adiós...")