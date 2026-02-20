from datetime import datetime
    
class Calculadora:
    def __init__(self,usuario ,fecha_uso, tipo_operacion):
        
        self.tipo_operacion= tipo_operacion
        self.usuario = usuario 
        self.resultado= None
        self.fecha = datetime.now()
        
   
        
    def get_tipo_operacion(self):
        return self.tipo_operacion
    
    def get_fecha(self):
        return self.fecha
    
    def set_tipo_operacion(self,nueva_operacion):
        self.tipo_operacion=nueva_operacion
    
    def realizar_operacion (self, num1, num2):
        
        if self.tipo_operacion== "suma":
            self.resultado= num1.get_valor() + num2.get_valor()
            
        elif self.tipo_operacion== "resta":
                self.resultado= num1.get_valor() - num2.get_valor()
                
        elif self.tipo_operacion== "multi":
            self.resultado= num1.get_valor() * num2.get_valor()
            
        elif self.tipo_operacion== "division":
            if num2.get_valor() == 0:
             self.resultado= num1.get_valor() / num2.get_valor()
        else: 
            return "Error maldito, no se puede dividir por 0 estúpido"
        
        return self.resultado
    
    def mostrar_info(self):
        return f"""
Usuario: {self.__usuario.get_nombre()}
Cedula: {self.__usuario.get_cedula()}
Operacion: {self.__tipo_operacion}
Resultado: {self.__resultado}
Fecha: {self.__fecha}
"""
          
        
            
    
        
    
        
    
        
        
        
        
        
        
        
        
        
        
        