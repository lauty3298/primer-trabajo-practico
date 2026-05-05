from colorama import Fore, Style, init
#Paquete que permite trabajar colores y estilos

#  ===Si colorama no esta dentro de tu biblioteca, generara un error en todos los Fore y Style===

init(autoreset=True)

def estado_cpu(cpu):
    """
    Recibe el porcentaje de uso de CPU y retorna el estado

    Args: 
        cpu (int): El porcentaje de uso de la CPU

    Returns:
        str: El estado de la CPU
    """

#Aplicamos colores a los parametros: "normal, moderado, critico", estilo semaforo. 
#Rendimiento del CPU - colorama

    if cpu <= 50:
        rendimiento_cpu = Fore.GREEN + "Normal" + Style.RESET_ALL # verde
        return rendimiento_cpu
    elif cpu < 80:
        rendimiento_cpu = Fore.YELLOW + "Moderado" + Style.RESET_ALL # amarillo
        return rendimiento_cpu
    else:
        rendimiento_cpu = Fore.RED + "Critico" + Style.RESET_ALL # rojo
        return rendimiento_cpu

def estado_ram(ram):
    """
    Recibe el espacio usado del disco y devuele si el espacio que queda es suficiente, moderado o esta casi lleno 

    Args:
        espacio_disco (int): Espacio usado del disco

    Returns:
        str: Como es la capacidad que queda del disco
    """

#Rendimiento de la RAM - colorama

    if ram <= 50:
        rendimiento_ram = Fore.GREEN + "Normal" + Style.RESET_ALL
        return rendimiento_ram
    elif ram < 80:
        rendimiento_ram = Fore.YELLOW + "Moderado" + Style.RESET_ALL
        return rendimiento_ram
    else:
        rendimiento_ram = Fore.RED + "Critico" + Style.RESET_ALL
        return rendimiento_ram

def porcentaje_uso_disco(espacio_disco, almacenamiento_disco):
    """
    Recibe el espacio total del disco, el espacio ocupado y devuele el porcentaje de uso del mismo

    Args:
        espacio_disco (int): Espacio usado del disco
        almacenamiento_disco (int): Espacio total del disco

    Returns:
        int: El porcentaje de uso del disco
    """

    porcentaje_uso = (espacio_disco / almacenamiento_disco) * 100
    return porcentaje_uso

#Estado de procesos - colorama

def estado_procesos(procesos_activos):
    """
    Recibe la cantidad de procesos activos y devuele si esta cantidad es normal, moderada o alta 

    Args:
        procesos_activos (int): cantidad de procesos activos

    Returns:
        str: estado de procesos activos
    """
    if procesos_activos <= 100:
        return Fore.GREEN + "Normal" + Style.RESET_ALL
    elif procesos_activos < 200:
        return Fore.YELLOW + "Moderado" + Style.RESET_ALL
    else:
        return Fore.RED + "Alto" + Style.RESET_ALL
    

#Estado del firewall - colorama

def firewall_estado(firewall):
    """
    Recibe el estado del firewall y devuelve un mensaje con color

    Args:
        firewall (str): El estado actual del firewall (activo o desactivado)

    Returns:
        str: Mensaje con color indicando el estado del firewall
    """
    if not firewall == "Activo" and not firewall == "activo" and not firewall == "1":
        return Fore.GREEN + "Activo" + Style.RESET_ALL
    else:
        return Fore.RED + "Desactivado" + Style.RESET_ALL

#Estado de almacenamiento - colorama
#Porcentaje uso del disco

def estado_almacenamiento(porcentaje_uso_disco):
    """
    Evalua el porcentaje de uso del disco y devuelve un estado con color

    Args:
        porcentaje_uso_disco (int): El porcentaje de ocupacion del disco
    
    Returns:
        str: Un mensaje indicando si el estado es suficiente, moderado o casi lleno
    """
    if porcentaje_uso_disco <= 30:
        return Fore.GREEN + "Suficiente" + Style.RESET_ALL
    elif porcentaje_uso_disco < 65:
        return Fore.YELLOW + "Moderado" + Style.RESET_ALL
    else:
        return Fore.RED + "Casi lleno" + Style.RESET_ALL


