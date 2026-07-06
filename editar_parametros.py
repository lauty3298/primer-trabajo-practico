from usar_json import leer_json, modificar_json
from inputs import (
    ingreso_nombre_servidor, 
    ingreso_nombre_admin_servidor, 
    ingreso_procesos_activos, 
    ingreso_porcentaje_cpu, 
    ingreso_porcentaje_ram,
    ingreso_espacio_total_disco,
    ingreso_espacio_utilizado_disco
    )

def modificar_parametro():
    """
    Despliega el menu interactivo para modificar los parametros del servidor.
    Carga la configuracion actual JSON y presenta un menu con opciones para alterar campos especificos del sistema.
    Esto se ejecuta hasta que el usuario elige la opcion de salida ("11")
    Esta funcion delega la persistencia de los cambios en la funcion modificar_json 
    """
    parametros = leer_json()

    componentes = parametros["componentes"]

    opcion = 0
    eleccion = ""
    while opcion != "11":

        print(
            "1. nombre de servidor"
            "\n2. nombre del admin"
            "\n3. sistema operativo"
            "\n4. ubicacion"
            "\n5. firewall"
            "\n6. procesos activos"
            "\n7. uso del cpu"
            "\n8. uso de la ram"
            "\n9. espacio total del almacenamiento"
            "\n10. espacio ocupado del almacenamiento"
            "\n11. salir"
        )

        opcion = input("que desea cambiar?: ")

        match opcion:
            case "1":
                parametros["server"] = ingreso_nombre_servidor()

                modificar_json(parametros)

                print("\ncambiado exitosamente.")
            case "2":
                parametros["dueño"] = ingreso_nombre_admin_servidor()

                modificar_json(parametros)

                print("cambiado exitosamente.")

            case "3":
                eleccion = input(
                    "1. windowns"
                    "\n2. linux"
                    "\n3. mac"
                    "\nque sistema operativo esta usando?: "
                )
                match eleccion:
                    case "1":
                        parametros["SO"] = "windowns"

                        modificar_json(parametros)

                        print("cambiado exitosamente.")
                    case "2":
                        parametros["SO"] = "linux"

                        modificar_json(parametros)

                        print("cambiado exitosamente.")
                    case "3":
                        parametros["SO"] = "mac"

                        modificar_json(parametros)

                        print("cambiado exitosamente.")
                    case "_":
                        print("eleccion invalida.")

            case "4":
                eleccion = input(
                    "1. argentina"
                    "\n2. uruguay"
                    "\n3. chile"
                    "\nque ubicacion esta usando?: "
                    )

                match eleccion:
                    case "1":
                        parametros["ubicacion"] = "argentina"

                        modificar_json(parametros)

                        print("cambiado exitosamente.")
                    case "2":
                        parametros["ubicacion"] = "uruguay"

                        modificar_json(parametros)

                        print("cambiado exitosamente.")
                    case "3":
                        parametros["ubicacion"] = "chile"

                        modificar_json(parametros)

                        print("cambiado exitosamente.")
                    case "_":
                        print("eleccion invalida.")
            case "5":
                eleccion = input(
                    "1. activo"
                    "\n2. inactivo"
                    "\nen que estado esta el firewall?: "
                    )

                match eleccion:
                    case "1":
                        parametros["firewall"] = "activo"

                        modificar_json(parametros)

                        print("cambiado exitosamente.")
                    case "2":
                        parametros["firewall"] = "inactivo"

                        modificar_json(parametros)

                        print("cambiado exitosamente.")

                    case "_":
                        print("eleccion invalida.")
            case "6":
                parametros["procesos"] = ingreso_procesos_activos()

                modificar_json(parametros)

                print("\ncambiado exitosamente.")
            case "7":
                componentes["cpu"] = ingreso_porcentaje_cpu()

                modificar_json(parametros)

                print("\ncambiado exitosamente.")
            case "8":
                componentes["ram"] = ingreso_porcentaje_ram()

                modificar_json(parametros)

                print("\ncambiado exitosamente.")
            case "9":
                componentes["almacenamiento"] = ingreso_espacio_total_disco()

                modificar_json(parametros)

                print("\ncambiado exitosamente.")
                
            case "10":
                componentes["uso_almacenamiento"] = ingreso_espacio_utilizado_disco(componentes["almacenamiento"])

                modificar_json(parametros)

                print("\ncambiado exitosamente.")

            case "11":
                return
            case _:
                print("opcion invalida.")