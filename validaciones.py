
def contar_puntos(texto_valor):
    contador = 0
    for i in range (len(texto_valor)):
        if texto_valor[i]==".":
            contador+=1
    if contador > 1:
        return True
    else:
        return False
    

def tiene_letras (texto_valor):
    contador = 0
    for i in range (len(texto_valor)):
        if ("a"<= texto_valor[i] <="z") or ("A"<= texto_valor[i] <="Z")  :
            contador+=1
    if contador >= 1:
        return True
    else:
        return False


def validar_porcentaje(texto_valor):

    varios_puntos = contar_puntos(texto_valor)
    hay_letras = tiene_letras(texto_valor)
    if texto_valor == "":
        return ""
    elif varios_puntos:
        return ""
    elif hay_letras:
        return ""
    elif texto_valor [0]=="." or texto_valor [-1]==".":
        return ""
    
    num_cpu = float(texto_valor)
    if num_cpu < 0 or num_cpu > 100:
        return ""
    
    return texto_valor

def validar_total_disco (texto_disco):

    varios_puntos = contar_puntos(texto_disco)
    hay_letras = tiene_letras(texto_disco)
    if texto_disco == "":
        return ""
    elif varios_puntos:
        return ""
    elif hay_letras:
        return ""
    elif texto_disco [0]=="." or texto_disco [-1]==".":
        return ""

    num_disco = float(texto_disco)
    if 16 <= num_disco <= 4000:
        return texto_disco
    
    return ""

def validar_espacio_usado(texto_usado, disco_total_num):

    varios_puntos = contar_puntos(texto_usado)
    hay_letras = tiene_letras(texto_usado)
    
    if texto_usado == "":
        return ""
    elif varios_puntos:
        return ""
    elif hay_letras:
        return ""
    elif texto_usado[0] == "." or texto_usado[-1] == ".":
        return ""
        
    # Convierto a float para la ultima comparacion de rango numerico
    num_usado = float(texto_usado)
    
    # Validamos: no puede ser negativo ni mayor que el espacio total 
    if num_usado < 0 or num_usado > disco_total_num:
        return ""
        
    return texto_usado

def validar_procesos(texto_procesos):
    if texto_procesos == "":
        return ""
        
    permitidos = "0123456789" 
    largo_texto = len(texto_procesos) 
    
    for i in range(largo_texto):
        # Accedemos al carácter actual 
        caracter = texto_procesos[i] 
        
        es_valido = False
        
        # Recorremos los permitidos 
        for j in range(len(permitidos)):
            if caracter == permitidos[j]:
                es_valido = True
                
        if es_valido == False: # si entra en este if significa que el caracter no era numero
            return ""
            
    num_procesos = int(texto_procesos)
    if num_procesos < 1 or num_procesos > 600:
        return ""
        
    return texto_procesos 
