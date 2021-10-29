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
    
def WindowCliente():  
    nuevocliente = tk.Tk()
    nuevocliente.title("Nuevo Cliente")
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
#Conexion a base de datos

'''cursor = conexion.cursor()
cursor.execute("select * from persona;")
personas = cursor.fetchall()
for persona in personas:
    print(persona)    
cursor.commit()
cursor.close()

conexion.close()'''

'''def cant():
    mywindow2 = tk.Tk()
    mywindow2.title("Ingreso Cliente Nuevo")
    mywindow2.resizable(1, 1)

    def cant_changed(event):
        msg = f'You selected {cont_cant_cb.get()}!'
        showinfo(title='Result', message=msg)

    # month of year
    cantidad = ('1', '2', '3', '4', '5', '6',
            '7', '8', '9', '10', '11', '12')

    label = tk.Label(mywindow2, text="Cuantos concentradores").grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)

    # create a combobox
    selected_cantidad = tk.StringVar()

    cont_cant_cb = ttk.Combobox(mywindow2, textvariable=selected_cantidad, width = 2)
    cont_cant_cb.grid(column=1, row=6, sticky=tk.SW, padx=5, pady=5)
    cont_cant_cb['values'] = cantidad
    cont_cant_cb['state'] = 'readonly'  # normal

    cont_cant_cb.bind('<<ComboboxSelected>>', cant_changed)


    label = tk.Label(mywindow2, text="Cuantos concentradores").grid(row=7, column=1, sticky=tk.W, padx=5, pady=5)

    control_cant_cb = ttk.Combobox(mywindow2, textvariable=selected_cantidad, width = 2)
    control_cant_cb.grid(column=1, row=8, sticky=tk.SW,padx=5, pady=5)
    control_cant_cb['values'] = cantidad
    control_cant_cb['state'] = 'readonly'  # normal

    control_cant_cb.bind('<<ComboboxSelected>>', cant_changed)

    mywindow2.mainloop()'''