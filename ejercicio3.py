"""Pide al usuario una cadena
cuenta cuantas vocales tiene"""
cad = input("Ingrsa una cadena de texto: ")
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0
for caracter in cad.lower():
    if caracter =="a":
        contador_a += 1
    elif caracter =="e":
        contador_e += 1
    elif caracter =="i":
        contador_i += 1
    elif caracter =="o":
        contador_o += 1
    elif caracter =="u":
        contador_u += 1
print("Cantidad de vocales: ")
print(f"a {contador_a}")
print(f"e, {contador_e}")
print(f"i, {contador_i}")
print(f"o, {contador_o}")
print(f"u, {contador_u}")