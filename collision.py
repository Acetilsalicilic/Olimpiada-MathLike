# Importar Union
from typing import Union

import math

# NOTAS SOBRE LA FUNCION:
# - Retorna el valor con cuatro decimales de presición.

# Definición de la función: rN[Xcoor, Ycoor], vN[mod, theta]
def collisionDescomp(
    rA: tuple[float, float],
    vA: tuple[float, float],
    rB: tuple[float, float],
    vB: tuple[float, float]
) -> Union[float, None]:
    # Validar los datos. Estas validaciones son: 
    # que todos pertenezcan a los reales positivos
    if (rA[0] < 0 or rA[1] < 0 or vA[0] < 0):
        print('Returning none because of first validation')
        return None
    
    if (rB[0] < 0 or rB[1] < 0 or vB[0] < 0):
        print('Returnirng none because of second validation')
        return None
    
    # Descomponer ambos vectores de velocidad
    # Componente X de A
    a_xComp = math.cos(vA[1]) * vA[0]
    # Componente y de A
    a_yComp = math.sin(vA[1]) * vA[0]

    # Componete x de B
    b_xComp = math.cos(vB[1]) * vA[0]
    # Componente x de B
    b_yComp = math.sin(vB[1]) * vA[0]

    # Determinar las coordenadas de cada cuerpo
    a_xCoor, a_yCoor = rA
    b_xCoor, b_yCoor = rB

    # Determinar si Delta X tiende a 0
    deltaXTiende = False
    if (abs(a_xCoor - b_xCoor) > abs((a_xCoor + a_xComp) - (b_xCoor + b_xComp))):
        deltaXTiende = True
    
    #print(f'Value of deltaXTiende: {deltaXTiende}')
    #print(f'Value of first X abs: {abs(a_xCoor + b_xComp)}')
    #print(f'Value of second X abs: {abs((a_xCoor + a_xComp) - (b_xCoor + b_xComp))}')

    # Determinar si Delta Y tiende a 0
    deltaYTiende = False
    if (abs(a_yCoor - b_yCoor) > abs((a_yCoor + a_yComp) - (b_yCoor + b_yComp))):
        deltaYTiende = True

    #print(f'Value of deltaYTiende: {deltaYTiende}')
    
    # Si los cuerpos no colisionarán, devolver None --------------------------
    if ((not deltaXTiende) or (not deltaYTiende)):
        print('Returning none because of changes in delta')
        return None
    
    # Determinar el tiempo en que las trayectorias intersecan en X
    tiempoColisionX = abs(a_xCoor - b_xCoor) / abs(a_xComp - b_xComp)
    print(f'tiempoColisionX {tiempoColisionX}')
    
    # Determinar el tiempo en que las trayectorias intersecan en Y
    tiempoColisionY = abs(a_yCoor - b_yCoor) / abs(a_yComp - b_yComp)
    print(f'tiempoColisionY {tiempoColisionY}')

    # Función secundaria de redondeo
    tiempoColisionX = math.floor(tiempoColisionX * 10000) / 10000
    tiempoColisionY = math.floor(tiempoColisionY * 10000) / 10000

    # Comparar si ambas son iguales.
    if (tiempoColisionY == tiempoColisionX):
        return tiempoColisionX
    else:
        print('Returning none because objects don\'t collide')
        return None



# Primera prueba
print(collisionDescomp((5, 0), (2, 0.5 * math.pi), (0, 5), (2, 0)))

# Segunda prueba
print(collisionDescomp([5, 0], [2, 1.5 * math.pi], [0, 5], [2, math.pi]))

# Tercera prueba
print(collisionDescomp([-5, 0], [2, -1.5 * math.pi], [0, -5], [2, math.pi]))

# Cuarta pruebe
print(collisionDescomp([5, 0], [1, 0.5 * math.pi], [0, 5], [1, 0]))

# Quinta parte
print(collisionDescomp([3, 0], [math.sqrt(5), 0.3524 * math.pi], [0, 2], [math.sqrt(3.25), 0.58]))