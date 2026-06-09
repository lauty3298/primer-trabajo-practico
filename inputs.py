import validaciones

def es_todo_espacios (texto): #Se agregó docstrings
    """
    Verifica si una cadena está vacía o compuesta únicamente por espacios en blanco.

    Args:
        texto (str): La cadena a evaluar.

    Returns:
        bool: True si está vacía o son solo espacios, False si contiene caracteres válidos.
    """
    # Si el usuario solo apretó Enter, el largo es 0
    if len(texto) == 0:
        return True
        
    # Recorremos cada letra/carácter del texto
    for caracter in texto:
        if caracter != " ":
            return False  # Encontró algo que no es espacio, entonces es valido
            
    return True  # Si recorrió todo y no entró al if, son todos espacios

def ingreso_nombre_servidor(): 
    """
    Solicita y valida el nombre del servidor asegurando que tenga más de 5 caracteres
    y no esté compuesto solo de espacios.

    Returns:
        str: El nombre del servidor validado.
    """
    nombre_invalido = True
    while nombre_invalido:
        nombre = input("Ingrese nombre del servidor: ")
        
        # 1. Validamos vacío o todo espacios usando nuestra función
        if es_todo_espacios(nombre):
            print("Error: El nombre del servidor no puede estar vacío ni contener solo espacios.")
            continue
            
        # 2. Validamos el largo mínimo 
        if len(nombre) <= 5:
            print("Error: El nombre debe tener mas de 5 caracteres.")
            continue
            
        # Si pasó ambos filtros, rompemos el bucle
        nombre_invalido = False

    print(f"Servidor registrado con éxito: {nombre}\n")    
    return nombre

def ingreso_nombre_admin_servidor():
    """
    Solicita y valida el nombre del administrador asegurando que tenga más de 5 caracteres
    y no esté compuesto solo de espacios.

    Returns:
        str: El nombre del administrador validado.
    """
    nombre_invalido = True
    while nombre_invalido:
        nombre = input("Ingrese nombre del administrador del servidor: ")
        
        # 1. Validamos vacío o todo espacios usando nuestra función
        if es_todo_espacios(nombre):
            print("Error: El nombre del administrador no puede estar vacío ni contener solo espacios.")
            continue
            
        # 2. Validamos el largo mínimo 
        if len(nombre) <= 5:
            print("Error: El nombre debe tener mas de 5 caracteres.")
            continue
            
        # Si pasó ambos filtros, rompemos el bucle
        nombre_invalido = False

    print(f"Nombre registrado con éxito: {nombre}\n")    
    return nombre



# def validar_sistema_operativo():
#     """
#     Solicita y valida que el sistema operativo ingresado pertenezca a la lista de permitidos.
# 
#     Returns:
#         str: El nombre del sistema operativo validado.
#     """    
#     so_validos = ["Linux", "Windows"]
#     no_valido = True
#     while no_valido:
#         so_ingresado = input("Ingrese Sistema Operativo (Linux / Windows): ")
#         encontrado = False
#         
#         # Recorremos la lista para buscar si es valido
#         for i in range(len(so_validos)):
#             if so_ingresado == so_validos[i]:
#                 encontrado = True
#                 break  # Sale del bucle for porque ya lo encontró
#                 
#         # Si la bandera quedó en False, el dato es inválido
#         if encontrado == False:
#             print("Error: El sistema operativo ingresado no es válido.")
#             continue  # Vuelve al inicio del while a pedir el dato otra vez
#         else:
#             no_valido = False
# 
#     return so_ingresado  # Cuando sale del while, devuelve el SO válido


