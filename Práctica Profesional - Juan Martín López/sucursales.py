from sucursales_lista import lista_sucursales
from vehiculos_lista import lista_vehiculos
from vehiculos import Camioneta, Auto, Moto


class Sucursal:
    CONTADOR = 0

    def __init__(self, nombre, direccion, horario_apertura, horario_cierre):
        Sucursal.CONTADOR += 1

        self.identificador = Sucursal.CONTADOR
        self.nombre = nombre
        self.direccion = direccion
        self.horario_apertura = horario_apertura
        self.horario_cierre = horario_cierre

    def set_sucursal(self, nuevo_nombre="", nueva_direccion="", nuevo_horario_apertura="", nuevo_horario_cierre=""):
        if nuevo_nombre != "":
            self.nombre = nuevo_nombre
        if nueva_direccion != "":
            self.direccion = nueva_direccion
        if nuevo_horario_apertura != "":
            self.horario_apertura = nuevo_horario_apertura
        if nuevo_horario_cierre != "":
            self.horario_cierre = nuevo_horario_cierre

    def get_sucursal(self):
        return f"{self.nombre}\n" \
               f"{self.direccion}\n" \
               f"{self.horario_apertura}\n" \
               f"{self.horario_cierre}"

    def buscar_vehiculos(self):
        pass

    def buscar_sin_filtros(self):
        for vehiculo in lista_vehiculos:
            print(
                vehiculo.nombre,
                vehiculo.marca,
                vehiculo.modelo,
                vehiculo.kilometraje,
                vehiculo.combustible,
                vehiculo.antiguedad,
                vehiculo.service_al_dia,
                vehiculo.precio,
                vehiculo.sucursales_vinculadas
            )

    def buscar_por_categoria(self):
        seleccion = str(input("¿Qué categoría desea buscar?")).lower
        if seleccion == "camioneta":
            seleccion = Camioneta  # selección pasa a ser de la clase seleccionada.
        elif seleccion == "auto":
            seleccion = Auto
        elif seleccion == "moto":
            seleccion = Moto

        for vehiculo in lista_vehiculos:
            if isinstance(vehiculo, seleccion):
                print(
                    vehiculo.nombre,
                    vehiculo.marca,
                    vehiculo.modelo,
                    vehiculo.kilometraje,
                    vehiculo.combustible,
                    vehiculo.antiguedad,
                    vehiculo.service_al_dia,
                    vehiculo.precio,
                    vehiculo.sucursales_vinculadas
                )

    def buscar_por_desgaste(self):
        pass

    sucursal = property(get_sucursal, set_sucursal)


print(lista_sucursales[1].buscar_sin_filtros)