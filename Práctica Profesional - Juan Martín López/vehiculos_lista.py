import vehiculos as vh


lista_vehiculos = {}


def add_vehiculo(valor):
    if isinstance(valor, vh.Vehiculo):
        lista_vehiculos[str(valor.identificador)] = valor  # [str(valor.identificador)] representa la key.


def del_vehiculo(id_vehiculo):
    for sucursal in lista_vehiculos.values():
        if sucursal.identificador == id_vehiculo:
            del lista_vehiculos[str(id_vehiculo)]


add_vehiculo(vh.Camioneta("Hilux", "Toyota", "2", 50000, "Diesel", 4, True, 900000.0, [1]))
add_vehiculo(vh.Camioneta("Hilux", "Toyota", "2", 10000, "Diesel", 2, True, 1200000.0, [1]))
add_vehiculo(vh.Auto("Etios", "Toyota", "2015", 70000, "Nafta", 2, True, 800000.0, [1]))

add_vehiculo(vh.Auto("Chevrolet", "Corsa", "2010", 30000, "Nafta", 5, False, 700000.0, [2, 3]))
add_vehiculo(vh.Auto("Chevrolet", "Corsa", "2010", 30000, "Nafta", 5, True, 900000.0, [2, 3]))
add_vehiculo(vh.Auto("Chevrolet", "Meriva", "2011", 60000, "Nafta", 6, False, 700000.0, [2]))
add_vehiculo(vh.Auto("Chevrolet", "Meriva", "2011", 50000, "Nafta", 4, True, 900000.0, [3]))

add_vehiculo(vh.Auto("Honda", "Civic", "2021", 10000, "Nafta", 1, False, 1000000.0, [4]))
add_vehiculo(vh.Moto("Honda", "Cravea", "2", 20000, "Nafta", 3, True, 600000.0, [4]))
add_vehiculo(vh.Moto("Honda", "Cravea", "2", 20000, "Nafta", 3, False, 550000.0, [4]))

print(lista_vehiculos)