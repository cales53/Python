import tkinter as tk
from tkinter import Entry, StringVar, ttk
import pyodbc
from configuracion import server, bd, usuario, contrasena

conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)

def openNewWindow():
    windowscomprobacion= tk.Tk()
    windowscomprobacion.title("Cantidades")
    windowscomprobacion.resizable(1, 1)

    
