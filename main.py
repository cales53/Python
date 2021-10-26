import tkinter as tk
from tkinter import ttk
import pyodbc
from tkinter.messagebox import showinfo

mywindow = tk.Tk()
mywindow.title("Ingreso Cliente Nuevo")
mywindow.resizable(1, 1)

botone = ttk.Button(mywindow, text="Enviar")
botone.grid(column=1, row=9, sticky=tk.SW, padx=5, pady=5)
botonc = ttk.Button(text="Cancelar")
botonc.grid(column=2, row=9, sticky=tk.SE, padx=5, pady=5)

tk.Label(mywindow, text="Nombre del cliente").grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
tk.Label(mywindow, text="Nombre de la empresa").grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
tk.Label(mywindow, text="Cargo").grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
tk.Label(mywindow, text="Celular").grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

# Crear las cajas de ingreso
cnombre = tk.Entry(mywindow)
cempresa = tk.Entry(mywindow)
ccargo = tk.Entry(mywindow)
cphone = tk.Entry(mywindow)
 
# cajones en grid
cnombre.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
cempresa.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)
ccargo.grid(row=3, column=2, sticky=tk.W, padx=5, pady=5)
cphone.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)

def cant_changed(event):
    msg = f'You selected {cont_cant_cb.get()}!'
    showinfo(title='Result', message=msg)

# month of year
cantidad = ('1', '2', '3', '4', '5', '6',
        '7', '8', '9', '10', '11', '12')

label = tk.Label(mywindow, text="Cuantos concentradores").grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)

# create a combobox
selected_cantidad = tk.StringVar()

cont_cant_cb = ttk.Combobox(mywindow, textvariable=selected_cantidad, width = 2)
cont_cant_cb.grid(column=1, row=6, sticky=tk.SW, padx=5, pady=5)
cont_cant_cb['values'] = cantidad
cont_cant_cb['state'] = 'readonly'  # normal

cont_cant_cb.bind('<<ComboboxSelected>>', cant_changed)


label = tk.Label(mywindow, text="Cuantos concentradores").grid(row=7, column=1, sticky=tk.W, padx=5, pady=5)

control_cant_cb = ttk.Combobox(mywindow, textvariable=selected_cantidad, width = 2)
control_cant_cb.grid(column=1, row=8, sticky=tk.SW,padx=5, pady=5)
control_cant_cb['values'] = cantidad
control_cant_cb['state'] = 'readonly'  # normal

control_cant_cb.bind('<<ComboboxSelected>>', cant_changed)

mywindow.mainloop()

#Conexion a base de datos

server = "192.168.1.89"
bd = "Clientes"
usuario = "usuario"
contrasena = "Manager21"
try:
    conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)
    print("Conexion exitosa")
except:
    print("Conexion fallida")


cursor = conexion.cursor()
cursor.execute("select * from persona;")
personas = cursor.fetchall()
for persona in personas:
    print(persona)    
cursor.commit()
cursor.close()

conexion.close()