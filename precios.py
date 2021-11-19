import tkinter as tk
from tkinter import ttk
import pyodbc
from configuracion import server, bd, usuario, contrasena

conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)

def ActualizarPrecios():
    precios = tk.Tk()
    precios.title("Actualizar Precios")
    precios.resizable(1, 1)
    precios.minsize(300,100)
    precios.columnconfigure(1, weight=3)

    tk.Label(precios, text="Concentradores").grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(precios, text="Tarjetas de Control").grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(precios, text="Tarjetas de interconexión").grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(precios, text="Microcontroladores").grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(precios, text="Fuentes").grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(precios, text="UPCs").grid(row=6, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(precios, text="Modem Celular").grid(row=7, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(precios, text="Modem RF").grid(row=8, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(precios, text="Displays").grid(row=9, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(precios, text="Modulo de 5 AMP").grid(row=10, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(precios, text="Modulo de 60 AMP").grid(row=11, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(precios, text="Modulo de 100 AMP").grid(row=12, column=1, sticky=tk.W, padx=5, pady=5)

        # Crear las cajas de ingreso
    cconcetrador = tk.Entry(precios)
    ccontrol = tk.Entry(precios)
    cintercon = tk.Entry(precios)
    cmicro = tk.Entry(precios)
    cfuente = tk.Entry(precios)
    cupc = tk.Entry(precios)
    cmdlcel = tk.Entry(precios)
    ccdmlrf = tk.Entry(precios)
    cdis = tk.Entry(precios)
    cmdl5a = tk.Entry(precios)
    cmdl60a = tk.Entry(precios)
    cmdl100a = tk.Entry(precios)


    cconcetrador.insert(10, "2.000.000")
    ccontrol.insert(10, "608.000")
    cintercon.insert(10, "170.000")
    cmicro.insert(10, "238.000")
    cfuente.insert(10, "84.000")
    cupc.insert(10, "1.800.000")
    cmdlcel.insert(10, "922.000")
    ccdmlrf.insert(10, "380.000")
    cdis.insert(10, "172.000")
    cmdl5a.insert(10, "99.000")
    cmdl60a.insert(10, "117.000")
    cmdl100a.insert(10, "135.000")

    # cajones en grid
    cconcetrador.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
    ccontrol.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)
    cintercon.grid(row=3, column=2, sticky=tk.W, padx=5, pady=5)
    cmicro.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)
    cfuente.grid(row=5, column=2, sticky=tk.W, padx=5, pady=5)
    cupc.grid(row=6, column=2, sticky=tk.W, padx=5, pady=5)
    cmdlcel.grid(row=7, column=2, sticky=tk.W, padx=5, pady=5)
    ccdmlrf.grid(row=8, column=2, sticky=tk.W, padx=5, pady=5)
    cdis.grid(row=9, column=2, sticky=tk.W, padx=5, pady=5)
    cmdl5a.grid(row=10, column=2, sticky=tk.W, padx=5, pady=5)
    cmdl60a.grid(row=11, column=2, sticky=tk.W, padx=5, pady=5)
    cmdl100a.grid(row=12, column=2, sticky=tk.W, padx=5, pady=5)


    botonSI = ttk.Button(
    precios, 
    text="Enviar", 
    command=lambda:ActualizarPrecios()
    )

    botonSI.grid(column=1, row=13, sticky=tk.SW ,padx=5, pady=5)