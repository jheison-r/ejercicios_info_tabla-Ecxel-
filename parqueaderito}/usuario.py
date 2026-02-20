class Usuario:
    def _init_(self, cedula, nombre, tipo_usuario):
        self.cedula = cedula
        self.nombre = nombre
        self.tipo_usuario = tipo_usuario

    # GETTERS
    def get_cedula(self):
        return self.cedula

    def get_nombre(self):
        return self.nombre

    def get_tipo_usuario(self):
        return self.tipo_usuario