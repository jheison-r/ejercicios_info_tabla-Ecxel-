class Usuario:
    def __init__(self,cedula,nombre,apellido):
      self.cedula=cedula
      self.nombre=nombre
      self.apellido=apellido
      
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self,nuevo_nombre):
        nuevo_nombre=input("ingrese su nombre: ")
        self.nombre=nuevo_nombre

    def get_apellido(self):
        return self.apellido
    
    def set_apellido(self,nuevo_apellido):
        nuevo_apellido=input("Digite su apellido: ")
        self.apellido=nuevo_apellido
          
    def get_cedula(self):
        return self.cedula
    
    def set_cedula(self,nueva_cedula):
        self.cedula = nueva_cedula
        
    def imprimir_datos(self):
        print (f"nombre cliente:{self.nombre}")
        print (f"Apellido cliente: {self.apellido}")
        print (f"cedula cliente:{self.cedula}")
        
