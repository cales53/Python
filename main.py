import pyodbc
from kivy.app import App
from kivy.uix.button import Button



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

class TestApp(App):
    def build(self):
        return Button(text='Hello World')
TestApp().run()