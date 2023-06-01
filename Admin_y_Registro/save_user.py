#!/usr/bin/env python
import cgi

# Establecer la ruta y el nombre del archivo de la base de datos
database_file = "users.csv"

# Obtener los datos del formulario
form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

# Guardar los datos en la base de datos
with open(database_file, "a") as f:
    f.write(f"{username},{password}\n")

# Redirigir al usuario a una página de éxito o realizar otras acciones necesarias
print("Content-Type: text/html")
print("Location: /admin.html")
print()
