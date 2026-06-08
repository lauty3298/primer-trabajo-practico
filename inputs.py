import validaciones

def es_todo_espacios(texto):
    # Si el usuario solo apretó Enter, el largo es 0
    if len(texto) == 0:
        return True
        
    # Recorremos cada letra/carácter del texto
    for caracter in texto:
        if caracter != " ":
            return False  # Encontró algo que no es espacio, entonces es valido
            
    return True  # Si recorrió todo y no entró al if, son todos espacios

def ingreso_nombre_servidor():

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


def validar_sistema_operativo():
    
    so_validos = ["Linux", "Windows"]
    no_valido = True
    while no_valido:
        so_ingresado = input("Ingrese Sistema Operativo (Linux / Windows): ")
        encontrado = False
        
        # Recorremos la lista para buscar si es valido
        for i in range(len(so_validos)):
            if so_ingresado == so_validos[i]:
                encontrado = True
                break  # Sale del bucle for porque ya lo encontró
                
        # Si la bandera quedó en False, el dato es inválido
        if encontrado == False:
            print("Error: El sistema operativo ingresado no es válido.")
            continue  # Vuelve al inicio del while a pedir el dato otra vez
        else:
            no_valido = False

    return so_ingresado  # Cuando sale del while, devuelve el SO válido


def validar_ubicacion_servidor():
    
    ubicacion_validos = ["Argentina", "Uruguay","Chile"]
    no_valido = True
    while no_valido:
        ubi_ingresado = input("Ingrese la ubicacion del Servidor (Argentica / Uruguay / Chile): ")
        encontrado = False
        
        # Recorremos la lista para buscar si es valido
        for i in range(len(ubicacion_validos)):
            if ubi_ingresado == ubicacion_validos[i]:
                encontrado = True
                break  # Sale del bucle for porque ya lo encontró
                
        # Si la bandera quedó en False, el dato es inválido
        if encontrado == False:
            print("Error: La ubicacion ingresada no es válida.")
            continue  # Vuelve al inicio del while a pedir el dato otra vez
        else:
            no_valido = False

    return ubi_ingresado  # Cuando sale del while, devuelve el SO válido

def validar_firewall():

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


def ingreso_porcentaje_cpu ():
    
 #   cpu = (input("ingrese el porcentaje de uso de la cpu: "))
    cpu = (input("ingrese el porcentaje de uso de la cpu (0 a 100): "))
    valor_porcentaje_cpu=validaciones.validar_porcentaje(cpu)
    
    while valor_porcentaje_cpu == "":
        print("Error: Ingrese un porcentaje válido (0 a 100).")
        cpu = (input("ingrese el porcentaje de uso de la cpu: "))
        valor_porcentaje_cpu=validaciones.validar_porcentaje(cpu)

    porcentaje_cpu = float (cpu)
    return porcentaje_cpu

def ingreso_porcentaje_ram ():
        
    ram = (input("ingrese el porcentaje de uso de la ram (0 a 100): "))
    valor_porcentaje_ram=validaciones.validar_porcentaje(ram)

    while valor_porcentaje_ram == "":
        print("Error: Ingrese un porcentaje válido (0 a 100).")
        ram = (input("ingrese el porcentaje de uso de la ram: "))
        valor_porcentaje_ram=validaciones.validar_porcentaje(ram)

    porcentaje_ram = float (ram)
    return porcentaje_ram

def ingreso_espacio_total_disco ():

    texto_disco = (input("ingrese el espacio total del disco (De 16 Gb hasta 4000 Gb): "))
    ingreso_valor_disco = validaciones.validar_total_disco(texto_disco)
    
    while ingreso_valor_disco == "":
        print("Error: Ingreso un espacio de disco invalido : ")
        texto_disco = (input("ingrese el espacio total del disco (De 16 Gb hasta 4000 Gb): "))
        ingreso_valor_disco = validaciones.validar_total_disco(texto_disco)

    almacenamiento_disco = float (texto_disco)
    return almacenamiento_disco

def ingreso_espacio_utilizado_disco(almacenamiento_disco:float):

    texto_disco = (input("ingrese el espacio utilizado del disco (0 hasta capacidad maxima del disco): "))
    ingreso_valor_disco = validaciones.validar_espacio_usado(texto_disco,almacenamiento_disco)
    
    while ingreso_valor_disco == "":
        print("Error: Ingresó un valor de espacio utlizado en disco invalido. ")
        texto_disco = input("ingrese el espacio utilizado del disco (0 hasta capacidad maxima del disco): ") 
        ingreso_valor_disco = validaciones.validar_espacio_usado(texto_disco,almacenamiento_disco)

    espacio_utilizado_disco = float (texto_disco)
    return espacio_utilizado_disco


def ingreso_procesos_activos():
    procesos = input("Ingrese la cantidad de procesos activos: ")
    valor_procesos = validaciones.validar_procesos(procesos)
    
    while valor_procesos == "":
        print("Error: Ingrese una cantidad válida de procesos enteros (1 a 600): ")
        procesos = input("Ingrese la cantidad de procesos activos: ")
        valor_procesos = validaciones.validar_procesos(procesos)
        
    return int(procesos)

