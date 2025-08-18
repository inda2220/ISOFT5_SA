import tkinter as tk
from tkinter import messagebox, simpledialog
import re

usuarios = []

# Funciones
def mostrar_ubicacion():
    ubicacion = (
        "📍 Nos encontramos en: UNIVERSIDAD POLITÉCNICA DEL ESTADO DE NAYARIT\n"
        "🕒 Horario: Martes a domingo\n"
        "📦 Contamos con envío a domicilio"
    )
    messagebox.showinfo("Ubicación", ubicacion)

def contacto():
    contacto = (
        "📞 Contacto para pedidos:\n\n"
        "Julio Cesar Inda Jimenez: 311 300 31 84\n"
        "David de Jesus Gonzalez Ramirez: 311 161 86 26 (Solo WhatsApp)\n"
        "Gabriel Eduardo Leal Hernandez: 311 186 01 37\n"
        "Edgar Fabian Perez Zepeda: 311 265 31 89"
    )
    messagebox.showinfo("Contacto", contacto)

def registrar_usuario():
    nombre = simpledialog.askstring("Registro", "Ingresa tu nombre:")
    if not nombre or not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", nombre):
        messagebox.showerror("Error", "El nombre solo debe contener letras.")
        return

    telefono = simpledialog.askstring("Registro", "Ingresa tu número de teléfono:")
    if not telefono or not re.match("^[0-9]+$", telefono):
        messagebox.showerror("Error", "El teléfono solo debe contener números.")
        return
    
    correo = simpledialog.askstring("Registro", "Ingresa tu correo electrónico:")
    if not correo or not re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", correo):
        messagebox.showerror("Error", "Ingresa un correo electrónico válido.")
        return

    usuarios.append({"nombre": nombre, "telefono": telefono, "correo": correo})
    messagebox.showinfo("Éxito", f"Usuario {nombre} registrado correctamente.")

def ver_usuarios():
    if not usuarios:
        messagebox.showinfo("Usuarios", "No hay usuarios registrados.")
    else:
        lista = "\n\n".join([f"- {u['nombre']}\n  Tel: {u['telefono']}\n  Email: {u['correo']}" for u in usuarios])
        messagebox.showinfo("Usuarios registrados", lista)

def hacer_pedido():
    if not usuarios:
        messagebox.showerror("Error", "Debes registrar al menos un usuario antes de hacer un pedido.")
        return

    pedido_ventana = tk.Toplevel(root)
    pedido_ventana.title("Realizar Pedido")
    pedido_ventana.geometry("400x400")

    tk.Label(pedido_ventana, text="Selecciona la cantidad de productos:", font=("Arial", 12, "bold")).pack(pady=10)

    productos = {
        "Mr.Cookies Red Velvet": {"precio": 30},
        "Mr.Cookies ChocoAve": {"precio": 30},
        "Cuernotes rellenos": {"precio": 45},
        "Brownies de chocolate": {"precio": 15},
    }

    spinners = {}

    for producto, info in productos.items():
        frame = tk.Frame(pedido_ventana)
        frame.pack(pady=5)
        tk.Label(frame, text=f"{producto} - ${info['precio']}", width=30, anchor="w").pack(side="left")
        spin = tk.Spinbox(frame, from_=0, to=10, width=5)
        spin.pack(side="right")
        spinners[producto] = spin

    def calcular_total():
        total = 0
        resumen = "🧾 Tu pedido:\n"
        algo_seleccionado = False

        for producto, spin in spinners.items():
            cantidad = int(spin.get())
            if cantidad > 0:
                precio = productos[producto]["precio"]
                subtotal = cantidad * precio
                total += subtotal
                resumen += f"- {producto} x{cantidad} = ${subtotal}\n"
                algo_seleccionado = True

        if not algo_seleccionado:
            messagebox.showwarning("Aviso", "No seleccionaste ningún producto.")
            return

        resumen += f"\nTotal: ${total}"
        messagebox.showinfo("Resumen del pedido", resumen)

    tk.Button(pedido_ventana, text="Confirmar Pedido", command=calcular_total).pack(pady=20)

# Interfaz principal
root = tk.Tk()
root.title("Mr.Cookies 🍪")
root.geometry("400x500")

# Título
titulo = tk.Label(root, text="Bienvenido a Mr.Cookies", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

subtitulo = tk.Label(root, text="¡El lugar donde los antojos sí se cumplen! 😋", font=("Arial", 12))
subtitulo.pack(pady=5)

# Botones
tk.Button(root, text="Ver Menú / Hacer Pedido", width=30, command=hacer_pedido).pack(pady=10)
tk.Button(root, text="Ver Ubicación", width=30, command=mostrar_ubicacion).pack(pady=10)
tk.Button(root, text="Registrar Usuario", width=30, command=registrar_usuario).pack(pady=10)
tk.Button(root, text="Ver Usuarios Registrados", width=30, command=ver_usuarios).pack(pady=10)
tk.Button(root, text="Ver Contacto para realizar pedidos", width=30, command=contacto).pack(pady=10)
tk.Button(root, text="Salir", width=30, command=root.quit).pack(pady=20)

# Ejecutar
root.mainloop()