import json
import os

ARCHIVO = "parametros.json"

def leer_json():
    """
    Lee y carga el archivo de configuración JSON del sistema.

    Verifica si el archivo existe en el disco. Si se encuentra, procesa su 
    contenido y lo transforma en un diccionario de Python. Si el archivo 
    no existe, evita que el programa se rompa devolviendo un diccionario vacío.

    Returns:
        dict: Un diccionario con los parámetros del servidor si el archivo existe,
              o un diccionario vacío `{}` si no se encuentra.
    """    
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as file:
            parametro = json.load(file)

            return parametro
    return {}

def modificar_json(parametro):
    """
    Guarda y actualiza los parámetros en el archivo JSON.

    Toma un diccionario de Python con las configuraciones modificadas y las
    escribe de forma persistente en el archivo físico del disco, aplicando un 
    formato ordenado y legible (indentación de 4 espacios) y asegurando el soporte 
    para caracteres especiales.

    Args:
        parametro (dict): El diccionario de Python actualizado que se desea guardar.

    Returns:
        dict: El mismo diccionario que fue recibido y guardado en el archivo.
    """
    with open(ARCHIVO, "w", encoding="utf-8") as file:
        json.dump(parametro, file, indent=4, ensure_ascii=False)

        return parametro
