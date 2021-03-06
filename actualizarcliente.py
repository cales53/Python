import tkinter as tk
from tkinter import ttk
import pyodbc
from configuracion import server, bd, usuario, contrasena
from tipoofc import tipoWindow

#from tkinter.messagebox import showinfo
conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)
    
def ActualizarCliente():  
    nuevocliente = tk.Tk()
    nuevocliente.title("Actualizar Cliente")
    nuevocliente.resizable(1, 1)
    nuevocliente.columnconfigure(1, weight=3)
    nuevocliente.minsize(300,100)
    nuevocliente.maxsize(300,160)

    selected_nombre = tk.StringVar()

    cargo_en = tk.Entry(nuevocliente)
    phone_en = tk.Entry(nuevocliente)
    empresa_en = tk.Entry(nuevocliente)

    cargo_en.grid(row=3, column=2, sticky=tk.W, padx=5, pady=5)
    phone_en.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)
    empresa_en.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)

    def nombre_changed(event):
        
        cargo_en.delete(0, tk.END)
        phone_en.delete(0, tk.END)
        empresa_en.delete(0, tk.END)

        #Clear de db donde nombre es null
        cursor = conexion.cursor()
        
        consulta = "delete from persona WHERE nombre = '';"
        cursor.execute(consulta)
        cursor.commit()

        cursor.execute("SELECT cargo FROM [dbo].[persona]")
        tuplec = cursor.fetchall()
        cargos = [_[0] for _ in tuplec]
        cursor.commit()
        cursor.execute("SELECT ntelefono FROM [dbo].[persona]")
        tuplet = cursor.fetchall()
        phones = [_[0] for _ in tuplet]
        cursor.commit()
        cursor.execute("SELECT empresa FROM [dbo].[persona]")
        tuplee = cursor.fetchall()
        companies = [_[0] for _ in tuplee]
        cursor.commit()
        cursor.execute("SELECT id FROM [dbo].[persona]")
        cursor.commit()

        cargo_en.insert(10, cargos[nombre_cb.current()])
        phone_en.insert(10, phones[nombre_cb.current()])
        empresa_en.insert(10, companies[nombre_cb.current()])

        cursor.close()

    cursor = conexion.cursor()
    cursor.execute("SELECT nombre FROM [dbo].[persona]")
    tuplen = cursor.fetchall()
    nombres = [_[0] for _ in tuplen]
    cursor.commit()
    cursor.close()

    cursor = conexion.cursor()
    cursor.execute("SELECT empresa FROM [dbo].[persona]")
    tuplee = cursor.fetchall()
    empresas = [_[0] for _ in tuplee]
    cursor.commit()
    cursor.close()

    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM [dbo].[persona]")
    tuplei = cursor.fetchall()
    id = [_[0] for _ in tuplei]
    cursor.commit()
    cursor.close()

    nombre_cb = ttk.Combobox(nuevocliente, textvariable=selected_nombre, width="18")
    nombre_cb['values'] = nombres
    nombre_cb['state'] = 'readonly'  # normal
    nombre_cb.grid(row=1, column=2)
    nombre_cb.bind('<<ComboboxSelected>>', nombre_changed)
    
    tk.Label(nuevocliente, text="Nombre del cliente").grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(nuevocliente, text="Nombre de la empresa").grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(nuevocliente, text="Cargo").grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(nuevocliente, text="Celular").grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)
        
    botonNO = ttk.Button(
    nuevocliente, 
    text="Creaci??n Oferta", 
     command=lambda:tipoWindow(id[nombre_cb.current()], nombre_cb.get(),empresa_en.get(),cargo_en.get(),phone_en.get())

    )

    botonNO.grid(column=1, row=5, sticky=tk.SW ,padx=5, pady=5)