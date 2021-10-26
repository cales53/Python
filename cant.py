import tkinter as tk
from tkinter import ttk
import pyodbc
from tkinter.messagebox import showinfo

mywindow = tk.Tk()
mywindow.title("Ingreso Cliente Nuevo")
mywindow.resizable(1, 1)

def cant_changed(event):
    msg = f'You selected {cont_cant_cb.get()}!'
    showinfo(title='Result', message=msg)

# month of year
cantidad = ('1', '2', '3', '4', '5', '6',
        '7', '8', '9', '10', '11', '12')

label = tk.Label(mywindow, text="Cuantos concentradores").grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)

# create a combobox
selected_cantidad = tk.StringVar()

cont_cant_cb = ttk.Combobox(mywindow, textvariable=selected_cantidad, width = 2)
cont_cant_cb.grid(column=1, row=6, sticky=tk.SW, padx=5, pady=5)
cont_cant_cb['values'] = cantidad
cont_cant_cb['state'] = 'readonly'  # normal

cont_cant_cb.bind('<<ComboboxSelected>>', cant_changed)


label = tk.Label(mywindow, text="Cuantos concentradores").grid(row=7, column=1, sticky=tk.W, padx=5, pady=5)

control_cant_cb = ttk.Combobox(mywindow, textvariable=selected_cantidad, width = 2)
control_cant_cb.grid(column=1, row=8, sticky=tk.SW,padx=5, pady=5)
control_cant_cb['values'] = cantidad
control_cant_cb['state'] = 'readonly'  # normal

control_cant_cb.bind('<<ComboboxSelected>>', cant_changed)

mywindow.mainloop()