#linea de adrian
def validar_sistema_operativo():
    """
    Solicita y valida que el sistema operativo ingresado pertenezca a la lista de permitidos,
    aceptando tanto mayúsculas como minúsculas.

    Returns:
        str: El nombre del sistema operativo estandarizado ("Linux" o "Windows").
    """
    # Agregamos las variaciones en minúscula a la lista de opciones válidas
    so_validos = ["Linux", "linux", "Windows", "windows"]
    no_valido = True
    
    while no_valido:
        so_ingresado = input("Ingrese Sistema Operativo (Linux / Windows): ")
        encontrado = False
        
        # Recorremos la lista para buscar si es valido
        for i in range(len(so_validos)):
            if so_ingresado == so_validos[i]:
                encontrado = True
                
                # Estandarizamos el texto para que el resto del programa siempre reciba mayúscula inicial
                if so_ingresado == "linux":
                    so_ingresado = "Linux"
                elif so_ingresado == "windows":
                    so_ingresado = "Windows"
                    
                break  # Sale del bucle for porque ya lo encontró
                
        # Si la bandera quedó en False, el dato es inválido
        if encontrado == False:
            print("Error: El sistema operativo ingresado no es válido.")
            continue  # Vuelve al inicio del while a pedir el dato otra vez
        else:
            no_valido = False

    return so_ingresado  # Devuelve el SO válido y estandarizado


# def validar_ubicacion_servidor():
#     
#     ubicacion_validos = ["Argentina", "Uruguay","Chile"]
#     no_valido = True
#     while no_valido:
#         ubi_ingresado = input("Ingrese la ubicacion del Servidor (Argentica / Uruguay / Chile): ")
#         encontrado = False
#         
#         # Recorremos la lista para buscar si es valido
#         for i in range(len(ubicacion_validos)):
#             if ubi_ingresado == ubicacion_validos[i]:
#                 encontrado = True
#                 break  # Sale del bucle for porque ya lo encontró
#                 
#         # Si la bandera quedó en False, el dato es inválido
#         if encontrado == False:
#             print("Error: La ubicacion ingresada no es válida.")
#             continue  # Vuelve al inicio del while a pedir el dato otra vez
#         else:
#             no_valido = False
# 
#     return ubi_ingresado  # Cuando sale del while, devuelve el SO válido

#linea de adrian
def validar_ubicacion_servidor():
    """
    Solicita y valida que la ubicación ingresada pertenezca a la lista de países permitidos.

    Returns:
        str: El país validado.
    """
    # Agrege las opciones en minúscula y mayúscula para atajar el error del usuario
    ubicacion_validos = ["Argentina", "argentina", "Uruguay", "uruguay", "Chile", "chile"]
    no_valido = True
    
    while no_valido:
        ubi_ingresado = input("Ingrese la ubicacion del Servidor (Argentina / Uruguay / Chile): ")
        encontrado = False
        
        for i in range(len(ubicacion_validos)):
            if ubi_ingresado == ubicacion_validos[i]:
                encontrado = True
                # Para que el reporte quede prolijo, forzamos a que devuelva la versión con mayúscula inicial
                if ubi_ingresado == "argentina": ubi_ingresado = "Argentina"
                elif ubi_ingresado == "uruguay": ubi_ingresado = "Uruguay"
                elif ubi_ingresado == "chile": ubi_ingresado = "Chile"
                break 
                
        if encontrado == False:
            print("Error: La ubicacion ingresada no es válida.")
            continue 
        else:
            no_valido = False

    return ubi_ingresado



def validar_firewall():
    """
    Solicita el estado del firewall por menú (1 o 2) o texto y estandariza su valor.

    Returns:
        str: El estado del firewall ("Activo" o "Desactivado").
    """
    firewall_invalido = True

    while firewall_invalido:
 
        firewall = input("Ingrese el estado del firewall (1. Activo / 2.Desactivado): ")

        match firewall:
            case "Activo" | "activo" | "1":
                firewall = "Activo"
                firewall_invalido = False
            case "Desactivado" | "desactivado" | "2":
                firewall = "Desactivado"
                firewall_invalido = False
            case _:
                print("Opción no válida")
    return firewall            


