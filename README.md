# 🖥️ Sistema de Monitoreo de Servidores

Este proyecto es una aplicación en Python que permite simular el monitoreo de un servidor, evaluando su estado en base a distintos parámetros como uso de CPU, RAM, disco, procesos activos y estado del firewall.

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

-------------------------------------------

## 🧠 Funcionamiento

El sistema solicita al usuario información del servidor:

* Nombre del servidor
* Administrador
* Sistema operativo
* Ubicación
* Estado del firewall
* Uso de CPU y RAM
* Uso de disco
* Cantidad de procesos activos

Luego procesa estos datos mediante funciones del módulo `componentes.py` para:

* Evaluar el estado de cada componente
* Calcular el nivel de riesgo
* Mostrar información detallada

-------------------------------------------

## 📋 Menú principal

El programa incluye un menú interactivo:

-------------------------------------------
1. Monitoreo de componentes
2. Diagnóstico del servidor
3. Salir
```

### 🔍 Monitoreo

Muestra el estado completo del servidor.

### ⚠️ Diagnóstico

* Detecta problemas
* Muestra recomendaciones
* Indica el nivel de riesgo

-------------------------------------------

## 🎨 Ejemplo de salida

-------------------------------------------
El estado de la cpu: 85%: Critico
El estado de la ram: 60%: Moderado
El nivel de riesgo: alto
```

*(Los colores se visualizan correctamente en consola gracias a `colorama`)*

-------------------------------------------

## 👨‍💻 Autores

Desarrollado por:
Lautaro Vallejos,
Tomas Clara y
Gaston Cespedes

-------------------------------------------