def nivel_riesgo(cpu, ram, porcentaje_uso_disco, procesos_activos, firewall_estado, estado_almacenamiento):
    """
    Calcula el nivel de riesgo global del servidor basándose en múltiples parámetros.

    Args:
        cpu (int): Porcentaje de uso del procesador.
        ram (int): Porcentaje de uso de la memoria RAM.
        porcentaje_uso_disco (int): Porcentaje de ocupación del disco.
        procesos_activos (int): Cantidad de procesos en ejecución.
        firewall_estado (str): Estado del firewall ("Activo" o "Desactivado").
        estado_almacenamiento (str): Categoría del disco ("Suficiente", "Moderado", "Casi lleno").

    Returns:
        str: El nivel de riesgo estimado ("alto", "moderado" o "bajo") con su color correspondiente.
    """
    if cpu > 80 or ram > 80 or porcentaje_uso_disco > 80 or procesos_activos > 200 or firewall_estado == "Desactivado" or firewall_estado == "desactivado" or estado_almacenamiento == "Casi lleno":
        nivel_estimado_riesgo = nivel_estimado_riesgo = Fore.RED + "alto" + Style.RESET_ALL
    elif cpu > 50 or ram > 50 or porcentaje_uso_disco > 50 or procesos_activos > 100 or firewall_estado == "Desactivado" or firewall_estado == "desactivado" or estado_almacenamiento == "moderado":
        nivel_estimado_riesgo = Fore.YELLOW + "moderado" + Style.RESET_ALL
    else:
        nivel_estimado_riesgo = Fore.GREEN + "bajo" + Style.RESET_ALL
    return nivel_estimado_riesgo

def problemas_detectados(cpu, ram, espacio_disco, procesos_activos, firewall_estado, estado_almacenamiento):
    """
    Analiza los parámetros del servidor e imprime alertas específicas si se detectan anomalías.

    Args:
        cpu (int): Porcentaje de uso del procesador.
        ram (int): Porcentaje de uso de la memoria RAM.
        porcentaje_uso_disco (int): Porcentaje de ocupación del disco.
        espacio_disco (str): Espacio usado del disco.
        procesos_activos (int): Cantidad de procesos en ejecución.
        firewall_estado (str): Estado actual del firewall.
        estado_almacenamiento (str): Categoría de almacenamiento actual.
    """
    print(Fore.RED + "\nProblemas detectados:" + Style.RESET_ALL)
    if cpu > 80:
        print(f"Uso de CPU alto: {cpu}%")
    elif cpu > 50:
        print(f"Uso de CPU moderado: {cpu}%")
    if ram > 80:
        print(f"Uso de RAM alto: {ram}%")
    elif ram > 50:
        print(f"Uso de RAM moderado: {ram}%")
    if procesos_activos > 200:
        print(f"Cantidad de procesos activos alta")
    elif procesos_activos > 100:
        print(f"Cantidad de procesos activos moderada")
    if firewall_estado == "Desactivado":
        print(f"Firewall desactivado")
    if estado_almacenamiento == "Casi lleno":
        print(f"Almacenamiento casi lleno: {espacio_disco} GB usados")
    elif estado_almacenamiento == "moderado":
        print(f"Almacenamiento moderado: {espacio_disco} GB usados")

#Recomendaciones 

