import tkinter as tk
from tkinter import messagebox, ttk
import random

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Asignación de memoria a los procesos")

ventana.memoria_total = 100
ventana.memoria_disponible = ventana.memoria_total

def generar_datos_automaticos():
    num_procesos = int(entrada_texto.get())
    if num_procesos < 1 or num_procesos > 10:
        messagebox.showerror("Error", "El número de procesos debe estar entre 1 y 10")
        return []
    if num_procesos > 10 or num_procesos < 1:
        messagebox.showerror("Error", "Ingrese un número válido")
        return []
    
    data = []
    
    for i in range(1, num_procesos + 1):
        memoria = random.randint(10, 90)
        tiempo = random.randint(1, 10)
        data.append((i, f"{memoria} MB", f"{tiempo} seg"))
    
    return data

def genera_procesos():
    for item in tree.get_children():
        tree.delete(item)
    
    datos_automaticos = generar_datos_automaticos()
    
    for row in datos_automaticos:
        tree.insert("", "end", values=row)



# Frame para entrada de datos
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=5)
tk.Label(frame_entrada, text="Número de procesos:").pack(side=tk.LEFT)
entrada_texto = tk.Entry(frame_entrada, width=5)
entrada_texto.pack(side=tk.LEFT, padx=5)
entrada_texto.insert(0, " 0")  # Valor por defecto

# Crear el widget Treeview
tree = ttk.Treeview(ventana, columns=("ID Tarea", "Memoria", "Tiempo"), show="headings")
tree.heading("ID Tarea", text="ID Proceso")
tree.heading("Memoria", text="Memoria (MB)")
tree.heading("Tiempo", text="Tiempo (seg)")
tree.column("ID Tarea", width=100, anchor=tk.CENTER)
tree.column("Memoria", width=100, anchor=tk.CENTER)
tree.column("Tiempo", width=100, anchor=tk.CENTER)
tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)


# Marco para que se dibuje la barra de memoria
frame_memoria = tk.Frame(ventana, padx=10, pady=5)
frame_memoria.pack(fill=tk.X)
        
tk.Label(frame_memoria, text="Memoria:").pack(side=tk.LEFT)
ventana.barra_memoria = ttk.Progressbar(frame_memoria, orient=tk.HORIZONTAL, 
                        length=300, mode='determinate',
                        maximum=ventana.memoria_total)
ventana.barra_memoria.pack(side=tk.LEFT, padx=5)
ventana.label_memoria = tk.Label(frame_memoria, text=f"{ventana.memoria_disponible}/{ventana.memoria_total} MB")
ventana.label_memoria.pack(side=tk.LEFT)

# Cuadro de texto para el mensaje final
cuadro_texto = tk.Text(ventana, height=3, width=50)
cuadro_texto.pack(pady=10)

# Marco para los botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# Crear los botones
boton_generar = tk.Button(
    frame_botones, 
    text="Generar Procesos", 
    command=genera_procesos, 
    activebackground="yellow"
)
boton_generar.pack(side=tk.LEFT, padx=5)

boton_iniciar = tk.Button(
    frame_botones, 
    text="Iniciar", 
    activebackground="olive"
)
boton_iniciar.pack(side=tk.LEFT, padx=5)

boton_finalizar = tk.Button(
    frame_botones, 
    text="Finalizar", 
    command=ventana.destroy, 
    activebackground="salmon"
)
boton_finalizar.pack(side=tk.LEFT, padx=5)

#inicializar
ventana.mainloop()