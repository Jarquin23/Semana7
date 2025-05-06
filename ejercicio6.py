"""Pide una frase
cuenta el numero de palabras que contiene"""
frase = input("Escribe una frase: ")
cont_palabras = 0
for palabra in frase.split():
    cont_palabras +=1
print(f"La cantidad de palabras en la frase son {cont_palabras}")