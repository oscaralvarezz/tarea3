#intentamos hacer el ejercicio 1
def mover(discos, tubo1 = 1, pibote = 2, tubo2 = 3):
    if discos > 0: 
        mover(discos - 1, tubo1, tubo2, pibote)
        print("Movemos el disco {discos} de {tubo1} a {tubo2}")
        mover(discos -1, pibote, tubo1, tubo2)

if __name__ == "__main__":
    num = 20
    mover(20)