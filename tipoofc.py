import tkinter as tk
from tkinter import ttk
from tkinter.constants import LAST
import pyodbc
from configuracion import server, bd, usuario, contrasena
from version import versionWindow

conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)

def tipoWindow(id, nombre, empresa, cargo, phone):

    def tipo_changed(event):
        cursor = conexion.cursor()
        consulta="insert into oferta(tipo) values (?);"
        cursor.execute(consulta, tipo_cb.get())
        cursor.commit()
        cursor.close()
    tipo= tk.Tk()
    tipo.title("Tipo de Oferta")
    tipo.resizable(1, 1)
    tipo.minsize(230,80)
    selected_tipo = tk.StringVar()
    tipoofc = ('NUEVOS SUMINISTROS', 'REPUESTOS')
    cursor = conexion.cursor()
    consulta = "update persona set ntelefono = ? , nombre = ?, cargo = ?, empresa = ? where id = ?;"
    cursor.execute(consulta, phone, nombre, cargo, empresa, id)
    cursor.commit()
    cursor.close()

    tipo_cb = ttk.Combobox(tipo, textvariable=selected_tipo,width="18")
    tipo_cb['values'] = tipoofc
    tipo_cb['state'] = 'readonly'  # normal
    tipo_cb.grid(row=1, column=2)
    tipo_cb.bind('<<ComboboxSelected>>', tipo_changed)
    
    tk.Label(tipo, text="Tipo de oferta").grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
    botone = ttk.Button(
        tipo, 
        text="Enviar", 
        command=lambda:versionWindow(tipo)
    )
    botone.grid(column=1, row=2, sticky=tk.SW, padx=5, pady=5)