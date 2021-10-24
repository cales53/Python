import tkinter as tk
from tkinter import ttk
import pyodbc

mywindow = tk.Tk()
mywindow.title("Ingreso Cliente Nuevo")
mywindow.geometry("600x400")
mywindow.resizable(0, 0)

content = ttk.Frame(mywindow)
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

botone = tk.Button(mywindow, text="Enviar")
botone.place(x=30, y=350)
botonc = ttk.Button(text="Cancelar")
botonc.place(x=500, y=350)

tk.Label(mywindow, text="Nombre del cliente").grid(row=1, column=1)
tk.Label(mywindow, text="Nombre de la empresa").grid(row=2, column=1)

# Create the entry objects using master
cnombre = tk.Entry(mywindow)
cempresa = tk.Entry(mywindow)
 
# Pack them using grid
cnombre.grid(row=1, column=2)
cempresa.grid(row=2, column=2)

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