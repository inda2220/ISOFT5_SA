import re

# --- Validaciones separadas ---
def validar_nombre(nombre: str) -> bool:
    """Valida que el nombre no esté vacío y solo tenga letras y espacios."""
    return bool(nombre and re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", nombre))

def validar_correo(correo: str) -> bool:
    """Valida que el correo sea de dominios gmail, hotmail u outlook."""
    return bool(correo and re.match(r"^[a-zA-Z0-9._%+-]+@(gmail|hotmail|outlook)\.com$", correo))


# --- Clase Singleton ---
class RegistroUsuarios:
    _instance = None  # atributo estático

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # proteger para que no reinicialice si ya existe
        if not hasattr(self, "_initialized"):
            self.nombres = []
            self.correos = []
            self._initialized = True  # bandera de inicialización

    def registrar(self, nombre: str, correo: str) -> tuple[bool, str]:
        """Intenta registrar un usuario. Devuelve (éxito, mensaje)."""

        if not validar_nombre(nombre):
            return False, "❌ El nombre solo debe contener letras y espacios."

        if nombre in self.nombres:
            return False, "❌ Ese nombre ya está registrado."

        if not validar_correo(correo):
            return False, "❌ Correo inválido. Solo se aceptan dominios: gmail, hotmail, outlook."

        if correo in self.correos:
            return False, "❌ Ese correo ya está registrado."

        # Si pasa las validaciones, se guarda
        self.nombres.append(nombre)
        self.correos.append(correo)
        return True, f"✅ Usuario '{nombre}' registrado con éxito."


# --- Uso / demo ---
def main():
    registro = RegistroUsuarios()

    nombre = input("Ingresa tu nombre: ").strip()
    correo = input("Ingresa tu correo electrónico: ").strip()

    ok, mensaje = registro.registrar(nombre, correo)
    print(mensaje)

    # Comprobar Singleton
    otro = RegistroUsuarios()
    print("\n📋 Usuarios registrados (desde otra variable Singleton):")
    print("Nombres:", otro.nombres)
    print("Correos:", otro.correos)


if __name__ == "__main__":
    main()
