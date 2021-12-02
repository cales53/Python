import tkinter as tk
from tkinter import ttk
import pyodbc
from configuracion import server, bd, usuario, contrasena
from cantidades import openNewWindow
conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)

def versionWindow():
    cursor = conexion.cursor()
    consulta1="select MAX(id) from oferta;"
    cursor.execute(consulta1)
    tuplei = cursor.fetchall()
    ids = [_[0] for _ in tuplei]
    cursor.close()
    def version_changed(event):
        cursor = conexion.cursor()
        consulta = "update oferta set version = ? where id = ?;"
        cursor.execute(consulta, version_cb.get(), ids[0])
        cursor.commit()   
        cursor.close()
    versionwin= tk.Tk()
    versionwin.title("Versión")
    versionwin.resizable(1, 1)
    versionwin.minsize(150,80)
    selected_tipo = tk.StringVar()
    version = ('V3', 'V4')
    version_cb = ttk.Combobox(versionwin, textvariable=selected_tipo,width="5")
    version_cb['values'] = version
    version_cb['state'] = 'readonly'  # normal
    version_cb.grid(row=1, column=2)
    version_cb.bind('<<ComboboxSelected>>', version_changed)
    
    tk.Label(versionwin, text="Versión").grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

    botone = ttk.Button(
        versionwin, 
        text="Enviar", 
        command=lambda:openNewWindow()
    )
    botone.grid(column=1, row=2, sticky=tk.SW, padx=5, pady=5)