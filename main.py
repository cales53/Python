import tkinter as tk
from tkinter import ttk
import pyodbc

server = "192.168.1.89"
bd = "Clientes"
usuario = "usuario"
contrasena = "Manager21"
try:
    conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)
    print("Conexion exitosa")
except:
    print("Conexion fallida")

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

mywindow.mainloop()

#Conexion a base de datos

cursor = conexion.cursor()
cursor.execute("select * from persona;")
personas = cursor.fetchall()
for persona in personas:
    print(persona)    
cursor.commit()
cursor.close()

conexion.close()