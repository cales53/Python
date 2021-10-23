import tkinter as tk
from tkinter import ttk
import pyodbc

mywindow = tk.Tk()
mywindow.title("Ingreso Cliente Nuevo")
mywindow.geometry("600x400")

content = ttk.Frame(mywindow)
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)


etiqueta_nombre = ttk.Label(text="Nombre del cliente")
etiqueta_nombre.place(x=30, y=15)
caja_nombre = ttk.Entry()
caja_nombre.place(x=180, y=15, width=250)
etiqueta_empresa = ttk.Label(text="Nombre de la empresa")
etiqueta_empresa.place(x=30, y=40)
caja_empresa = ttk.Entry()
caja_empresa.place(x=180, y=40, width=250)

boton = ttk.Button(text="Enviar")
boton.place(x=30, y=350)
boton = ttk.Button(text="Cancelar")
boton.place(x=500, y=350)

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