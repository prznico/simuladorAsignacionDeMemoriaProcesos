# 📊 SIMULADOR DE GESTIÓN DE MEMORIA

## 🌟 Descripcción
Este simulador visual muestra cómo se asignan y liberan los recursos de memoria cuando múltiples procesos se ejecutan concurrentemente. La interfaz gráfica permite:
  
  *  Generar procesos aleatorios con requerimientos de memoria y tiempo de ejecución

  *  Visualizar en tiempo real el estado de la memoria

  *  Monitorear qué procesos están activos y cuáles están en espera

  *  Observar cómo se libera la memoria cuando los procesos terminan

## 🖥️ Características principales
Visualización interactiva

  -  Barra de memoria con colores dinámicos (verde/naranja/rojo según uso)

  -  Contador de procesos activos y pendientes

  -  Listado detallado de todos los procesos con su estado actual

  -  Registro de eventos con marca de tiempo para seguimiento

Funcionalidades clave

  -  Generación de procesos con parámetros aleatorios

  -  Asignación automática de memoria cuando hay espacio disponible

  -  Ejecución concurrente de múltiples procesos

  -  Sistema de cola para procesos pendientes

  -  Liberación automática de recursos al finalizar procesos

Información mostrada
Para cada proceso se visualiza:

  -  ID único del proceso

  -  Memoria asignada (en MB)

  -  Tiempo de ejecución (en segundos)

  -  Estado actual (En espera/Ejecutando/Completado)

## 🛠️Requisitos
  -  Python 3.x

  -  Bibliotecas:

      *  tkinter

      *  ttk (incluida en tkinter)

      * random

      *  time

## 📝 Instrucciones de uso
  1.  Generar procesos:

      *  Ingrese el número de procesos deseados (1-10)

      *  Haga clic en "Generar Procesos"

  2.  Iniciar simulación:

      *  Haga clic en "Iniciar" para comenzar la ejecución

  3.  Monitorear:

      *  Observe la barra de memoria y los contadores

      *  Revise la lista de procesos y sus estados

      *  Siga los eventos en el registro

  4.  Controles adicionales:

      *  "Resetear" para limpiar la simulación

      *  "Finalizar" para cerrar la aplicación

## 🎨 Personalización
Puede modificar:

  -  memoria_total para cambiar la capacidad de memoria

  -  Los rangos de memoria/tiempo de los procesos en generar_datos_automaticos()

  -  Los colores de la barra de memoria en actualizar_barra_memoria()


## 🚀 Este proyecto es ideal para entender conceptos básicos de:

Gestión de memoria en sistemas operativos

Planificación de procesos

Asignación de recursos

Concurrencia básica
