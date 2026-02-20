class Parqueadero:
    def _init_(self):
        self.__registros = []

    def agregar_registro(self, usuario, carro, puesto, fecha, hora_entrada):
        # Verificar si el puesto está ocupado
        for r in self.__registros:
            if r["puesto"] == puesto and r["estado"] == "Entrada":
                print(f"Error: El puesto {puesto} ya está ocupado.")
                return

        registro = {
            "usuario": usuario,
            "carro": carro,
            "puesto": puesto,
            "fecha": fecha,
            "hora_entrada": hora_entrada,
            "hora_salida": "",
            "estado": "Entrada"
        }

        self.__registros.append(registro)

    def registrar_salida(self, placa, hora_salida):
        for r in self.__registros:
            if r["carro"].get_placa() == placa and r["estado"] == "Entrada":
                r["hora_salida"] = hora_salida
                r["estado"] = "Salida"
                print(f"Salida procesada: {placa}")
                return
        print(f"No se encontró vehículo activo con placa {placa}")

    def mostrar_todo(self):
        print("\n" + "="*90)
        print(f"| {'CEDULA':10} | {'NOMBRE':16} | {'PLACA':7} | {'PUESTO':5} | {'ENTRADA':7} | {'SALIDA':7} | {'ESTADO':7} |")
        print("-" * 90)

        for r in self.__registros:
            usuario = r["usuario"]
            carro = r["carro"]
            h_salida = r["hora_salida"] if r["hora_salida"] != "" else "  --  "

            print(f"| {usuario.get_cedula():10} | "
                  f"{usuario.get_nombre():16} | "
                  f"{carro.get_placa():7} | "
                  f"{r['puesto']:5} | "
                  f"{r['hora_entrada']:7} | "
                  f"{h_salida:7} | "
                  f"{r['estado']:7} |")

        print("="*90)