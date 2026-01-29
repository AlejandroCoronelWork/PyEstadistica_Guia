# -*- coding: utf-8 -*-
import os
import textwrap

def limpiar_pantalla():
    """Limpia la pantalla de la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input("\nPresione Enter para continuar...")

def mostrar_encabezado(titulo):
    """Limpia la pantalla y muestra un título decorado."""
    limpiar_pantalla()
    # Calcular ancho dinámico (mínimo 40, o largo del título + 4 padding)
    ancho = max(40, len(titulo) + 4)
    print("=" * ancho)
    print(f"{titulo:^{ancho}}")
    print("=" * ancho)
    print()

def obtener_ruta_recurso(nombre_archivo):
    """Obtiene la ruta absoluta de un recurso."""
    # Ruta base = directorio padre de 'utils' (carpeta del proyecto)
    ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ruta_base, "recursos", nombre_archivo)

def leer_concepto(tag):
    """
    Busca una etiqueta en recursos/conceptos.txt y muestra el contenido en una tarjeta ASCII.
    """
    limpiar_pantalla()
    ruta_archivo = obtener_ruta_recurso("conceptos.txt")
    
    # Diccionario de Emojis
    key_limpia = tag.replace("[", "").replace("]", "")
    emojis = {
        "MEDIA": "📊", "MEDIANA": "📊", "MODA": "📊",
        "COMBINACIONES": "🔢", "PERMUTACIONES": "🔢",
        "EXPERIMENTO": "🎲", "PROBABILIDAD": "🎲"
    }
    
    # Seleccionar emoji por coincidencia parcial
    emoji = "📘"
    for k, v in emojis.items():
        if k in key_limpia:
            emoji = v
            break
            
    contenido_encontrado = ""
    
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            texto_completo = archivo.read()
            
        # Parsing manual usando split
        bloques = texto_completo.split('[')
        for bloque in bloques:
            if ']' in bloque:
                header, body = bloque.split(']', 1)
                if header.strip() == key_limpia:
                    contenido_encontrado = body.strip()
                    break
                        
        if contenido_encontrado:
            # Renderizado de Tarjeta ASCII
            ancho = 60
            borde_h = "═" * ancho
            titulo = f" {emoji} CONCEPTOS: {key_limpia} "
            
            print(f"╔{borde_h}╗")
            # Restamos 1 al ancho porque el emoji ocupa 2 espacios visuales pero len() cuenta 1
            print(f"║{titulo:^{ancho-1}}║")
            print(f"╠{borde_h}╣")
            
            lineas = contenido_encontrado.split('\n')
            for linea in lineas:
                linea = linea.strip()
                if not linea:
                    # Línea vacía: relleno total
                    print(f"║{' ' * ancho}║")
                    continue
                    
                # Ajuste de texto para que quepa en la tarjeta
                # ancho-4 deja margen de 2 espacios a cada lado (aprox) para legibilidad
                texto_envuelto = textwrap.wrap(linea, width=ancho-4)
                for linea_envuelta in texto_envuelto:
                    # Estrategia: Imprimir borde izq, espacio, texto, relleno calculado, espacio, borde der
                    # Total ancho deseado entre bordes = ancho (60)
                    # Contenido actual = " " + linea_envuelta + " "
                    # Longitud actual = 1 + len(linea_envuelta) + 1 = len + 2
                    # Relleno necesario = ancho - (len + 2)
                    
                    espacios_relleno = ancho - 2 - len(linea_envuelta)
                    espacios_relleno = max(0, espacios_relleno)
                    print(f"║ {linea_envuelta}{' ' * espacios_relleno} ║")
            
            print(f"╚{borde_h}╝")
            print()
            
    except FileNotFoundError:
        print(f"\n[Advertencia] No se encontró el archivo de conceptos: {ruta_archivo}")

def cargar_datos_csv(ruta):
    """
    Carga datos numéricos desde un archivo CSV.
    """
    # Si la ruta es relativa, la hacemos absoluta respecto a la raíz del proyecto
    if not os.path.isabs(ruta):
        ruta = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ruta)
    
    datos = []
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            linea = archivo.readline()
            if linea:
                # Asumiendo una sola columna o valores separados por comas
                partes = linea.split(',')
                for parte in partes:
                    try:
                        datos.append(float(parte.strip()))
                    except ValueError:
                        continue
        print(f"\nDatos cargados correctamente desde {ruta}")
    except FileNotFoundError:
        print(f"\nError: No se encontró el archivo {ruta}")
    return datos

def guardar_historial(operacion, resultado):
    """
    Guarda una operación y su resultado en recursos/historial.csv.
    """
    ruta_historial = obtener_ruta_recurso("historial.csv")
    try:
        with open(ruta_historial, 'a', encoding='utf-8') as archivo:
            archivo.write(f"{operacion},{resultado}\n")
        print(f" [Historial actualizado]")
    except Exception as e:
        print(f" [Error al guardar historial: {e}]")

