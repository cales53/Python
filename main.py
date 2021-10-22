import tkinter as tk
import pyodbc

mywindow = tk.Tk()
mywindow.title("Python + Tkinter GUI")
mywindow.geometry("600x400")
mywindow.mainloop()

#conexion a base de datos

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