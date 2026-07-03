import json

ARCHIVO = "parametros.json"

def leer_json():
    
    with open(ARCHIVO, "r", encoding="utf-8") as file:
        parametro = json.load(file)

        return parametro

def modificar_json(parametro):

    with open(ARCHIVO, "w", encoding="utf-8") as file:
        json.dump(parametro, file, indent=4, ensure_ascii=False)

        return parametro
