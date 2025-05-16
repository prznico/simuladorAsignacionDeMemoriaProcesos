import tkinter as tk
from tkinter import messagebox, ttk
import random

#creamos la ventana principal
ventana = tk.Tk()
ventana.title("Asignación de memoria a los procesos")

ventana.memoria_total = 100
ventana.memoria_disponible = ventana.memoria_total
procesos_pendientes = []
procesos_ejecucion = 0


# ---- Funciones ---
def actualizar_barra_memoria():
    usado = ventana.memoria_total - ventana.memoria_disponible
    porcentaje = usado / ventana.memoria_total
    ventana.barra_memoria['value'] = usado
    ventana.label_memoria.config(text=f"{ventana.memoria_disponible}/{ventana.memoria_total} MB")

    style = ttk.Style()
    if porcentaje <= 0.7:
        style.configure("verde.Horizontal.TProgressbar", troughcolor='white', background='green')
        ventana.barra_memoria.config(style="verde.Horizontal.TProgressbar")
    elif porcentaje <= 0.9:
        style.configure("naranja.Horizontal.TProgressbar", troughcolor='white', background='orange')
        ventana.barra_memoria.config(style="naranja.Horizontal.TProgressbar")
    else:
        style.configure("rojo.Horizontal.TProgressbar", troughcolor='white', background='red')
        ventana.barra_memoria.config(style="rojo.Horizontal.TProgressbar")

def actualizar_contador():
    label_procesos_activos.config(text=f"Procesos en ejecución: {procesos_ejecucion}")

def actualizar_lista_pendientes():
    lista_pendientes.delete(0, tk.END)
    for p in procesos_pendientes:
        lista_pendientes.insert(tk.END, f"Proceso {p[0]} ({p[1]} MB, {p[2]} seg)")

def log_evento(texto):
    cuadro_texto.insert(tk.END, texto + "\n")
    cuadro_texto.see(tk.END)

def generar_datos_automaticos():
    try:
        num_procesos = int(entrada_texto.get().strip())
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")
        return []

    if num_procesos < 1 or num_procesos > 10:
        messagebox.showerror("Error", "El número de procesos debe estar entre 1 y 10")
        return []

    data = []
    for i in range(1, num_procesos + 1):
        memoria = random.randint(10, 90)
        tiempo = random.randint(1, 5)
        data.append((i, f"{memoria} MB", f"{tiempo} seg"))
    return data

def genera_procesos():
    for item in tree.get_children():
        tree.delete(item)
    datos = generar_datos_automaticos()
    for row in datos:
        tree.insert("", "end", values=row)

    resetear_memoria()

def resetear_memoria():
    global procesos_ejecucion
    ventana.memoria_disponible = ventana.memoria_total
    procesos_pendientes.clear()
    procesos_ejecucion = 0
    actualizar_barra_memoria()
    actualizar_contador()
    actualizar_lista_pendientes()
    cuadro_texto.delete("1.0", tk.END)

def asignar_proceso(id_proceso, memoria_requerida, tiempo):
    global procesos_ejecucion
    if ventana.memoria_disponible >= memoria_requerida:
        ventana.memoria_disponible -= memoria_requerida
        procesos_ejecucion += 1
        actualizar_barra_memoria()
        actualizar_contador()
        log_evento(f"✅ Proceso {id_proceso} asignado ({memoria_requerida} MB, {tiempo} seg)")

        def liberar():
            global procesos_ejecucion
            ventana.memoria_disponible += memoria_requerida
            procesos_ejecucion -= 1
            actualizar_barra_memoria()
            actualizar_contador()
            log_evento(f"🟢 Proceso {id_proceso} finalizado. Liberó {memoria_requerida} MB")
            revisar_procesos_pendientes()

        ventana.after(tiempo * 1000, liberar)
        return True
    return False

