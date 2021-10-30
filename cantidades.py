import tkinter as tk
from tkinter import Entry, StringVar, ttk
import pyodbc
from configuracion import server, bd, usuario, contrasena

conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)

def openNewWindow():
    windowscomprobacion= tk.Tk()
    windowscomprobacion.title("Cantidades")
    windowscomprobacion.resizable(1, 1)
    windowscomprobacion.minsize(200,100)

    cantidades = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    def cantidades_changed(event):
        pass

    tk.Label(windowscomprobacion, text="Concentradores").grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(windowscomprobacion, text="Tarjetas de Control").grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(windowscomprobacion, text="Tarjetas de interconexión").grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(windowscomprobacion, text="Microcontroladores").grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(windowscomprobacion, text="Fuentes").grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(windowscomprobacion, text="UPCs").grid(row=6, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(windowscomprobacion, text="Modem Celular").grid(row=7, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(windowscomprobacion, text="Modem RF").grid(row=8, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(windowscomprobacion, text="Displays").grid(row=9, column=1, sticky=tk.W, padx=5, pady=5)
    
    selected_concentradores = tk.StringVar()
    selected_control = tk.StringVar()
    selected_intercon = tk.StringVar()
    selected_micros = tk.StringVar()
    selected_fuentes = tk.StringVar()
    selected_upcs = tk.StringVar()
    selected_mdlcell = tk.StringVar()
    selected_mdlrf = tk.StringVar()
    selected_dis = tk.StringVar()


    concentrador_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_concentradores,width="2")
    concentrador_cb['values'] = cantidades
    concentrador_cb['state'] = 'readonly'  # normal
    concentrador_cb.grid(row=1, column=2)
    concentrador_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    concentrador_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_control,width="2")
    concentrador_cb['values'] = cantidades
    concentrador_cb['state'] = 'readonly'  # normal
    concentrador_cb.grid(row=2, column=2)
    concentrador_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    concentrador_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_intercon,width="2")
    concentrador_cb['values'] = cantidades
    concentrador_cb['state'] = 'readonly'  # normal
    concentrador_cb.grid(row=3, column=2)
    concentrador_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    concentrador_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_micros,width="2")
    concentrador_cb['values'] = cantidades
    concentrador_cb['state'] = 'readonly'  # normal
    concentrador_cb.grid(row=4, column=2)
    concentrador_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    concentrador_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_fuentes,width="2")
    concentrador_cb['values'] = cantidades
    concentrador_cb['state'] = 'readonly'  # normal
    concentrador_cb.grid(row=5, column=2)
    concentrador_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    concentrador_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_upcs,width="2")
    concentrador_cb['values'] = cantidades
    concentrador_cb['state'] = 'readonly'  # normal
    concentrador_cb.grid(row=6, column=2)
    concentrador_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    concentrador_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_mdlcell,width="2")
    concentrador_cb['values'] = cantidades
    concentrador_cb['state'] = 'readonly'  # normal
    concentrador_cb.grid(row=7, column=2)
    concentrador_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    concentrador_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_mdlrf,width="2")
    concentrador_cb['values'] = cantidades
    concentrador_cb['state'] = 'readonly'  # normal
    concentrador_cb.grid(row=8, column=2)
    concentrador_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    concentrador_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_dis,width="2")
    concentrador_cb['values'] = cantidades
    concentrador_cb['state'] = 'readonly'  # normal
    concentrador_cb.grid(row=9, column=2)
    concentrador_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    botone = ttk.Button(
        windowscomprobacion, 
        text="Enviar", 
        #command=lambda:
    )
    botone.grid(column=1, row=10, sticky=tk.SW, padx=5, pady=5)

    
