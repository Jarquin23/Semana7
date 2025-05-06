"""Pedir la cantidad de calificaciones
solicitar cada calificacion
calcular promedio"""
n = int(input("¿Cuántas calificaciones desea ingresar?"))
suma = 0
for i in range(n):
    calificacion = float(input(f"Ingrese la calificación {i+1}: "))
    suma += calificacion
if n>0:
    promedio = suma/n
else:
    0
print(f"El promedio equivale a: {promedio}")   