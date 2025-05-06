"""Pide un numero
calcula cuantas veces aparece cada digito en el numero"""
num = input("Ingresa un numero: ")
frec = [0] * 10
i = 0
while i < len(num):
    if num[i].isdigit():
        digito = int(num[i])
        frec[digito] +=1
    i +=1
for d in range(10):
    print(f"Digito{d}: {frec[d]} veces")