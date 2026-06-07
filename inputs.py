import validaciones

def ingreso_nombre_servidor():
    pass

def ingreso_porcentaje_cpu ():
    
 #   cpu = (input("ingrese el porcentaje de uso de la cpu: "))
    cpu = (input("ingrese el porcentaje de uso de la cpu: "))
    valor_porcentaje_cpu=validaciones.validar_porcentaje(cpu)
    
    while valor_porcentaje_cpu == "":
        print("Error: Ingrese un porcentaje válido (0 a 100).")
        cpu = (input("ingrese el porcentaje de uso de la cpu: "))
        valor_porcentaje_cpu=validaciones.validar_porcentaje(cpu)

    porcentaje_cpu = float (cpu)
    return porcentaje_cpu

def ingreso_porcentaje_ram ():
        
    ram = (input("ingrese el porcentaje de uso de la ram: "))
    valor_porcentaje_ram=validaciones.validar_porcentaje(ram)

    while valor_porcentaje_ram == "":
        print("Error: Ingrese un porcentaje válido (0 a 100).")
        ram = (input("ingrese el porcentaje de uso de la ram: "))
        valor_porcentaje_ram=validaciones.validar_porcentaje(ram)

    porcentaje_ram = float (ram)
    return porcentaje_ram

def ingreso_espacio_total_disco ():

    texto_disco = (input("ingrese el espacio total del disco: "))
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
        print("Error: Ingrese una cantidad válida de procesos enteros (1 a 1000): ")
        procesos = input("Ingrese la cantidad de procesos activos: ")
        valor_procesos = validaciones.validar_procesos(procesos)
        
    return int(procesos)