from sucursales import Sucursal


lista_sucursales = {}


def add_sucursal(valor):
    if isinstance(valor, Sucursal):
        lista_sucursales[str(valor.identificador)] = valor  # [str(valor.identificador)] representa la key.


def del_sucursal(id_sucursal):
    for sucursal in lista_sucursales.values():
        if sucursal.identificador == id_sucursal:
            del lista_sucursales[str(id_sucursal)]


add_sucursal(Sucursal("Toyota.Hnos", "Alsina 1000", "12:00", "20:00"))
add_sucursal(Sucursal("Chevrolet.Hnos", "Alsina 2000", "12:00", "20:00"))
add_sucursal(Sucursal("Chevrolet2.Hnos", "Alsina 2000", "12:00", "20:00"))
add_sucursal(Sucursal("Honda.Hnos", "Alsina 2000", "12:00", "20:00"))


print(f"{lista_sucursales} \n")
print(lista_sucursales["1"])