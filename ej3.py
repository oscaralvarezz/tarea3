#intentamos hacer el ejercicio 3.
from pickle import TRUE

class Nave():
    def __init__(self, nombre, largo, tripulacion, cantidad_pasajeros):
        self.nombre= nombre
        self.largo=largo
        self.tripulacion= tripulacion
        self.cantidad_pasajeros=cantidad_pasajeros

    def __str__(self):
        return "{}".format(self.nombre)

print("informacion")
def nombres(lista_naves):
    lista_ordenada = sorted(lista_naves,key=lambda x:x.nombre.lower())
    print([i.nombre for i in lista_ordenada])
    return lista_ordenada

def largo(lista_naves):
    lista_ordenada=sorted(lista_naves,key=lambda x:x.largo, reverse = True)
    print([(i.nombre, i.largo) for i in lista_ordenada])
    return lista_ordenada 

Halcon_Milenario= Nave("Halcón-Milenario",34.37,3,1)
Estrella_muerte=Nave("Estrella de la muerte", 178,200000, 1000000)
TIE_fighter=Nave("TIE-Fighter", 6.3, 1, 45)
x_wing = Nave("X-wing", 12.5,2, 346)
quinta= Nave("At-23000",134,3, 453)
sexta = Nave("Atras-24", 45,3,6)
naves=[Halcon_Milenario, x_wing,TIE_fighter,Estrella_muerte, quinta, sexta]  

nombres(naves)
largo(naves)

print("info Halcon y Estrella")
print(Halcon_Milenario.__dict__)
print(Estrella_muerte.__dict__)


print("pasajeros")
def cantidad_pasajeros(lista_naves):
    lista_ordenada=sorted(lista_naves,key=lambda x:x.cantidad_pasajeros, reverse= True)
    print([(i.nombre, i.cantidad_pasajeros) for i in lista_ordenada[0:5]])

cantidad_pasajeros(naves)

print("tripulacion")

def tripulacion(lista_naves):
    lista_ordenada=sorted(lista_naves,key=lambda x:x.tripulacion, reverse= True)
    print(lista_ordenada[0].nombre, lista_ordenada[0].tripulacion)

tripulacion(naves)

print("naves AT")

def nombre_AT(lista_naves):
    lista_AT= []
    for nave in lista_naves:
        if nave.nombre[0:2].lower()== "at":
            lista_AT.append(nave.nombre)
    print(lista_AT)

nombre_AT(naves)

print("num pasajeros > 6")

def cantidad_pasajeros(lista_naves):
    lista_mas_6_pasajeros= []
    for nave in lista_naves:
        if nave.cantidad_pasajeros>=6:
            lista_mas_6_pasajeros.append(nave)
    print([nave.nombre for nave in lista_mas_6_pasajeros])

cantidad_pasajeros(naves)


print("info nave + peq y + grande")

def tamanio(lista_naves):
    lista_ordenada=sorted(lista_naves,key=lambda x:x.largo)
    print("La nave más pequeña es: {} y la nave más grande es: {}".format(lista_ordenada[0].__dict__,lista_ordenada[-1].__dict__))

tamanio(naves)