# Definir una matriz 3D para temperaturas [ciudades][días de la semana][semanas]
import random

ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Generar datos aleatorios de temperatura entre 10 y 35 grados
temperaturas = [[[random.randint(10, 35) for _ in range(len(dias_semana))] for _ in range(semanas)] for _ in range(len(ciudades))]

# Mostrar la matriz de temperaturas
print("\nTemperaturas registradas:")
for i, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")
    for semana in range(semanas):
        print(f"  Semana {semana + 1}: {temperaturas[i][semana]}")

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
print("\nPromedio de temperaturas por ciudad y semana:")
for i, ciudad in enumerate(ciudades):
    for semana in range(semanas):
        promedio = sum(temperaturas[i][semana]) / len(dias_semana)
        print(f"  {ciudad}, Semana {semana + 1}: {promedio:.2f}°C")