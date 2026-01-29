# -*- coding: utf-8 -*-
from utils import consola

def ejecutar():
    consola.leer_concepto('[PROBABILIDAD]')
    while True:
        consola.mostrar_encabezado("CÁLCULO DE PROBABILIDADES")
        print("1. Probabilidad Simple")
        print("2. Probabilidad Compuesta (Eventos Independientes)")
        print("3. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            consola.mostrar_encabezado("PROBABILIDAD SIMPLE")
            try:
                favorables = float(input("Ingrese el número de casos favorables: "))
                totales = float(input("Ingrese el número de casos totales: "))
                
                if totales <= 0:
                    print("\nError: El número de casos totales debe ser mayor a 0.")
                elif favorables < 0:
                    print("\nError: Los casos favorables no pueden ser negativos.")
                elif favorables > totales:
                    print("\nError: Los casos favorables no pueden ser mayores que los totales.")
                else:
                    probabilidad = favorable_sobre_total = favorables / totales
                    porcentaje = probabilidad * 100
                    print(f"\nProbabilidad = {favorables} / {totales} = {probabilidad:.4f} ({porcentaje:.2f}%)")
                    consola.guardar_historial("Probabilidad Simple", f"{probabilidad:.4f}")
                    
            except ValueError:
                print("\nError: Ingrese valores numéricos válidos.")
            consola.pausar()
            
        elif opcion == '2':
            consola.mostrar_encabezado("PROBABILIDAD COMPUESTA (Independientes)")
            print("Calcula P(A ∩ B) = P(A) * P(B)\n")
            try:
                p_a = float(input("Ingrese la probabilidad del evento A (0-1): "))
                p_b = float(input("Ingrese la probabilidad del evento B (0-1): "))
                
                if not (0 <= p_a <= 1) or not (0 <= p_b <= 1):
                    print("\nError: Las probabilidades deben estar entre 0 y 1.")
                else:
                    prob_conjunta = p_a * p_b
                    print(f"\nP(A ∩ B) = {p_a} * {p_b} = {prob_conjunta:.4f} ({prob_conjunta*100:.2f}%)")
                    consola.guardar_historial("Probabilidad Compuesta", f"{prob_conjunta:.4f}")
                    
            except ValueError:
                print("\nError: Ingrese valores numéricos válidos.")
            consola.pausar()
            
        elif opcion == '3':
            break
        else:
            print("\nOpción no válida.")
            consola.pausar()

