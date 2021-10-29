import tkinter as tk
from tkinter import Entry, StringVar, ttk
from tkinter.constants import CHAR, NS
from typing import Text
import pyodbc
from configuracion import server, bd, usuario, contrasena
from cantidades import openNewWindow
from tkinter.messagebox import showinfo

#from tkinter.messagebox import showinfo
conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)
    
def ActualizarCliente():  
    nuevocliente = tk.Tk()
    nuevocliente.title("Actualizar Cliente")
    nuevocliente.resizable(1, 1)
    nuevocliente.minsize(300,100)

    def month_changed(event):
        pass

    # month of year
    nombres = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    empresas = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    selected_nombre = tk.StringVar()
    selected_empresa = tk.StringVar()

    nombre_cb = ttk.Combobox(nuevocliente, textvariable=selected_nombre)
    nombre_cb['values'] = nombres
    nombre_cb['state'] = 'readonly'  # normal
    nombre_cb.grid(row=1, column=2)
    nombre_cb.bind('<<ComboboxSelected>>', month_changed)

    empresa_cb = ttk.Combobox(nuevocliente, textvariable=selected_empresa)
    empresa_cb['values'] = empresas
    empresa_cb['state'] = 'readonly'  # normal
    empresa_cb.grid(row=2, column=2)
    nombre_cb.bind('<<ComboboxSelected>>', month_changed)

    tk.Label(nuevocliente, text="Nombre del cliente").grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(nuevocliente, text="Nombre de la empresa").grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(nuevocliente, text="Cargo").grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(nuevocliente, text="Celular").grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)
    botone = ttk.Button(
        nuevocliente, 
        text="Enviar", 
        #command=lambda:
    )
    botone.grid(column=1, row=9, sticky=tk.SW, padx=5, pady=5)