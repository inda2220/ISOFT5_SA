import time  # Para simular pausas entre acciones
import random  # Para seleccionar acciones y ordenar de forma aleatoria

# Definimos la clase Borracho que representa a una persona en una fiesta
class Borracho:
    # Constructor: se ejecuta al crear un objeto Borracho
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del borracho
        self.ultima_accion = None  # Guarda la última acción que hizo
        self.veces_tomado = 0  # Cuenta cuántas veces ha tomado seguidas

    # Acción de tomar cerveza
    def tomar(self):
        print(f"{self.nombre} tomando cerveza...")  # Mensaje en consola
        time.sleep(1)  # Pausa de 1 segundo simulando el tiempo de la acción
        self.ultima_accion = "tomar"  # Se guarda esta acción como la última
        self.veces_tomado += 1  # Se incrementa el contador de tragos seguidos

    # Acción de ir al baño
    def usar_baño(self):
        print(f"{self.nombre} orinando....")  # Mensaje al empezar
        time.sleep(1)  # Espera 1 segundo
        print(f"{self.nombre} salió del baño.")  # Mensaje al terminar
        self.ultima_accion = "usar_baño"  # Se actualiza la última acción
        self.veces_tomado = 0  # Se reinicia el contador de tragos

    # Acción de llamar a su ex (clásico borracho)
    def call_to_EX(self):
        print(f"{self.nombre} calling to the EX")  # Mensaje al marcar
        time.sleep(1)  # Pausa de 1 segundo
        print(f"{self.nombre} hang up")  # Mensaje al colgar
        self.ultima_accion = "call_to_EX"  # Actualiza acción
        self.veces_tomado = 0  # Reinicia contador de tragos

    # Acción de cantar
    def sing(self):
        print(f"{self.nombre} singing")  # Mensaje al cantar
        self.ultima_accion = "sing"  # Se guarda la acción
        self.veces_tomado = 0  # Reinicia contador de tragos

    # Método principal: decide qué acción hará el borracho en su turno
    def hacer_algo(self):
        # Condición para poder tomar: no ha tomado más de 1 vez seguida y hay 60% de probabilidad
        if self.veces_tomado < 1 and random.random() < 0.6:
            self.tomar()  # Si se cumple, toma otra chela
            return  # Sale del método (ya hizo su acción)

        # Si no puede tomar, arma una lista de acciones posibles que no repitan la última
        acciones_disponibles = []
        
        # Solo añade ir al baño si no fue su última acción
        if self.ultima_accion != "usar_baño":
            acciones_disponibles.append(self.usar_baño)
        
        # Solo añade llamar a la ex si no fue la última acción
        if self.ultima_accion != "call_to_EX":
            acciones_disponibles.append(self.call_to_EX)
        
        # Solo añade cantar si no fue la última acción
        if self.ultima_accion != "sing":
            acciones_disponibles.append(self.sing)
        
        # Si por alguna razón no hay acciones disponibles, se desbloquean todas
        if not acciones_disponibles:
            acciones_disponibles = [self.usar_baño, self.call_to_EX, self.sing]
        
        # Selecciona aleatoriamente una de las acciones válidas
        accion = random.choice(acciones_disponibles)
        accion()  # Ejecuta la acción seleccionada

# Creamos 5 objetos Borracho con nombres distintos
borrachito1 = Borracho("Borrachito 1")
borrachito2 = Borracho("Borrachito 2")
borrachito3 = Borracho("Borrachito 3")
borrachito4 = Borracho("Borrachito 4")
borrachito5 = Borracho("Borrachito 5")

# Ejecutamos 4 rondas de la fiesta
for ciclo in range(4):
    print(f"\n--- Ciclo {ciclo + 1} ---")  # Indicamos el número de ciclo
    
    # Creamos una lista con los borrachos y la mezclamos aleatoriamente
    borrachitos = [borrachito1, borrachito2, borrachito3, borrachito4, borrachito5]
    random.shuffle(borrachitos)  # Cambiamos el orden cada vez

    # Cada borracho hace una acción en orden aleatorio
    for borrachito in borrachitos:
        borrachito.hacer_algo()  # Llama al método que decide la acción

    time.sleep(2)  # Pausa de 2 segundos entre ciclos para simular el paso del tiempo
