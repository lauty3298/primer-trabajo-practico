from almacenamiento_procesos import porcentaje_uso_disco, estado_procesos, estado_almacenamiento
from estado_componentes import estado_cpu, estado_ram
from seguridad import firewall_estado, nivel_riesgo, problemas_detectados
from monitoreo_reportes import monitoreo_estado_servidor, estado_servidor, recomendaciones
import inputs
from usar_json import leer_json
from editar_parametros import modificar_parametro

def iniciar_monitoreo():
    # Variables de entrada
    print("Bienvenido al sistema de monitoreo de servidores\n")

    parametros = leer_json()

    componentes = parametros["componentes"]
    
    # Variables calculadas
    rendimiento_cpu = estado_cpu(componentes["cpu"])
    rendimiento_ram = estado_ram(componentes["ram"])

    rendimiento_disco = porcentaje_uso_disco(
        componentes["almacenamiento"],
        componentes["uso_almacenamiento"]
    )

    estado_alm = estado_almacenamiento(rendimiento_disco)
    estado_proc = estado_procesos(parametros["procesos"])

    riesgo = nivel_riesgo(
        componentes["cpu"],
        componentes["ram"],
        rendimiento_disco,
        parametros["procesos"],
        parametros["firewall"],
        estado_alm
    )

    # Menú
    # Se agregaron Emojis y estetica al menú de opciones.
    #opcion = 0
    opcion = "0"  # Cambio papra que el programa no tire error si el ususario agrega un caracter diferente a 1,2,3

    while opcion != "4":

        opcion = (
            input(
                "\n1. 🖥️  Monitoreo de componentes"
                "\n2. 🔍 Diagnóstico del servidor"
                "\n3. 🗄️ Modificar contenido "
                "\n4. ❌ Salir"
                "\n👉 Seleccione una opción: "
            )
        )

        match opcion:

            case "1":

                monitoreo_estado_servidor(
                rendimiento_cpu,
                rendimiento_ram,
                rendimiento_disco,
                estado_almacenamiento,
                estado_procesos,
                nivel_riesgo)
        
            case "2":

                print(
                    f"\n🔍 Diagnóstico del servidor: {parametros["server"]}"
                    f"\n💿 Sistema operativo: {parametros["SO"]}"
                    f"\n📍 Ubicación: {parametros["ubicacion"]}"
                )

                print(f"🧠 CPU: {rendimiento_cpu}")
                print(f"⚡ RAM: {rendimiento_ram}")
                print(f"💾 Disco: {estado_alm}")
                print(f"🔄 Procesos: {estado_proc}")

                firewall_estado(parametros["firewall"])

                print(f"⚠️ Nivel de riesgo: {riesgo}")

                recomendaciones(
                    componentes["cpu"],
                    componentes["ram"],
                    parametros["procesos"],
                    parametros["firewall"],
                    estado_alm,
                    riesgo
                    )

            case "3":
                modificar_parametro()
                
            case "4":
                print("\n👋 Saliendo...")
                break

            case _:
                print("❌ Opción no válida")