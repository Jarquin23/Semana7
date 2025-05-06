"""Simula un cajero automático con un saldo inicial
permite al usuario realizar depósitos y retiros hasta que decida salir"""
saldo = float(input("Ingrese el saldo inicial: "))
while True:
    print("\nOperaciones")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Salir")
    opcion = input("Seleccione una opcion: ")
    if opcion=="1":
        monto = float(input("Ingrese el monto que desee depositar:"))
        saldo += monto
        print(f"Su nuevo saldo es de: {saldo}")
    elif opcion=="2":
        monto = float(input("Ingrese el monto que desee retirar:"))
        if monto>saldo:
            print("Fondos insuficientes")
        else:
            saldo -= monto
            print(f"Su nuevo saldo es de: {saldo}")
    elif opcion=="3":
        print(f"Gracias por usar el cajero. Su saldo final es de {saldo}")
        break
    else:
        print("La opción es inválida, por favor intente de nuevo.")