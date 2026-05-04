import componentes

# Variables de entrada

print("Bienvenido al sistema de monitoreo de servidores")
nombre_servidor = input("ingrese el nombre del servidor: ")
admin_name = input("ingrese el nombre del administrador del servidor: ")
print("Selecciones el sistema operativo del servidor: \n1. Windows\n2. Linux")
sistema_operativo = input("ingrese el sistema operativo del servidor: ")
match sistema_operativo:
    case "Windows" | "windows" | "1":
        sistema_operativo = "Windows"
    case "Linux" | "linux" | "2":
        sistema_operativo = "Linux"
    case _:
        print("Opcion no valida, seleccione nuevamente")
        sistema_operativo = input(
            "ingrese el sistema operativo del servidor: "
        )
print(
    "Seleccione la ubicacion del servidor: "
    "\n1. Argentina\n2. Chile\n3. Uruguay"
)
ubicacion_servidor = input("ingrese la ubicacion del servidor: ")
match ubicacion_servidor:
    case "Argentina" | "argentina" | "1":
        ubicacion_servidor = "Argentina"
    case "Chile" | "chile" | "2":
        ubicacion_servidor = "Chile"
    case "Uruguay" | "uruguay" | "3":
        ubicacion_servidor = "Uruguay"
    case _:
        print("Opcion no valida, seleccione nuevamente")
        ubicacion_servidor = input("ingrese la ubicacion del servidor: ")

print("Seleccione el estado del firewall: \n1. Activo\n2. Desactivado")
firewall = input("ingrese el estado del firewall: ")
match firewall:
    case "Activo" | "activo" | "1":
        firewall = "Activo"
    case "Desactivado" | "desactivado" | "2":
        firewall = "Desactivado"
    case _:
        print("Opcion no valida, seleccione nuevamente")
        firewall = input("ingrese el estado del firewall: ")
cpu = int(input("ingrese el porcentaje de uso de la cpu: "))
ram = int(input("ingrese el porcentaje de uso de la ram: "))
almacenamiento_disco = int(input("ingrese el espacio total del disco: "))
espacio_disco = int(input("ingrese el espacio usado en el disco: "))
procesos_activos = int(input("ingrese la cantidad de procesos activos: "))

# Variables de salida
rendimiento_cpu = componentes.estado_cpu(cpu)
rendimiento_ram = componentes.estado_ram(ram)
rendimiento_disco = componentes.porcentaje_uso_disco(
    espacio_disco,
    almacenamiento_disco
)
estado_almacenamiento = componentes.estado_almacenamiento(rendimiento_disco)
estado_procesos = componentes.estado_procesos(procesos_activos)
nivel_riesgo = componentes.nivel_riesgo(
    cpu,
    ram,
    rendimiento_disco,
    procesos_activos,
    componentes.firewall_estado(firewall),
    estado_almacenamiento
)

# Menu
opcion = int( input("1. monitoreo de componentes\n""2. Diagnostico del servidor\n""3. salir\n" ))
match opcion:
        case 1:
            # monitoreo de componentes
            componentes.monitoreo_estado_servidor(
                nombre_servidor,
                admin_name,
                sistema_operativo,
                cpu,
                ram,
                rendimiento_disco,
                espacio_disco,
                procesos_activos,
                firewall,
                rendimiento_cpu,
                rendimiento_ram,
                rendimiento_disco,
                estado_almacenamiento,
                estado_procesos,
                nivel_riesgo
            )
        case 2:
            # Resultado esperado
            print(f"\nDiagnostico del servidor: {nombre_servidor}\nSistema operativo: {sistema_operativo}\nUbicacion: {ubicacion_servidor}")
            componentes.problemas_detectados(
                cpu,
                ram,
                espacio_disco,
                procesos_activos,
                firewall,
                estado_almacenamiento
            )
            componentes.recomendaciones(
                cpu,
                ram,
                procesos_activos,
                firewall,
                estado_almacenamiento,
                nivel_riesgo
            )
        case 3:
            print("saliendo...")
        case _:
            print("Opcion no valida")
            opcion = int(
                input("1. monitoreo de componentes\n""2. Diagnostico del servidor\n""3. salir\n"))