def ingreso_porcentaje_cpu():
    """
    Solicita y valida el porcentaje de uso de la CPU iterando hasta obtener un dato correcto.

    Returns:
        float: El porcentaje de CPU validado como número decimal.
    """    
 #   cpu = (input("ingrese el porcentaje de uso de la cpu: "))
    cpu = (input("ingrese el porcentaje de uso de la cpu (0 a 100): "))
    valor_porcentaje_cpu=validaciones.validar_porcentaje(cpu)
    
    while valor_porcentaje_cpu == "":
        print("Error: Ingrese un porcentaje válido (0 a 100).")
        cpu = (input("ingrese el porcentaje de uso de la cpu: "))
        valor_porcentaje_cpu=validaciones.validar_porcentaje(cpu)

    porcentaje_cpu = float (cpu)
    return porcentaje_cpu

def ingreso_porcentaje_ram():
    """
    Solicita y valida el porcentaje de uso de la RAM iterando hasta obtener un dato correcto.

    Returns:
        float: El porcentaje de RAM validado como número decimal.
    """        
    ram = (input("ingrese el porcentaje de uso de la ram (0 a 100): "))
    valor_porcentaje_ram=validaciones.validar_porcentaje(ram)

    while valor_porcentaje_ram == "":
        print("Error: Ingrese un porcentaje válido (0 a 100).")
        ram = (input("ingrese el porcentaje de uso de la ram: "))
        valor_porcentaje_ram=validaciones.validar_porcentaje(ram)

    porcentaje_ram = float (ram)
    return porcentaje_ram

def ingreso_espacio_total_disco():
    """
    Solicita y valida la capacidad total del disco iterando hasta obtener un dato dentro del rango.

    Returns:
        float: La capacidad del disco validada en GB.
    """
    texto_disco = (input("ingrese el espacio total del disco (De 16 Gb hasta 4000 Gb): "))
    ingreso_valor_disco = validaciones.validar_total_disco(texto_disco)
    
    while ingreso_valor_disco == "":
        print("Error: Ingreso un espacio de disco invalido : ")
        texto_disco = (input("ingrese el espacio total del disco (De 16 Gb hasta 4000 Gb): "))
        ingreso_valor_disco = validaciones.validar_total_disco(texto_disco)

    almacenamiento_disco = float (texto_disco)
    return almacenamiento_disco

def ingreso_espacio_utilizado_disco(almacenamiento_disco:float):
    """
    Solicita y valida el espacio ocupado del disco, asegurando que no supere la capacidad total.

    Args:
        almacenamiento_disco (float): La capacidad máxima del disco.

    Returns:
        float: El espacio utilizado validado en GB.
    """
    texto_disco = (input("ingrese el espacio utilizado del disco (0 hasta capacidad maxima del disco): "))
    ingreso_valor_disco = validaciones.validar_espacio_usado(texto_disco,almacenamiento_disco)
    
    while ingreso_valor_disco == "":
        print("Error: Ingresó un valor de espacio utlizado en disco invalido. ")
        texto_disco = input("ingrese el espacio utilizado del disco (0 hasta capacidad maxima del disco): ") 
        ingreso_valor_disco = validaciones.validar_espacio_usado(texto_disco,almacenamiento_disco)

    espacio_utilizado_disco = float (texto_disco)
    return espacio_utilizado_disco


def ingreso_procesos_activos():
    """
    Solicita y valida la cantidad de procesos activos iterando hasta obtener un número entero dentro del rango.

    Returns:
        int: La cantidad de procesos validados.
    """
    procesos = input("Ingrese la cantidad de procesos activos: ")
    valor_procesos = validaciones.validar_procesos(procesos)
    
    while valor_procesos == "":
        print("Error: Ingrese una cantidad válida de procesos enteros (1 a 600): ")
        procesos = input("Ingrese la cantidad de procesos activos: ")
        valor_procesos = validaciones.validar_procesos(procesos)
        
    return int(procesos)

