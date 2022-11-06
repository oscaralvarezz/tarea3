#intentamos hacer el ejercicio2

matriz = [[8,9,7],[7,9,6],[8,7,8]]

def iterativa(matriz):
    matriz = matriz*2
    #matriz.pop(-1)
    det = 0
    for i in range(0,3):
        resta = matriz[i][2]*matriz[i+1][1]*matriz[i+2][0]
        sumas = matriz[i][0]*matriz[i+1][1]*matriz[i+2][2]
        det = det + (sumas-resta)
    
    print(det)


iterativa(matriz)


def recursiva(matriz):
    matriz = matriz*2
    #matriz.pop(-1)
    i = 0
    
    suma = matriz[i][0]*matriz[i+1][1]*matriz[i+2][2]
    iterativa(suma)
    
    resta  = matriz[i][2]*matriz[i+1][1]*matriz[i+2][0]
    i =+ 1
    recursiva(resta)
    
    print(recursiva(suma)-recursiva(resta))

recursiva(matriz)
