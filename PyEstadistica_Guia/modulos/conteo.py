# -*- coding: utf-8 -*-
import math
from utils import consola

def ejecutar():
    consola.mostrar_encabezado("TÉCNICAS DE CONTEO: Combinaciones y Permutaciones")
    
    consola.leer_concepto("[COMBINACIONES]")
    consola.leer_concepto("[PERMUTACIONES]")
    
    print("Este módulo calcula formas de seleccionar r elementos de un conjunto de n elementos.\n")
    
    try:
        n = int(input("Ingrese el número total de elementos (n): "))
        r = int(input("Ingrese el número de elementos a seleccionar (r): "))
        
        if n < 0 or r < 0:
            print("\nError: Los números deben ser no negativos.")
        elif r > n:
            print("\nError: r no puede ser mayor que n.")
        else:
            combinaciones = math.comb(n, r)
            permutaciones = math.perm(n, r)
            
            print(f"\nResultados para n={n}, r={r}:")
            print("-" * 30)
            print(f"Combinaciones: {combinaciones}")
            print("  (El orden NO importa. Ej: seleccionar frutas para una ensalada)")
            print("-" * 30)
            print(f"Permutaciones: {permutaciones}")
            print("  (El orden SÍ importa. Ej: asignar puestos de una directiva)")
            print("-" * 30)
            
            consola.guardar_historial("Combinatoria", f"C={combinaciones} P={permutaciones}")
            
    except ValueError:
        print("\nError: Debe ingresar números enteros válidos.")
    
    consola.pausar()

