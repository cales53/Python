import tkinter as tk
from tkinter import Entry, StringVar, ttk
import pyodbc
from configuracion import server, bd, usuario, contrasena
from cantidades import openNewWindow

def tipoWindow():
    tipo= tk.Tk()
    tipo.title("Cantidades")
    tipo.resizable(1, 1)
    tipo.minsize(250,100)

    selected_tipo = tk.StringVar()
    cantidades = ('NUEVOS SUMINISTROS', 'REPUESTOS')

    tipo_cb = ttk.Combobox(tipo, textvariable=selected_tipo,width="18")
    tipo_cb['values'] = cantidades
    tipo_cb['state'] = 'readonly'  # normal
    tipo_cb.grid(row=1, column=2)
    tipo_cb.bind('<<ComboboxSelected>>', tipo_changed)
    
    tk.Label(tipo, text="Tipo de oferta").grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

    botone = ttk.Button(
        tipo, 
        text="Enviar", 
        command=lambda:openNewWindow()
        #command=lambda:
    )
    botone.grid(column=1, row=2, sticky=tk.SW, padx=5, pady=5)

def tipo_changed(event):
    pass