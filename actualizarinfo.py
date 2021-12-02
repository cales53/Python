import tkinter as tk
from tkinter import ttk
from actualizarcliente import ActualizarCliente
from actualizarempresa import ActualizarEmpresa

def ActualizarInfo():
    actualizarWin = tk.Tk()
    actualizarWin.title("Actualizar Informacion")
    actualizarWin.resizable(1, 1)
    actualizarWin.columnconfigure(1, weight=3)
    actualizarWin.minsize(300,80)
    actualizarWin.maxsize(300,80)

    
    botonNC = ttk.Button(
        actualizarWin, 
        text="Actualizar Cliente", 
        command=lambda:ActualizarCliente()
    )

    botonNC.grid(column=1, row=1, sticky=tk.W, padx=20, pady=20)
    botonAC = ttk.Button(
        actualizarWin, 
        text="Actualizar Empresa", 
        command=lambda:ActualizarEmpresa()
    )

    botonAC.grid(column=2, row=1, padx=20, pady=20)