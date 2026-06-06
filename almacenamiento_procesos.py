from colorama import Fore, Style, init
#Paquete que permite trabajar colores y estilos

#  ===Si colorama no esta dentro de tu biblioteca, generara un error en todos los Fore y Style===

init(autoreset=True)

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


