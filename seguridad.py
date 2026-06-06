from colorama import Fore, Style, init
#Paquete que permite trabajar colores y estilos

#  ===Si colorama no esta dentro de tu biblioteca, generara un error en todos los Fore y Style===

init(autoreset=True)

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