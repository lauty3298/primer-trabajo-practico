#monitoreo del estado del servidor
from colorama import Fore, Style, init
from usar_json import leer_json

parametros = leer_json()

componentes = parametros["componentes"]

init(autoreset=True)

def monitoreo_estado_servidor(
                rendimiento_cpu,
                rendimiento_ram,
                rendimiento_disco,
                estado_almacenamiento,
                estado_procesos,
                nivel_riesgo
):

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

    print(
        f"⚙️ Nombre del servidor {parametros["server"]}\n",
        f"👤 Administrador: {parametros["dueño"]}\n",
        f"💿 Sistema operativo: {parametros["SO"]}\n",
        f"🧱 Estado del firewall: {parametros["firewall"]}\n",
        f"------ \n" ,
        f"🧠 El estado de la cpu: {componentes["cpu"]}%: {rendimiento_cpu}\n",
        f"⚡ El estado de la ram: {componentes["ram"]}%: {rendimiento_ram}\n",
        f"💾 El estado del disco: {componentes["almacenamiento"]}%: {rendimiento_disco}\n",
        f"📦 El almacenamiento del disco: {componentes["uso_almacenamiento"]}GB: {estado_almacenamiento}\n",
        f"🔄 El estado de los procesos activos: {estado_procesos}({"procesos"})\n",
        f"⚠️ El nivel de riesgo: {nivel_riesgo}\n",
        f"------ \n"
    )

def estado_servidor(nombre_servidor, admin_name, sistema_operativo, ubicacion_servidor,porcentaje_uso_disco,estado_procesos, firewall, rendimiento_cpu, rendimiento_ram, estado_almacenamiento, nivel_riesgo):
    print(f"⚙️ Nombre del servidor: {nombre_servidor}")
    print(f"👤 Administrador: {admin_name}")
    print(f"💿 Sistema operativo: {sistema_operativo}")
    print(f"📍 Ubicacion: {ubicacion_servidor}")
    print(f"🧱 Estado del firewall: {firewall}")
    print("------")
    print(f"🧠 El estado de la cpu: {rendimiento_cpu}")
    print(f"⚡ El estado de la ram: {rendimiento_ram}")
    print(f"💾 Porcentaje del disco en uso: {porcentaje_uso_disco}%")
    print(f"📦 El almacenamiento del disco: {estado_almacenamiento}")
    print(f"🔄 El estado de los procesos activos: {estado_procesos}")
    print(f"⚠️ El nivel de riesgo: {nivel_riesgo}")
    print("------")

#Recomendaciones 

def recomendaciones(
    cpu,
    ram,
    procesos_activos,
    firewall_estado, 
    estado_almacenamiento, 
    nivel_riesgo
    ):
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
    print(Fore.GREEN + "\n💡 Recomendaciones:" + Style.RESET_ALL)
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
    print(f"⚠️ El nivel de riesgo es: {nivel_riesgo}")