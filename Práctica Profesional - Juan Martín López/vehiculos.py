from abc import ABC


class Vehiculo(ABC):
    CONTADOR = 0

    def __init__(
            self,
            nombre,
            marca,
            modelo,
            kilometraje,
            combustible,
            antiguedad,
            service_al_dia,
            precio,
            sucursales_vinculadas
    ):
        Vehiculo.CONTADOR += 1

        self.identificador = Vehiculo.CONTADOR
        self.nombre = nombre
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = kilometraje
        self.combustible = combustible
        self.antiguedad = antiguedad
        self.service_al_dia = service_al_dia
        self.precio = precio
        self.sucursales_vinculadas = sucursales_vinculadas

    def get_vehiculo(self):
        return f"{self.nombre}\n" \
               f"{self.marca}\n" \
               f"{self.modelo}\n" \
               f"{self.kilometraje}\n" \
               f"{self.combustible}\n" \
               f"{self.antiguedad}\n" \
               f"{self.service_al_dia}\n" \
               f"{self.precio}\n"

    def get_sucursales_vinculadas(self):
        return self.sucursales_vinculadas

    def calcular_nivel_desgaste(self):
        return self.kilometraje / self.antiguedad

    vehiculo = property(get_vehiculo)
    sucursales = property(get_sucursales_vinculadas)


class Camioneta(Vehiculo):
    def __init__(
            self,
            nombre,
            marca,
            modelo,
            kilometraje,
            combustible,
            antiguedad,
            service_al_dia,
            precio,
            sucursales_vinculadas):
        super().__init__(
            nombre,
            marca,
            modelo,
            kilometraje,
            combustible,
            antiguedad,
            service_al_dia,
            precio,
            sucursales_vinculadas
        )

    def calcular_nivel_desgaste(self):
        if self.combustible.lower == "diesel":
            return (self.kilometraje / self.antiguedad) / 1000
        elif self.combustible.lower == "nafta":
            return (self.kilometraje / self.antiguedad) / 100


class Auto(Vehiculo):
    def __init__(
            self,
            nombre,
            marca,
            modelo,
            kilometraje,
            combustible,
            antiguedad,
            service_al_dia,
            precio,
            sucursales_vinculadas):
        super().__init__(
            nombre,
            marca,
            modelo,
            kilometraje,
            combustible,
            antiguedad,
            service_al_dia,
            precio,
            sucursales_vinculadas
        )

    def calcular_nivel_desgaste(self):
        if self.service_al_dia:
            return (self.kilometraje / self.antiguedad) / 100
        else:
            return (self.kilometraje / self.antiguedad) / 10


class Moto(Vehiculo):
    def __init__(
            self,
            nombre,
            marca,
            modelo,
            kilometraje,
            combustible,
            antiguedad,
            service_al_dia,
            precio,
            sucursales_vinculadas):
        super().__init__(
            nombre,
            marca,
            modelo,
            kilometraje,
            combustible,
            antiguedad,
            service_al_dia,
            precio,
            sucursales_vinculadas
        )

    def calcular_nivel_desgaste(self):
        if self.service_al_dia and self.kilometraje <= 30000:
            return (self.kilometraje / self.antiguedad) / 1000
        else:
            return (self.kilometraje / self.antiguedad) / 10
