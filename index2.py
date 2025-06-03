import re

nombres = []
correos = []

def registrar_usuario():
    nombre = input("Ingresa tu nombre: ").strip()
    if not nombre or not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", nombre):
        print("ERROR: El nombre solo debe contener letras y espacios.")
        return

    if nombre in nombres:
        print("ERROR: Ese nombre ya está registrado.")
        return

    correo = input("Ingresa tu correo electrónico: ").strip()
    if not correo or not re.match(r"^[a-zA-Z0-9._%+-]+@(gmail|hotmail|outlook)\.com$", correo):
        print("ERROR: El correo debe ser de los siguientes dominios: @gmail.com, @hotmail.com, @outlook.com")
        return

    if correo in correos:
        print("ERROR: Ese correo ya está registrado.")
        return

    nombres.append(nombre)
    correos.append(correo)

    print("Usuario registrado correctamente.")
    print(f"Nombre: {nombre}")
    print(f"Correo: {correo}")

registrar_usuario()
print("Nombres:", nombres)
print("Correos:", correos)
