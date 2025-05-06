numero = int(input("Dime un numero: "))
suma = 0
for i in range(1, numero +1):
    suma += i
    print(f"La suma de los primeros {i} números es: {suma}")