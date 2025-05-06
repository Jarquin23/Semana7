palabra = input("Dime una palabra: ")
for i in range (10000000):
    if(palabra.lower()) == "fin":
        break
    else:
        print(f"{palabra.upper()} tiene {len(palabra)} letras")
        palabra = input("Dime una palabra")