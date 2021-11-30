import tkinter as tk
from tkinter import Label, PhotoImage, ttk
from actualizarinfo import ActualizarInfo
from nuevocliente import WindowCliente
from validacion import validacion

root = tk.Tk()
root.title("Nueva Oferta Economica")
root.columnconfigure(1, weight=3)

root.minsize(430, 100)

botonNC = ttk.Button(
    root, 
    text="Nuevo Cliente", 
    command=lambda:WindowCliente()
)

botonNC.grid(column=1, row=1, sticky=tk.NW, padx=5, pady=5)
botonAC = ttk.Button(
    root, 
    text="Actualizar Información", 
    command=lambda:ActualizarInfo()
)

botonAC.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

botonAP = ttk.Button(
    root, 
    text="Actualizar Precios", 
    command=lambda:validacion()
)

botonAP.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

botonc = ttk.Button(
    root, 
    text="Salir", 
    command=lambda:root.quit()
)
botonc.grid(column=2, row=4, sticky=tk.SE, padx=5, pady=5)


imagen=PhotoImage(file=r"Imagenes\logo.png")
fondo =Label(root,image=imagen).place(x=140,y=30)

root.mainloop()
