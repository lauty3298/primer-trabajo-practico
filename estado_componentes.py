from colorama import Fore, Style, init
#Paquete que permite trabajar colores y estilos

#  ===Si colorama no esta dentro de tu biblioteca, generara un error en todos los Fore y Style===

init(autoreset=True)

def estado_cpu(cpu=type(int)):
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