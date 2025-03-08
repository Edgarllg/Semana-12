# Matriz 3D: [Ciudad][Semana][Día]
ciudades = ["Ambato", "Guayaquil", "Quito", "Cuenca", "Macas"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Matriz tridimensional (3D) con temperaturas [5 ciudades][3 semanas][7 días]
temperaturas = [
    # Ambato
    [
        [14, 18, 22, 17, 19, 23, 20],  # Semana 1
        [15, 19, 21, 18, 20, 24, 22],  # Semana 2
        [16, 20, 23, 19, 21, 25, 23]   # Semana 3
    ],
    # Guayaquil
    [
        [28, 28, 28, 28, 28, 29, 30],
        [27, 28, 28, 29, 30, 30, 31],
        [26, 27, 28, 28, 29, 30, 31]
    ],
    # Quito
    [
        [12, 14, 15, 13, 16, 18, 19],
        [13, 15, 16, 14, 17, 19, 20],
        [14, 16, 17, 15, 18, 20, 21]
    ],
    # Cuenca
    [
        [10, 12, 14, 13, 15, 17, 18],
        [11, 13, 15, 14, 16, 18, 19],
        [12, 14, 16, 15, 17, 19, 20]
    ],
    # Macas
    [
        [22, 23, 24, 23, 24, 25, 26],
        [21, 22, 23, 22, 23, 24, 25],
        [20, 21, 22, 21, 22, 23, 24]
    ]
]

# 🔹 Iterar sobre la matriz 3D
for i, ciudad in enumerate(ciudades):
    print(f"\n Ciudad: {ciudad}")
    
    total_temperaturas = 0  
    total_dias = 0  
    
    for j, semana in enumerate(temperaturas[i]):
        print(f"   Semana {j + 1}:")
        
        suma_semana = sum(semana)
        for k, temp in enumerate(semana):
            print(f"    {dias_semana[k]}: {temp}°C")

        promedio_semana = suma_semana / len(semana)
        print(f"     Promedio semanal: {promedio_semana:.2f}°C")

        total_temperaturas += suma_semana
        total_dias += len(semana)

    #  Promedio total por ciudad
    promedio_ciudad = total_temperaturas / total_dias
    print(f"   Promedio total en {ciudad}: {promedio_ciudad:.2f}°C")