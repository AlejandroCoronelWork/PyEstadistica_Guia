# -*- coding: utf-8 -*-
import statistics
from utils import consola

def ejecutar():
    consola.mostrar_encabezado("ESTADÍSTICA DESCRIPTIVA: Media, Mediana, Moda")
    
    consola.leer_concepto("[MEDIA]")
    
    print("Ingrese una lista de números separados por espacios.")
    entrada = input("Números: ")
    
    try:
        # Convertir la entrada a una lista de flotantes
        datos = [float(x) for x in entrada.split()]
        
        if not datos:
            print("\nError: No ingresó ningún número.")
        else:
            media = statistics.mean(datos)
            mediana = statistics.median(datos)
            
            print(f"\nResultados:")
            print(f"- Media: {media:.2f}")
            print(f"- Mediana: {mediana:.2f}")
            
            # Guardamos la Tendencia Central (Media)
            consola.guardar_historial("Tendencia Central", f"Media={media:.2f}")
            
            try:
                moda = statistics.mode(datos)
                print(f"- Moda: {moda:.2f}")
            except statistics.StatisticsError:
                print("- Moda: No hay una única moda (multimodal o sin moda).")
                
    except ValueError:
        print("\nError: Asegúrese de ingresar solo números separados por espacios.")
    
    consola.pausar()

