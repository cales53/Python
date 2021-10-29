import tkinter as tk
from tkinter import Entry, StringVar, ttk
from tkinter.constants import CHAR
from typing import Text
import pyodbc
from configuracion import server, bd, usuario, contrasena
from cantidades import openNewWindow

#from tkinter.messagebox import showinfo
conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)

def consulta(cnombre,cempresa,ccargo,cphone):
    cursor = conexion.cursor()
    consulta = "Insert into persona(nombre,ntelefono,empresa,cargo) values (?,?,?,?)"
    cursor.execute(consulta,cnombre,cphone,cempresa,ccargo)
    cursor.execute("select * from persona;")
    personas = cursor.fetchall()
    for persona in personas:
        print(persona)    
    cursor.commit()
    cursor.close()
    # creacion de una segunda ventana para dar continuacion al ingreso de cantidades
    openNewWindow()
    
def ActualizarCliente():  
    nuevocliente = tk.Tk()
    nuevocliente.title("Actualizar Cliente")
    nuevocliente.resizable(1, 1)

    tk.Label(nuevocliente, text="Nombre del cliente").grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(nuevocliente, text="Nombre de la empresa").grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(nuevocliente, text="Cargo").grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(nuevocliente, text="Celular").grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

    # Crear las cajas de ingreso
    cnombre = tk.Entry(nuevocliente)
    cempresa = tk.Entry(nuevocliente)
    ccargo = tk.Entry(nuevocliente)
    cphone = tk.Entry(nuevocliente)
    # cajones en grid
    cnombre.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
    cempresa.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)
    ccargo.grid(row=3, column=2, sticky=tk.W, padx=5, pady=5)
    cphone.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)

    botone = ttk.Button(
        nuevocliente, 
        text="Enviar", 
        command=lambda:consulta(cnombre.get(),cempresa.get(),ccargo.get(),cphone.get())
    )
    botone.grid(column=1, row=9, sticky=tk.SW, padx=5, pady=5)