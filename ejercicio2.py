num = int(input("Dime un número"))
producto = 1
contador = 0
i = 0
while contador < num:
    i += 4
    contador += 1
    producto *= 1
    print(f"El producto de los {num} numeros pares es {producto}")