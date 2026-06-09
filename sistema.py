from almacenamiento_procesos import porcentaje_uso_disco, estado_procesos, estado_almacenamiento
from estado_componentes import estado_cpu, estado_ram
from seguridad import firewall_estado, nivel_riesgo, problemas_detectados
from monitoreo_reportes import monitoreo_estado_servidor, estado_servidor, recomendaciones
import inputs

def iniciar_monitoreo():
    # Variables de entrada
    print("Bienvenido al sistema de monitoreo de servidores\n")

    nombre_servidor = inputs.ingreso_nombre_servidor()
    admin_name = inputs.ingreso_nombre_admin_servidor()

    sistema_operativo = inputs.validar_sistema_operativo()
    print()

    ubicacion_servidor = inputs.validar_ubicacion_servidor()
    print()

    firewall = inputs.validar_firewall()
    print()

    cpu = inputs.ingreso_porcentaje_cpu()
    print()

    ram = inputs.ingreso_porcentaje_ram()
    print()

    almacenamiento_disco = inputs.ingreso_espacio_total_disco()
    print()

    espacio_disco = inputs.ingreso_espacio_utilizado_disco(almacenamiento_disco)
    print()

    procesos_activos = inputs.ingreso_procesos_activos()
    print()

    # Variables calculadas
    rendimiento_cpu = estado_cpu(cpu)
    rendimiento_ram = estado_ram(ram)

    rendimiento_disco = porcentaje_uso_disco(
        espacio_disco,
        almacenamiento_disco
    )

    estado_alm = estado_almacenamiento(rendimiento_disco)
    estado_proc = estado_procesos(procesos_activos)

    riesgo = nivel_riesgo(
        cpu,
        ram,
        rendimiento_disco,
        procesos_activos,
        firewall,
        estado_alm
    )

    # Menú
    # Se agregaron Emojis y estetica al menú de opciones.
    #opcion = 0
    opcion = "0"  # Cambio papra que el programa no tire error si el ususario agrega un caracter diferente a 1,2,3

    while opcion != "3":

        opcion = (
            input(
                "\n1. 🖥️  Monitoreo de componentes"
                "\n2. 🔍 Diagnóstico del servidor"
                "\n3. ❌ Salir"
                "\n👉 Seleccione una opción: "
            )
        )

        match opcion:

            case "1":

                monitoreo_estado_servidor(
                    nombre_servidor,
                    admin_name,
                    sistema_operativo,
                    cpu,
                    ram,
                    espacio_disco,
                    procesos_activos,
                    firewall,
                    rendimiento_cpu,
                    rendimiento_ram,
                    rendimiento_disco,
                    estado_alm,
                    estado_proc,
                    riesgo
                )

            case "2":

                print(
                    f"\n🔍 Diagnóstico del servidor: {nombre_servidor}"
                    f"\n💿 Sistema operativo: {sistema_operativo}"
                    f"\n📍 Ubicación: {ubicacion_servidor}"
                )

                print(f"🧠 CPU: {rendimiento_cpu}")
                print(f"⚡ RAM: {rendimiento_ram}")
                print(f"💾 Disco: {estado_alm}")
                print(f"🔄 Procesos: {estado_proc}")

                firewall_estado(firewall)

                print(f"⚠️ Nivel de riesgo: {riesgo}")

                recomendaciones(
                    cpu,
                    ram,
                    procesos_activos,
                    firewall,
                    estado_alm,
                    riesgo
                )

            case "3":
                print("\n👋 Saliendo...")
                break

            case _:
                print("❌ Opción no válida")