import tkinter as tk
from tkinter import ttk
import pyodbc
from configuracion import server, bd, usuario, contrasena
from tkinter import messagebox

conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)


def actualizarv(concentrador, control, intercon, micro, fuente, upc, cel, rf, dis, mdl5a, mdl60a, mdl100a):
    cursor = conexion.cursor()
    consulta = "update precios set [valor unitario] = ? where producto = ?;"
    cursor.execute(consulta, concentrador, 'concentrador')

    consulta = "update precios set [valor unitario] = ? where producto = ?;"
    cursor.execute(consulta, control, 'control')

    consulta = "update precios set [valor unitario] = ? where producto = ?;"
    cursor.execute(consulta, intercon, 'intercon')

    consulta = "update precios set [valor unitario] = ? where producto = ?;"
    cursor.execute(consulta, micro, 'micro')

    consulta = "update precios set [valor unitario] = ? where producto = ?;"
    cursor.execute(consulta, fuente, 'fuente')
    
    consulta = "update precios set [valor unitario] = ? where producto = ?;"
    cursor.execute(consulta, upc, 'upc')

    consulta = "update precios set [valor unitario] = ? where producto = ?;"
    cursor.execute(consulta, cel, 'cel')

    consulta = "update precios set [valor unitario] = ? where producto = ?;"
    cursor.execute(consulta, rf, 'rf')

    consulta = "update precios set [valor unitario] = ? where producto = ?;"
    cursor.execute(consulta, dis, 'display')

    consulta = "update precios set [valor unitario] = ? where producto = ?;"
    cursor.execute(consulta, mdl5a, 'mdl5a')

    consulta = "update precios set [valor unitario] = ? where producto = ?;"
    cursor.execute(consulta, mdl60a, 'mdl60a')

    consulta = "update precios set [valor unitario] = ? where producto = ?;"
    cursor.execute(consulta, mdl100a, 'mdl100a')

    cursor.commit()
    cursor.close()
    messagebox.showwarning("Novedad", "Información Actualizada")
    

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
    cconcentrador = tk.Entry(precios)
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

    cconcentrador.delete(0, tk.END)
    ccontrol.delete(0, tk.END)
    cintercon.delete(0, tk.END)
    cmicro.delete(0, tk.END)
    cfuente.delete(0, tk.END)
    cupc.delete(0, tk.END)
    cmdlcel.delete(0, tk.END)
    ccdmlrf.delete(0, tk.END)
    cdis.delete(0, tk.END)
    cmdl5a.delete(0, tk.END)
    cmdl60a.delete(0, tk.END)
    cmdl100a.delete(0, tk.END)

    cursor = conexion.cursor()

    cursor.execute("SELECT [valor unitario] FROM [dbo].[precios] WHERE producto = 'concentrador';")
    tupleve = cursor.fetchall()
    vconcentrador = [_[0] for _ in tupleve]
    cconcentrador.insert(10, int(vconcentrador[0]))
    
    cursor.execute("SELECT [valor unitario] FROM [dbo].[precios] WHERE producto = 'control';")
    tuplevcon = cursor.fetchall()
    vcontrol = [_[0] for _ in tuplevcon]
    ccontrol.insert(10, int(vcontrol[0]))

    cursor.execute("SELECT [valor unitario] FROM [dbo].[precios] WHERE producto = 'intercon';")
    tuplevintercon = cursor.fetchall()
    vintercon = [_[0] for _ in tuplevintercon]
    cintercon.insert(10, int(vintercon[0]))

    cursor.execute("SELECT [valor unitario] FROM [dbo].[precios] WHERE producto = 'micro';")
    tuplevmicro = cursor.fetchall()
    vmicro = [_[0] for _ in tuplevmicro]
    cmicro.insert(10, int(vmicro[0]))

    cursor.execute("SELECT [valor unitario] FROM [dbo].[precios] WHERE producto = 'fuente';")
    tuplevfuente = cursor.fetchall()
    vfuente = [_[0] for _ in tuplevfuente]
    cfuente.insert(10, int(vfuente[0]))

    cursor.execute("SELECT [valor unitario] FROM [dbo].[precios] WHERE producto = 'upc';")
    tuplevupc = cursor.fetchall()
    vupc = [_[0] for _ in tuplevupc]
    cupc.insert(10, int(vupc[0]))

    cursor.execute("SELECT [valor unitario] FROM [dbo].[precios] WHERE producto = 'cel';")
    tuplevcel = cursor.fetchall()
    vcel = [_[0] for _ in tuplevcel]
    cmdlcel.insert(10, int(vcel[0]))

    cursor.execute("SELECT [valor unitario] FROM [dbo].[precios] WHERE producto = 'rf';")
    tuplevrf = cursor.fetchall()
    vrf = [_[0] for _ in tuplevrf]
    ccdmlrf.insert(10, int(vrf[0]))

    cursor.execute("SELECT [valor unitario] FROM [dbo].[precios] WHERE producto = 'display';")
    tuplevdis = cursor.fetchall()
    vdis = [_[0] for _ in tuplevdis]
    cdis.insert(10, int(vdis[0]))

    cursor.execute("SELECT [valor unitario] FROM [dbo].[precios] WHERE producto = 'mdl5a';")
    tuplev5a = cursor.fetchall()
    vmdl5a = [_[0] for _ in tuplev5a]
    cmdl5a.insert(10, int(vmdl5a[0]))

    cursor.execute("SELECT [valor unitario] FROM [dbo].[precios] WHERE producto = 'mdl60a';")
    tuplevmdl60a = cursor.fetchall()
    vmdl60a = [_[0] for _ in tuplevmdl60a]
    cmdl60a.insert(10, int(vmdl60a[0]))

    cursor.execute("SELECT [valor unitario] FROM [dbo].[precios] WHERE producto = 'mdl100a';")
    tuplevmdl100a = cursor.fetchall()
    vmdl100a = [_[0] for _ in tuplevmdl100a]
    cmdl100a.insert(10, int(vmdl100a[0]))

    cursor.close()

    # cajones en grid
    cconcentrador.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
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
    command=lambda:actualizarv(cconcentrador.get(), ccontrol.get(), cintercon.get(), cmicro.get(), cfuente.get(), cupc.get(), cmdlcel.get(), ccdmlrf.get(), cdis.get(), cmdl5a.get(), cmdl60a.get(), cmdl100a.get())
    )

    botonSI.grid(column=1, row=13, sticky=tk.SW ,padx=5, pady=5)