def recomendaciones(cpu, ram, procesos_activos, firewall_estado, estado_almacenamiento, nivel_riesgo):
    """
    Analiza las métricas del servidor y muestra sugerencias para optimizar el rendimiento.

    Args:
        cpu (int): Porcentaje de uso del procesador.
        ram (int): Porcentaje de uso de la memoria RAM.
        porcentaje_uso_disco (int): Porcentaje de ocupación del disco duro.
        procesos_activos (int): Cantidad de procesos corriendo actualmente.
        firewall_estado (str): Estado de seguridad del firewall.
        estado_almacenamiento (str): Clasificación actual del espacio en disco.
        nivel_riesgo (str): Nivel de riesgo calculado.
    """
    print(Fore.GREEN + "\nRecomendaciones:" + Style.RESET_ALL)
    if cpu > 80:
        print("Reiniciar el servidor para reducir el uso de la cpu")
    elif cpu > 50:
        print("Cerrar aplicaciones que consuman mucha cpu")
    if ram > 80:
        print("Cerrar aplicaciones que consuman mucha memoria ram")
    elif ram > 50:
        print("Cerrar aplicaciones que consuman mucha memoria ram")
    if procesos_activos > 200:
        print("Reiniciar el servidor para reducir los procesos activos")
    elif procesos_activos > 100:
        print("Cerrar aplicaciones innecesarias para reducir los procesos activos")
    if firewall_estado == "Desactivado":
        print("Activar el firewall para mejorar la seguridad del servidor")
    if estado_almacenamiento == "Casi lleno":
        print("Liberar espacio en el disco para mejorar el rendimiento del servidor")
    elif estado_almacenamiento == "moderado":
        print("Monitorear el almacenamiento para evitar problemas de rendimiento")
    print("--------------------------------------")
    print(f"El nivel de riesgo es: {nivel_riesgo}")

#monitoreo del estado del servidor

def monitoreo_estado_servidor(nombre_servidor, admin_name, sistema_operativo, cpu, ram, disco, espacio_disco, procesos_activos, firewall, rendimiento_cpu, rendimiento_ram, rendimiento_disco, estado_almacenamiento, estado_procesos, nivel_riesgo):
    """
    Imprime el reporte detallado del estado del servidor en la consola.

    Args:
        nombre_servidor (str): El nombre asignado al servidor.
        sistema_operativo (str): El SO que está corriendo.
        cpu (float): Porcentaje de uso del CPU.
        ram (float): Porcentaje de uso de la memoria RAM.
        disco (float): Porcentaje de uso del disco.
        espacio_disco (float): Espacio total o disponible en GB.
        procesos_activos (int): Total de procesos corriendo.
        firewall (str): Estado del firewall.
        rendimiento_cpu (str): Estado del CPU con color.
        rendimiento_ram (str): Estado de la RAM con color.
        rendimiento_disco (str): Estado del disco con color.
        estado_almacenamiento (str): Estado del almacenamiento con color
        estado_procesos (str): Estado de los proceos
        nivel_riesgo (str): Clasificacion del estado de riesgo
    """
    print(f"Nombre del servidor: {nombre_servidor}")
    print(f"Administrador: {admin_name}")
    print(f"Sistema operativo: {sistema_operativo}")
    print(f"Estado del firewall: {firewall}")
    print("------")
    print(f"El estado de la cpu: {cpu}%: {rendimiento_cpu}")
    print(f"El estado de la ram: {ram}%: {rendimiento_ram}")
    print(f"El estado del disco: {disco}%: {rendimiento_disco}")
    print(f"El almacenamiento del disco: {espacio_disco} GB: {estado_almacenamiento}")
    print(f"El estado de los procesos activos: {estado_procesos}({procesos_activos})")
    print(f"El nivel de riesgo: {nivel_riesgo}")
    print("------")

def estado_servidor(nombre_servidor, admin_name, sistema_operativo, ubicacion_servidor, firewall, rendimiento_cpu, rendimiento_ram, estado_almacenamiento, nivel_riesgo):
    print(f"Nombre del servidor: {nombre_servidor}")
    print(f"Administrador: {admin_name}")
    print(f"Sistema operativo: {sistema_operativo}")
    print(f"Ubicacion: {ubicacion_servidor}")
    print(f"Estado del firewall: {firewall}")
    print("------")
    print(f"El estado de la cpu: {rendimiento_cpu}")
    print(f"El estado de la ram: {rendimiento_ram}")
    print(f"porcentaje del disco en uso: {porcentaje_uso_disco}%")
    print(f"El almacenamiento del disco: {estado_almacenamiento}")
    print(f"El estado de los procesos activos: {estado_procesos}")
    print(f"El nivel de riesgo: {nivel_riesgo}")
    print("------")


