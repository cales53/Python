import tkinter as tk
from tkinter import ttk
import pyodbc

mywindow = tk.Tk()
mywindow.title("Ingreso Cliente Nuevo")
mywindow.resizable(1, 1)

content = ttk.Frame(mywindow)
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

botone = ttk.Button(mywindow, text="Enviar")
botone.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)
botonc = ttk.Button(text="Cancelar")
botonc.grid(column=2, row=3, sticky=tk.E, padx=5, pady=5)

tk.Label(mywindow, text="Nombre del cliente").grid(row=1, column=1, sticky=tk.SW, padx=5, pady=5)
tk.Label(mywindow, text="Nombre de la empresa").grid(row=2, column=1, sticky=tk.SE, padx=5, pady=5)

# Create the entry objects using master
cnombre = tk.Entry(mywindow)
cempresa = tk.Entry(mywindow)
 
# Pack them using grid
cnombre.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
cempresa.grid(row=2, column=2, sticky=tk.E, padx=5, pady=5)

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