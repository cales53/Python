import pyodbc
from sshtunnel import SSHTunnelForwarder

bd = "Clientes"
usuario = "usuario"
contrasena = "Manager21"

try:
    server = ('192.168.1.89')
    conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)
    print("Conexion exitosa")
except:
    with SSHTunnelForwarder(
        ('190.147.177.209', 22),
        ssh_username="admin",
        ssh_password="%it$2018",
        local_bind_address=('127.0.0.1', 1433),
        remote_bind_address=('192.168.1.89', 1433)) as sv:
        sv.start()

        print("Server Connected")
        server = ('127.0.0.1')
        bd = "Clientes"
        usuario = "usuario"
        contrasena = "Manager21"

        conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)
        print("Conexion exitosa")
        sv.close()