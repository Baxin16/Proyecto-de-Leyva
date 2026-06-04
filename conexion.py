# Kevin Eduardo Baxin

# conexion.py

import mysql.connector

def conectar():
conexion = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="escuela"
)

```
return conexion
```
