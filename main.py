import tkinter as tk
from tkinter import Label, PhotoImage, ttk
from nuevocliente import WindowCliente
from actualizarcliente import ActualizarCliente

root = tk.Tk()
root.title("Nueva Oferta Economica")
root.columnconfigure(1, weight=3)

root.minsize(410, 100)

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


botonc = ttk.Button(
    root, 
    text="Salir", 
    command=lambda:root.quit()
)
botonc.grid(column=2, row=3, sticky=tk.SE, padx=5, pady=5)

#root.geometry("275x57")
imagen=PhotoImage(file=r"D:\User\Documentos\Python\Imagenes\logo.png")
#imagen
#imagen.resizable(180,37.31)
#imagen=PhotoImage(file=open("D:\User\Documentos\Python\Imagenes"))
fondo =Label(root,image=imagen).place(x=120,y=10)

root.mainloop()