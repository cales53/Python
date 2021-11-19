import tkinter as tk
from tkinter import ttk
import pyodbc
from configuracion import server, bd, usuario, contrasena

conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)

def openNewWindow():
    windowscomprobacion= tk.Tk()
    windowscomprobacion.title("Cantidades")
    windowscomprobacion.resizable(1, 1)
    windowscomprobacion.minsize(200,100)

    cantidades = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
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
    tk.Label(windowscomprobacion, text="Modulo de 5 AMP").grid(row=10, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(windowscomprobacion, text="Modulo de 60 AMP").grid(row=11, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(windowscomprobacion, text="Modulo de 100 AMP").grid(row=12, column=1, sticky=tk.W, padx=5, pady=5)
    
    selected_concentradores = tk.StringVar()
    selected_control = tk.StringVar()
    selected_intercon = tk.StringVar()
    selected_micros = tk.StringVar()
    selected_fuentes = tk.StringVar()
    selected_upcs = tk.StringVar()
    selected_mdlcell = tk.StringVar()
    selected_mdlrf = tk.StringVar()
    selected_dis = tk.StringVar()
    selected_mdl5a = tk.StringVar()
    selected_mdl60a = tk.StringVar()
    selected_mdl100a = tk.StringVar()

    concentrador_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_concentradores,width="2")
    concentrador_cb['values'] = cantidades
    concentrador_cb['state'] = 'readonly'  # normal
    concentrador_cb.grid(row=1, column=2)
    concentrador_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    control_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_control,width="2")
    control_cb['values'] = cantidades
    control_cb['state'] = 'readonly'  # normal
    control_cb.grid(row=2, column=2)
    control_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    intercon_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_intercon,width="2")
    intercon_cb['values'] = cantidades
    intercon_cb['state'] = 'readonly'  # normal
    intercon_cb.grid(row=3, column=2)
    intercon_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    micro_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_micros,width="2")
    micro_cb['values'] = cantidades
    micro_cb['state'] = 'readonly'  # normal
    micro_cb.grid(row=4, column=2)
    micro_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    fuente_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_fuentes,width="2")
    fuente_cb['values'] = cantidades
    fuente_cb['state'] = 'readonly'  # normal
    fuente_cb.grid(row=5, column=2)
    fuente_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    upc_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_upcs,width="2")
    upc_cb['values'] = cantidades
    upc_cb['state'] = 'readonly'  # normal
    upc_cb.grid(row=6, column=2)
    upc_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    cell_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_mdlcell,width="2")
    cell_cb['values'] = cantidades
    cell_cb['state'] = 'readonly'  # normal
    cell_cb.grid(row=7, column=2)
    cell_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    mdlrf_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_mdlrf,width="2")
    mdlrf_cb['values'] = cantidades
    mdlrf_cb['state'] = 'readonly'  # normal
    mdlrf_cb.grid(row=8, column=2)
    mdlrf_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    dis_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_dis,width="2")
    dis_cb['values'] = cantidades
    dis_cb['state'] = 'readonly'  # normal
    dis_cb.grid(row=9, column=2)
    dis_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    mdl5a_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_mdl5a,width="2")
    mdl5a_cb['values'] = cantidades
    mdl5a_cb['state'] = 'readonly'  # normal
    mdl5a_cb.grid(row=10, column=2)
    mdl5a_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    mdl60a_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_mdl60a,width="2")
    mdl60a_cb['values'] = cantidades
    mdl60a_cb['state'] = 'readonly'  # normal
    mdl60a_cb.grid(row=11, column=2)
    mdl60a_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    mdl100a_cb = ttk.Combobox(windowscomprobacion, textvariable=selected_mdl100a,width="2")
    mdl100a_cb['values'] = cantidades
    mdl100a_cb['state'] = 'readonly'  # normal
    mdl100a_cb.grid(row=12, column=2)
    mdl100a_cb.bind('<<ComboboxSelected>>', cantidades_changed)

    botone = ttk.Button(
        windowscomprobacion, 
        text="Enviar", 
        #command=lambda:
    )
    botone.grid(column=1, row=13, sticky=tk.SW, padx=5, pady=5)

    
