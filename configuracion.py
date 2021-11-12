import time
import paramiko
from getpass import getpass
import pyodbc

server = "192.168.1.89"
bd = "Clientes"
usuario = "usuario"
contrasena = "Manager21"

try:
    conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)
    print("Conexion exitosa")
except:
    print("Conexion fallida a base de datos")
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('190.147.177.209', '222', username='cales53@msn.com', password='carlosvega4')
        stdin,stdout,stderr = client.exec_command('dir')
        conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)
    except paramiko.AuthenticationException as e:
        print('Autenticacion fallida')