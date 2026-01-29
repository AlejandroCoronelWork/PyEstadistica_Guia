# -*- coding: utf-8 -*-
"""
Proyecto de Probabilidad y Estadística.
Integrantes: Alejandro Coronel y Josué Morales.
"""

from utils import consola
from modulos import basicos, conteo, experimentos, probabilidad, ejercicios, graficos

def menu_principal():
    while True:
        consola.limpiar_pantalla()
        print("=" * 60)
        print(f"{'PROYECTO DE PROBABILIDAD Y ESTADÍSTICA':^60}")
        print("=" * 60)
        print(f"{'Integrantes: Alejandro Coronel y Josué Morales':^60}")
        print("=" * 60)
        print("\nMENÚ PRINCIPAL:")
        print("1. Estadística Descriptiva (Media, Mediana, Moda)")
        print("2. Técnicas de Conteo (Combinaciones, Permutaciones)")
        print("3. Experimentos Aleatorios (Moneda, Dado)")
        print("4. Probabilidad (Simple, Compuesta)")
        print("5. Ejercicios (Quiz)")
        print("6. Gráficos (Histograma de Notas)")
        print("7. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            basicos.ejecutar()
        elif opcion == '2':
            conteo.ejecutar()
        elif opcion == '3':
            experimentos.ejecutar()
        elif opcion == '4':
            probabilidad.ejecutar()
        elif opcion == '5':
            ejercicios.ejecutar()
        elif opcion == '6':
            graficos.ejecutar()
        elif opcion == '7':
            print("\n¡Gracias por usar PyEstadistica_Guia! Hasta luego.")
            break
        else:
            print("\nOpción no válida.")
            consola.pausar()

def main():
    menu_principal()

if __name__ == "__main__":
    main()
