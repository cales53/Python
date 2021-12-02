import tkinter as tk
from tkinter import ttk
import pyodbc
from configuracion import server, bd, usuario, contrasena
from tipoofc import tipoWindow

#from tkinter.messagebox import showinfo
conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)
    
def ActualizarEmpresa():  
    empresawin = tk.Tk()
    empresawin.title("Actualizar Cliente")
    empresawin.resizable(1, 1)
    empresawin.columnconfigure(1, weight=3)
    empresawin.minsize(300,100)
    empresawin.maxsize(300,155)
    selected_empresa = tk.StringVar()

    cargo_en = tk.Entry(empresawin)
    phone_en = tk.Entry(empresawin)
    nombre_en = tk.Entry(empresawin)

    nombre_en.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)
    cargo_en.grid(row=3, column=2, sticky=tk.W, padx=5, pady=5)
    phone_en.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)

    def empresa_changed(event):
      
        cargo_en.delete(0, tk.END)
        phone_en.delete(0, tk.END)
        nombre_en.delete(0, tk.END)

        cursor = conexion.cursor()

        consulta = "delete from persona WHERE nombre = '';"
        cursor.execute(consulta)
        cursor.commit()

        cursor.execute("SELECT nombre FROM [dbo].[persona]")
        tuplen = cursor.fetchall()
        names = [_[0] for _ in tuplen]
        cursor.commit()
        cursor.execute("SELECT cargo FROM [dbo].[persona]")
        tuplec = cursor.fetchall()
        cargos = [_[0] for _ in tuplec]
        cursor.commit()
        cursor.execute("SELECT ntelefono FROM [dbo].[persona]")
        tuplet = cursor.fetchall()
        phones = [_[0] for _ in tuplet]
        cursor.commit()
        cursor.execute("SELECT id FROM [dbo].[persona]")
        cursor.commit()

        cargo_en.insert(10, cargos[empresa_cb.current()])
        phone_en.insert(10, phones[empresa_cb.current()])
        nombre_en.insert(10, names[empresa_cb.current()])

        cursor.close()

    cursor = conexion.cursor()
    cursor.execute("SELECT nombre FROM [dbo].[persona]")
    tuplen = cursor.fetchall()
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

    empresa_cb = ttk.Combobox(empresawin, textvariable=selected_empresa, width="18")
    empresa_cb['values'] = empresas
    empresa_cb['state'] = 'readonly'  # normal
    empresa_cb.grid(row=1, column=2)
    empresa_cb.bind('<<ComboboxSelected>>', empresa_changed)
        
    tk.Label(empresawin, text="Nombre del cliente").grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(empresawin, text="Nombre de la empresa").grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(empresawin, text="Cargo").grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
    tk.Label(empresawin, text="Celular").grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)
        
    botonNO = ttk.Button(
    empresawin, 
    text="Creación Oferta", 
     command=lambda:tipoWindow(id[empresa_cb.current()], nombre_en.get(),empresa_cb.get(),cargo_en.get(),phone_en.get())

    )

    botonNO.grid(column=1, row=5, sticky=tk.SW ,padx=5, pady=5)