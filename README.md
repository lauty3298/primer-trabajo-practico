# 🖥️ Sistema de Monitoreo de Servidores

Este proyecto es una aplicación en Python que permite simular el monitoreo de un servidor, evaluando su estado en base a distintos parámetros como uso de CPU, RAM, disco, procesos activos y estado del firewall.

> 🚀 **[NUEVO - SPRINT 2]:** El sistema evolucionó de un script funcional a un mini-sistema estructurado, aplicando el principio DRY (No te repitas), modularización en múltiples archivos `.py`, documentación interna con *docstrings* y un `main.py` limpio que actúa puramente como punto de entrada.

-------------------------------------------

## 📌 Características

* Monitoreo de:
  * CPU
  * Memoria RAM
  * Uso de disco
  * Procesos activos
  * Estado del firewall
* Diagnóstico automático del servidor
* Detección de problemas
* Recomendaciones según el estado del sistema
* Clasificación del nivel de riesgo (bajo, moderado, alto)
* Salida en consola con colores (usando `colorama`)
* 🖥️ **[NUEVO - SPRINT 2]:** Interfaz mejorada visualmente con emojis claros en menús y reportes para una lectura más amigable.

-------------------------------------------

## 🧠 Funcionamiento

El sistema solicita al usuario información del servidor:

* Nombre del servidor *(Mínimo 5 caracteres - SPRINT 2)*
* Administrador *(Mínimo 5 caracteres - SPRINT 2)*
* Sistema operativo *(Soporta mayúsculas/minúsculas de forma flexible - SPRINT 2)*
* Ubicación *(Soporta mayúsculas/minúsculas de forma flexible - SPRINT 2)*
* Estado del firewall
* Uso de CPU y RAM
* Uso de disco
* Cantidad de procesos activos

Luego procesa estos datos mediante funciones del módulo `componentes.py` para:

* Evaluar el estado de cada componente
* Calcular el nivel de riesgo
* Mostrar información detallada

> 📂 **[NUEVO - SPRINT 2] Organización del Sistema:** La lógica ahora está completamente distribuida en módulos específicos (`inputs.py` para capturas, `validaciones.py` para controles robustos sin métodos prohibidos de listas, y `sistema.py` para el control de flujo del menú).

-------------------------------------------

## 📋 Menú principal

El programa incluye un menú interactivo:

-------------------------------------------
1. 🖥️ Monitoreo de componentes `[Actualizado con emojis]`
2. 🔍 Diagnóstico del servidor `[Actualizado con emojis]`
3. ❌ Salir `[Actualizado con emojis]`

### 🔍 Monitoreo

Muestra el estado completo del servidor.

### ⚠️ Diagnóstico

* Detecta problemas
* Muestra recomendaciones
* Indica el nivel de riesgo

-------------------------------------------

## 🎨 Ejemplo de salida

-------------------------------------------
🧠 El estado de la cpu: 85%: Critico
⚡ El estado de la ram: 60%: Moderado
⚠️ El nivel de riesgo: alto

*(Los colores se visualizan correctamente en consola gracias a `colorama` y los emojis ayudan a identificar los componentes de un vistazo)*

-------------------------------------------

NUEVO SPRINT 3: PERSISTENCIA DE DATOS

Se agregó:
• Uso de diccionarios. 
• Manejo de archivos.  
• Persistencia de datos. 
• Reutilización de la información almacenada. 

# 1. Estructura de los diccionarios:
 Para la getion y monitoreo del servidor, se utiliza una estructura de diccionario anidada en PYTHON.
 Esto permite agrupar los datos gnenerales en el primer nivel y aislar las metricas del hardware en un sub-diccionario 
 facilitando su lectura y escalabilidad.


### 📂 Vista del archivo `parametros.json`

```json
{
    "server": "latam-verso",
    "dueño": "juanchopanza",
    "SO": "mac",
    "ubicacion": "argentina",
    "procesos": 523,
    "firewall": "activo",
    "componentes": {
        "cpu": 23.0,
        "ram": 89.0,
        "almacenamiento": 500.0,
        "uso_almacenamiento": 89.0
    }
}
```
# 2. Formato de Archivo Utilizado
Se seleccionó el formato JSON (`.json`) para la persistencia de datos a través del archivo `parametros.json`. Las razones de su elección son:
*Compatibilidad nativa:* Python lo transforma directamente en un diccionario mediante la librería estándar `json` (`json.load` y `json.dump`).
*Legibilidad:* Al guardarse con indentación de 4 espacios y codificación `utf-8`, permite que cualquier administrador lea o edite la configuración de forma externa fácilmente.

# 3. Organización de los Módulos del Proyecto
El proyecto está estructurado de forma modular para respetar el principio de *responsabilidad única*, separando la interfaz de usuario, las validaciones, la lógica del Sistema  y la persistencia:

```
primer-trabajo-practico/
│
├── main.py                   # Punto de entrada de la aplicación. 
├── sistema.py                # Módulo principal de control y manejo del monitoreo.
├── editar_parametros.py      # Interfaz de usuario (menús de consola) para modificar datos.
├── usar_json.py              # Capa de persistencia (Lectura y escritura del archivo JSON).
├── inputs.py                 # Captura de datos ingresados por el usuario por teclado.
├── validaciones.py           # Funciones de control (asegura datos correctos).
├── estado_componentes.py     # Lógica matemática y cálculos de rendimiento del hardware.
├── monitoreo_reportes.py     # Generación de alertas, recomendaciones.
├── seguridad.py              # Módulo encargado de informar los problemas detectados y niveles de riesgo.
│
├── parametros.json           # Archivo físico donde se guardan los parámetros.
└── README.md                 # Documentación general del proyecto.
```
---------------------------------------------------

# 📋 Menú principal

1. 🖥️  Monitoreo de componentes
2. 🔍 Diagnóstico del servidor
3. 🗄️ Modificar contenido 
4. ❌ Salir
👉 Seleccione una opción: 1

⚙️ Nombre del servidor latam-verso
👤 Administrador: juanchopanza
💿 Sistema operativo: linux
🧱 Estado del firewall: activo
------ 
🧠 El estado de la cpu: 23.0%: Normal
⚡ El estado de la ram: 89.0%: Critico
💾 El estado del disco: 500.0%: 561.7977528089888
📦 El almacenamiento del disco: 89.0GB: <function estado_almacenamiento at 0x000001D2CA333950>
🔄 El estado de los procesos activos: <function estado_procesos at 0x000001D2CA3338A0>(procesos)

------
1. 🖥️  Monitoreo de componentes
2. 🔍 Diagnóstico del servidor
3. 🗄️ Modificar contenido 
4. ❌ Salir
👉 Seleccione una opción: 3

1. nombre de servidor
2. nombre del admin
3. sistema operativo
4. ubicacion
5. firewall
6. procesos activos
7. uso del cpu
8. uso de la ram
9. espacio total del almacenamiento
10. espacio ocupado del almacenamiento
11. salir
    
que desea cambiar?: 3
1. windowns
2. linux
3. mac
   
Que sistema operativo esta usando?: 3
Cambiado exitosamente.

 
## 👨‍💻 Autores

Desarrollado por:
* Lautaro Vallejos
* Gaston Cespedes
* Adrian Robles
