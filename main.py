import tkinter as tk
from tkinter import ttk
from nuevocliente import WindowCliente
from cantidades import openNewWindow
from actualizarcliente import ActualizarCliente

root = tk.Tk()
root.title("Nueva Oferta Economica")

root.minsize(300, 100)

botonNC = ttk.Button(
    root, 
    text="Nuevo Cliente", 
    command=lambda:WindowCliente()
)
botonNC.grid(column=1, row=1, sticky=tk.NW, padx=5, pady=5)
botonAC = ttk.Button(
    root, 
    text="Actualizar Cliente", 
    command=lambda:ActualizarCliente()
)
botonAC.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
botonNO = ttk.Button(
    root, 
    text="Creación Oferta", 
    command=lambda:openNewWindow()
)
botonNO.grid(column=1, row=3, sticky=tk.SW ,padx=5, pady=5)

botonc = ttk.Button(
    root, 
    text="Salir", 
    command=lambda:root.quit()
)
botonc.grid(column=2, row=4, sticky=tk.SE)
root.mainloop()