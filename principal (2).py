from usuario import Usuario
from numero import Numero
from calculadora import Calculadora

print("=== DATOS DEL USUARIO ===")
nombre = input("Nombre: ")
cedula = input("Cedula: ")
apellido=input("apellidin: ")

usuario = Usuario(nombre, cedula, apellido)


print("\nOperaciones: suma, resta, multiplicacion, division")
operacion = input("Operacion: ")

n1 = Numero(float(input("Numero 1: ")))
n2 = Numero(float(input("Numero 2: ")))

calc = Calculadora(operacion, usuario)

resultado = calc.realizar_operacion(n1, n2)

print("Resultado:", resultado)
print(calc.mostrar_info())
















