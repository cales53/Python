import pyodbc
import paramiko

server = "192.168.1.89"
bd = "Clientes"
usuario = "usuario"
contrasena = "Manager21"

try:
    conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+server+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)
    print("Conexion exitosa")
except:
    print("Conexion fallida")
    
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('192.168.1.2', 22, 'admin', '%it$2018')
entrada, salida, error = ssh_client.exec_command('ls -la')
print(salida.read())
print(error.read())
ssh_client.close()