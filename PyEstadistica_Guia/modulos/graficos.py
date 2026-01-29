# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
from utils import consola

def ejecutar():
    consola.mostrar_encabezado("GRÁFICOS ESTADÍSTICOS")
    
    print("Seleccione la fuente de datos:")
    print("1. Generar datos aleatorios")
    print("2. Cargar desde archivo (recursos/datos.csv)")
    
    fuente = input("\nOpción: ")
    datos = []
    
    if fuente == '2':
        datos = consola.cargar_datos_csv("recursos/datos.csv")
        if not datos:
            print("No se pudieron cargar datos. Usando aleatorios por defecto.")
            datos = [random.randint(5, 10) for _ in range(50)]
    else:
        print("Generando 50 calificaciones aleatorias entre 5 y 10...")
        # Generar 50 calificaciones aleatorias entre 5 y 10 (enteros para simplificar histograma)
        datos = [random.randint(5, 10) for _ in range(50)]
    
    print(f"\nDatos a graficar: {datos}")
    
    print("\nINTERPRETACIÓN:")
    print("El gráfico muestra la frecuencia de las notas obtenidas por 50 estudiantes simulados.")
    print("El eje X representa la calificación (5-10) y el eje Y la cantidad de estudiantes.")
    print("\nSe abrirá una ventana con el gráfico. Ciérrela para continuar.")
    
    # Crear el histograma
    plt.figure(figsize=(10, 6))
    plt.hist(datos, bins=range(5, 12), align='left', rwidth=0.8, color='skyblue', edgecolor='black')
    plt.title('Distribución de Calificaciones de 50 Estudiantes')
    plt.xlabel('Calificación')
    plt.ylabel('Frecuencia (Cantidad de Estudiantes)')
    plt.xticks(range(5, 11))
    plt.grid(axis='y', alpha=0.75)
    
    # Mostrar el gráfico
    plt.show()
    
    consola.pausar()

