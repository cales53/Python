import tkinter as tk
from tkinter import ttk
import pyodbc
from configuracion import server, bd, usuario, contrasena
from precios import ActualizarPrecios
from tkinter import messagebox
import time

conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)

def val(cusuario, ccontrasena,validacion):
    u = 0
    c = 0
    cursor = conexion.cursor()
    cursor.execute("SELECT username FROM [dbo].[validacion];")
    tupleuser = cursor.fetchall()
    cursor1 = conexion.cursor()
    cursor1.execute("SELECT pass FROM [dbo].[validacion];")
    tuplepass = cursor1.fetchall()
    for x in tupleuser: 
        usuario = ' '.join(x)
        if(cusuario == usuario):
            contrasena = ' '.join(tuplepass[tupleuser.index(x)])
            if(ccontrasena == contrasena):
                time.sleep(1)
                ActualizarPrecios(validacion)
            if(ccontrasena != contrasena):
                 c = c + 1
                 if(c == 1): 
                    time.sleep(1)
                    messagebox.showwarning("Advertencia", "Contraseña Erronea")
        if (cusuario != usuario):
            u = u + 1
            if(u == len(tupleuser)): 
                time.sleep(1)
                messagebox.showwarning("Advertencia", "Usuario Erroneo")
    cursor.commit()
    cursor.close()

def validacion():
    validacion = tk.Tk()
    validacion.title("Login")
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
    command=lambda:val(cusuario.get(), ccontrasena.get(),validacion)
    )

    botonSI.grid(column=1, row=9, sticky=tk.SW ,padx=5, pady=5)