from almacenamiento_procesos import porcentaje_uso_disco, estado_procesos, estado_almacenamiento
from estado_componentes import estado_cpu, estado_ram
from seguridad import firewall_estado, nivel_riesgo, problemas_detectados
from monitoreo_reportes import monitoreo_estado_servidor, estado_servidor, recomendaciones

# Variables de entrada
print("Bienvenido al sistema de monitoreo de servidores")

nombre_servidor = input("Ingrese el nombre del servidor: ")
admin_name = input("Ingrese el nombre del administrador del servidor: ")

print("Seleccione el sistema operativo del servidor:")
print("1. Windows")
print("2. Linux")

sistema_operativo = input("Ingrese el sistema operativo del servidor: ")

match sistema_operativo:
    case "Windows" | "windows" | "1":
        sistema_operativo = "Windows"
    case "Linux" | "linux" | "2":
        sistema_operativo = "Linux"
    case _:
        print("Opción no válida")
        sistema_operativo = input("Ingrese el sistema operativo del servidor: ")

print(
    "Seleccione la ubicación del servidor:"
    "\n1. Argentina"
    "\n2. Chile"
    "\n3. Uruguay"
)

ubicacion_servidor = input("Ingrese la ubicación del servidor: ")

match ubicacion_servidor:
    case "Argentina" | "argentina" | "1":
        ubicacion_servidor = "Argentina"
    case "Chile" | "chile" | "2":
        ubicacion_servidor = "Chile"
    case "Uruguay" | "uruguay" | "3":
        ubicacion_servidor = "Uruguay"
    case _:
        print("Opción no válida")
        ubicacion_servidor = input("Ingrese la ubicación del servidor: ")

print("Seleccione el estado del firewall:")
print("1. Activo")
print("2. Desactivado")

firewall = input("Ingrese el estado del firewall: ")

match firewall:
    case "Activo" | "activo" | "1":
        firewall = "Activo"
    case "Desactivado" | "desactivado" | "2":
        firewall = "Desactivado"
    case _:
        print("Opción no válida")
        firewall = input("Ingrese el estado del firewall: ")

cpu = float(input("Ingrese el porcentaje de uso de CPU: "))
ram = float(input("Ingrese el porcentaje de uso de RAM: "))
almacenamiento_disco = float(input("Ingrese el espacio total del disco: "))
espacio_disco = float(input("Ingrese el espacio usado del disco: "))
procesos_activos = int(input("Ingrese la cantidad de procesos activos: "))

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
opcion = 0

while opcion != 3:

    opcion = int(
        input(
            "\n1. Monitoreo de componentes"
            "\n2. Diagnóstico del servidor"
            "\n3. Salir"
            "\nSeleccione una opción: "
        )
    )

    match opcion:

        case 1:

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

        case 2:

            print(
                f"\nDiagnóstico del servidor: {nombre_servidor}"
                f"\nSistema operativo: {sistema_operativo}"
                f"\nUbicación: {ubicacion_servidor}"
            )

            print(f"CPU: {rendimiento_cpu}")
            print(f"RAM: {rendimiento_ram}")
            print(f"Disco: {estado_alm}")
            print(f"Procesos: {estado_proc}")

            firewall_estado(firewall)

            print(f"Nivel de riesgo: {riesgo}")

            # Si la función recibe parámetros, agrégalos aquí
            # problemas_detectados(...)

            recomendaciones(
                cpu,
                ram,
                procesos_activos,
                firewall,
                estado_alm,
                riesgo
            )

        case 3:
            print("\nSaliendo...")
            break

        case _:
            print("Opción no válida")