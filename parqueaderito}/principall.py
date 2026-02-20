from usuario import Usuario
from carro import Carro
from parqueadero import Parqueadero




mi_parqueadero = Parqueadero()

 # Crear usuarios
usuario1 = Usuario("1020345678", "Juan García", "Administrador")
usuario2 = Usuario("1020345679", "María López", "Cliente")
usuario3 = Usuario("1020345680", "Carlos Rodríguez", "Cliente")
usuario4 = Usuario("1020345681", "Ana Martínez", "Cliente")

    # Crear carros
carro1 = Carro("ABC123", "Sedan", "Negro")
carro2 = Carro("XYZ789", "SUV", "Blanco")
carro3 = Carro("KLM456", "Pickup", "Azul")
carro4 = Carro("DEF321", "Hatchback", "Rojo")

    # Agregar registros
mi_parqueadero.agregar_registro(usuario1, carro1, "A-01", "2026-02-16", "08:30")
mi_parqueadero.agregar_registro(usuario2, carro2, "B-05", "2026-02-16", "09:15")
mi_parqueadero.agregar_registro(usuario3, carro3, "C-12", "2026-02-16", "10:00")
mi_parqueadero.agregar_registro(usuario4, carro4, "A-03", "2026-02-16", "11:20")

    # Registrar salida
mi_parqueadero.registrar_salida("KLM456", "11:45")

    # Mostrar todo
mi_parqueadero.mostrar_todo()



  