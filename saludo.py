# el único cambio fué agregar esto
# este es otro cambió de prueba
# este es un tercer cambio
import tkinter as tk
from tkinter import messagebox

def saludar():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    mensaje = f"¡Bienvenido, {nombre} {apellido}!"
    messagebox.showinfo("Saludo", mensaje)

root = tk.Tk()
root.title("Programa de Bienvenida")

tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Apellido:").grid(row=1, column=0, padx=10, pady=5)
entry_apellido = tk.Entry(root)
entry_apellido.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Saludar", command=saludar).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
