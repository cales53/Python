import tkinter as tk
from tkinter import Entry, StringVar, ttk
from tkinter.constants import CHAR, NS
from typing import Text
import pyodbc
from configuracion import server, bd, usuario, contrasena
from precios import ActualizarPrecios

conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)

def validacion():
    validacion = tk.Tk()
    validacion.title("Login")
    #precios.resizable(1, 1)
    validacion.minsize(150,100)
    validacion.columnconfigure(1, weight=2)


    tk.Label(validacion, text="Usuario").grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(validacion, text="Contraseña").grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

    # Crear las cajas de ingreso
    cusuario = tk.Entry(validacion)
    ccontrasena = tk.Entry(validacion, show="*")
    cusuario.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
    ccontrasena.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)

    botonSI = ttk.Button(
    validacion, 
    text="Login", 
    command=lambda:ActualizarPrecios()
    )

    botonSI.grid(column=1, row=9, sticky=tk.SW ,padx=5, pady=5)