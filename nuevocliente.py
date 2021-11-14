import tkinter as tk
from tkinter import Entry, StringVar, ttk
from tkinter.constants import CHAR
from typing import Text
import pyodbc
from configuracion import server, bd, usuario, contrasena
from tipoofc import tipoWindow

#from tkinter.messagebox import showinfo
conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)

def consulta(cnombre,cempresa,ccargo,cphone):
    #clear de db donde nombre es null
    cursor = conexion.cursor()
    consulta = "delete from persona WHERE nombre = '';"
    cursor.execute(consulta)
    cursor.commit()
    cursor.close()

    cursor = conexion.cursor()
    consulta = "insert into persona(nombre,ntelefono,empresa,cargo) values (?,?,?,?);"
    cursor.execute(consulta,cnombre,cphone,cempresa,ccargo)
    cursor.commit()
    cursor.close()

    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM [dbo].[persona]")
    tuplei = cursor.fetchall()
    id = [_[0] for _ in tuplei]
    cursor.commit()
    cursor.close()
    print(len(tuplei)-1)
    
    # creacion de una segunda ventana para dar continuacion al ingreso de cantidades
    tipoWindow(id[len(tuplei)-1], cnombre,cempresa,ccargo,cphone)
    
def WindowCliente():  
    nuevocliente = tk.Tk()
    nuevocliente.title("Nuevo Cliente")
    nuevocliente.resizable(1, 1)
    nuevocliente.columnconfigure(1, weight=3)
    
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

    botonNO = ttk.Button(
    nuevocliente, 
    text="Creación Oferta", 
    command=lambda:consulta(cnombre.get(),cempresa.get(),ccargo.get(),cphone.get())
    )

    botonNO.grid(column=1, row=9, sticky=tk.SW ,padx=5, pady=5)
