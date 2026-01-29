# -*- coding: utf-8 -*-
import random
from utils import consola

def ejecutar():
    consola.mostrar_encabezado("QUIZ DE ESTADÍSTICA")
    
    # Banco de preguntas: (Pregunta, [Opciones], Respuesta Correcta (índice 0-2 o letra))
    # Formato opciones: [a, b, c]
    banco = [
        {
            "pregunta": "¿Qué medida de tendencia central es el promedio aritmético?",
            "opciones": ["a) Mediana", "b) Media", "c) Moda"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Cuál medida representa el valor central de datos ordenados?",
            "opciones": ["a) Mediana", "b) Rango", "c) Varianza"],
            "respuesta": "a"
        },
        {
            "pregunta": "En una combinación, ¿importa el orden de los elementos?",
            "opciones": ["a) Sí", "b) No", "c) Depende del caso"],
            "respuesta": "b"
        },
        {
            "pregunta": "En una permutación, ¿importa el orden de los elementos?",
            "opciones": ["a) Sí", "b) No", "c) Solo si son números"],
            "respuesta": "a"
        },
        {
            "pregunta": "¿Cuál es el rango de valores de una probabilidad?",
            "opciones": ["a) 0 a 100", "b) -1 a 1", "c) 0 a 1"],
            "respuesta": "c"
        },
        {
            "pregunta": "¿Cuál es la probabilidad de sacar 7 al lanzar un dado estándar?",
            "opciones": ["a) 1/6", "b) 0", "c) 1/7"],
            "respuesta": "b"
        },
        {
            "pregunta": "Si lanzas una moneda, ¿cuál es el espacio muestral?",
            "opciones": ["a) {1, 2}", "b) {Cara, Cruz}", "c) {Cara}"],
            "respuesta": "b"
        },
        {
            "pregunta": "Para eventos independientes A y B, P(A y B) es:",
            "opciones": ["a) P(A) + P(B)", "b) P(A) * P(B)", "c) P(A) / P(B)"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Qué gráfico es adecuado para frecuencias de datos continuos?",
            "opciones": ["a) Histograma", "b) Diagrama de Pastel", "c) Dispersión"],
            "respuesta": "a"
        },
        {
            "pregunta": "La moda es:",
            "opciones": ["a) El dato mayor", "b) El dato que más se repite", "c) El promedio"],
            "respuesta": "b"
        }
    ]
    
    # Seleccionar 5 preguntas al azar
    seleccion = random.sample(banco, 5)
    puntaje = 0
    total = len(seleccion)
    
    print(f"Responde {total} preguntas seleccionadas aleatoriamente.\n")
    
    for i, item in enumerate(seleccion, 1):
        print(f"Pregunta {i}: {item['pregunta']}")
        for op in item['opciones']:
            print(f"   {op}")
            
        respuesta = input("\nTu respuesta (a, b, c): ").lower().strip()
        
        if respuesta == item['respuesta']:
            print("✅ ¡Correcto!")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La correcta era {item['respuesta']}")
            
        print("-" * 40)
    
    print(f"\n🎯 PUNTAJE FINAL: {puntaje}/{total}")
    if puntaje == total:
        print("¡Excelente! Dominas los conceptos.")
    elif puntaje >= total / 2:
        print("¡Bien hecho! Sigue practicando.")
    else:
        print("Necesitas repasar un poco más.")
    
    consola.pausar()

