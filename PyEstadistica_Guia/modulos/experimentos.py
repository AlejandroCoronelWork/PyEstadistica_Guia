# -*- coding: utf-8 -*-
import random
from utils import consola

def ejecutar():
    consola.leer_concepto('[EXPERIMENTO]')
    consola.pausar()
    while True:
        consola.mostrar_encabezado("EXPERIMENTOS ALEATORIOS")
        print("1. Lanzar Moneda")
        print("2. Lanzar Dado")
        print("3. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            consola.mostrar_encabezado("LANZAMIENTO DE MONEDA")
            print("Espacio Muestral S = {Cara, Cruz}")
            input("\nPresione Enter para lanzar la moneda...")
            resultado = random.choice(["Cara", "Cruz"])
            print(f"\n¡Ha salido: {resultado}!")
            consola.pausar()
            
        elif opcion == '2':
            consola.mostrar_encabezado("LANZAMIENTO DE DADO")
            print("Espacio Muestral S = {1, 2, 3, 4, 5, 6}")
            input("\nPresione Enter para lanzar el dado...")
            resultado = random.randint(1, 6)
            print(f"\n¡Ha salido: {resultado}!")
            consola.pausar()
            
        elif opcion == '3':
            break
        else:
            print("\nOpción no válida.")
            consola.pausar()