def iniciar_simulacion():
    procesos = tree.get_children()
    if not procesos:
        messagebox.showinfo("Info", "Primero genera los procesos.")
        return

    resetear_memoria()

    for proceso in procesos:
        id_p, mem, t = tree.item(proceso)['values']
        memoria = int(mem.split()[0])
        tiempo = int(t.split()[0])
        asignado = asignar_proceso(id_p, memoria, tiempo)
        if not asignado:
            procesos_pendientes.append((id_p, memoria, tiempo))
            log_evento(f"❌ Proceso {id_p} encolado (No hay memoria suficiente)")
    actualizar_lista_pendientes()

def revisar_procesos_pendientes():
    pendientes_actualizados = []
    for p in procesos_pendientes:
        id_p, mem, t = p
        if not asignar_proceso(id_p, mem, t):
            pendientes_actualizados.append(p)
    procesos_pendientes[:] = pendientes_actualizados
    actualizar_lista_pendientes()

def resetear():
    tree.delete(*tree.get_children())
    entrada_texto.delete(0, tk.END)
    entrada_texto.insert(0, "0")
    resetear_memoria()

# ----- INTERFAZ -----

#el cuadro de texto para que se ingresen los procesos 
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=5)
tk.Label(frame_entrada, text="Número de procesos:").pack(side=tk.LEFT)
entrada_texto = tk.Entry(frame_entrada, width=5)
entrada_texto.pack(side=tk.LEFT, padx=5)
entrada_texto.insert(0, " ")

#inserta la tabla de los procesos
tree = ttk.Treeview(ventana, columns=("ID Tarea", "Memoria", "Tiempo"), show="headings")
tree.heading("ID Tarea", text="ID Proceso")
tree.heading("Memoria", text="Memoria (MB)")
tree.heading("Tiempo", text="Tiempo (seg)")
tree.column("ID Tarea", width=100, anchor=tk.CENTER)
tree.column("Memoria", width=100, anchor=tk.CENTER)
tree.column("Tiempo", width=100, anchor=tk.CENTER)
tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

#mensaje de memoria
frame_memoria = tk.Frame(ventana, padx=10, pady=5)
frame_memoria.pack(fill=tk.X)
tk.Label(frame_memoria, text="Memoria:").pack(side=tk.LEFT)

#estilo de la barra de memoria
style = ttk.Style()
style.theme_use('default')
style.configure("verde.Horizontal.TProgressbar", troughcolor='white', background='green')

#Muestra la barra de memoria
ventana.barra_memoria = ttk.Progressbar(
    frame_memoria, orient=tk.HORIZONTAL, length=300, mode='determinate',
    maximum=ventana.memoria_total, style="verde.Horizontal.TProgressbar"
)
#muestra la memoria disponible y la memoria total al lado derecho de la barra
ventana.barra_memoria.pack(side=tk.LEFT, padx=5)
ventana.label_memoria = tk.Label(frame_memoria, text=f"{ventana.memoria_disponible}/{ventana.memoria_total} MB")
ventana.label_memoria.pack(side=tk.LEFT)

#los procesos en ejecucion
label_procesos_activos = tk.Label(ventana, text="Procesos en ejecución: 0")
label_procesos_activos.pack(pady=2)

#Muestra los procesos pendientes
frame_pendientes = tk.Frame(ventana)
frame_pendientes.pack(pady=5)
tk.Label(frame_pendientes, text="Procesos pendientes:").pack()
lista_pendientes = tk.Listbox(frame_pendientes, height=4, width=60)
lista_pendientes.pack()

#cuadro de texto en donde se muestran los procesos que se estan ejecutando, se van a la cola o finalizan
cuadro_texto = tk.Text(ventana, height=8, width=70)
cuadro_texto.pack(pady=10)

#Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Generar Procesos", command=genera_procesos, activebackground="yellow").pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Iniciar", command=iniciar_simulacion, activebackground="olive").pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Resetear", command=resetear, activebackground="lightblue").pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Finalizar", command=ventana.destroy, activebackground="salmon").pack(side=tk.LEFT, padx=5)

actualizar_barra_memoria()
#inicializa
ventana.mainloop()