import tkinter as tk
from tkinter import Entry, StringVar, ttk
from tkinter.constants import CHAR, NS, NUMERIC
from actualizarcliente import ActualizarCliente
from actualizarempresa import ActualizarEmpresa

def ActualizarInfo():
    actualizarWin = tk.Tk()
    actualizarWin.title("Actualizar Informacion")
    actualizarWin.resizable(1, 1)
    actualizarWin.columnconfigure(1, weight=3)
    actualizarWin.minsize(300,100)

    
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