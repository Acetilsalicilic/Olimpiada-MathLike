from math import ceil
from typing import Union

def find_sublist():
    pass


def calcularPrimos(t: int) -> list[int]:
    # Definir el límite
    limite = ceil(t / 2)

    # Tercer paso: criba
    numerosMenoresQueT = list(range(1, limite + 1))
    primosMenoresQueT = numerosMenoresQueT.copy()
    d = 0
    while primosMenoresQueT[d] ** 2 < limite:
        for n in primosMenoresQueT:
            if n != d:
                if n % primosMenoresQueT[d] == 0:
                    primosMenoresQueT.remove(n)
        
        d += 1
    
    #print(f'Lista numeros: {primosMenoresQueT}')

    # Descomposición en factores primos
    listaPrimos = []
    # tTemp = t
    i = 0
    while True:
        if t % primosMenoresQueT[i] == 0:
            listaPrimos.append(primosMenoresQueT[i])
            t /= primosMenoresQueT[i]
        else:
            i += 1

        if i == len(primosMenoresQueT):
            break
    
    #print(f'Lista factores primos {listaPrimos}')
    return listaPrimos


def validar(L: list[int], t: int) -> Union[list[int | None]]:
    if len(L) == 0: # Si la lista está vacía, retornar lista vacía
        return []
    
    if len(L) == 1 and t in L: # Si tiene un solo elemento y ese elemento es el mismo t, retornar L
        return L
    
    # Verificar que los números en L sean positivos
    for n in L:
        if n < 0 or n % int(n) != 0:
            raise Exception("Error: los números deben ser estrictamente positivos y sin cifras decimales")
    
    return None


def determinarSublistas(listaPrimos: list[int], L: list[int]):
    # Crear sublistas a probar
    sublistasAProbar = []
    listaListasAProbar = [[listaPrimos]]
    nivelesACalcular = len(listaPrimos) - 1
    nivelesCalculados = 0

    while nivelesCalculados < nivelesACalcular: # Recorrer todos los niveles
        nuevoNivel = []
        #lista = listaListasAProbar[-1][-1] 
        for lista in listaListasAProbar[-1]: # Usar los elementos del último nivel y  Usar los elementos de la última lsta en el nivel
            for n in range(0, len(lista) - 1): # Añadir a una nueva lista
                itemACombinar1 = lista[n]
                itemACombinar2 = lista[n + 1]
                nuevaLista = [itemACombinar1 * itemACombinar2]
                nuevaLista += [x for i,x in enumerate(lista) if i != n and i != n+1]
                # nuevaLista += list(filter(lambda a : lista.index(a) != n or lista.index(a) != n + 1, lista)) It's broken

                nuevoNivel.append(nuevaLista)
        listaListasAProbar.append(nuevoNivel)
        nivelesCalculados += 1

    # print(f'listaDeSublistas: {listaListasAProbar}')
    print(f'listaDeSublistas: {listaListasAProbar}')

    # concentrar las sublistas en sublistasAProbar
    for nivel in listaListasAProbar:
        for sublista in nivel:
            sublistasAProbar.append(sublista)

    print(f'Listas a probar {sublistasAProbar}')

    
    # Verificar si es una sublista
    sublistas = []
    removed = False
    
    for sublista in sublistasAProbar:
        sublistaTemp = sublista.copy()
        for n in L:
            for m in sublistaTemp:
                if n == m:
                    sublistaTemp.remove(m)
                    removed = True
                
                if removed:
                    break
            
            if removed:
                removed = False
                continue
        
        if len(sublistaTemp) == 0:
            sublistas.append(sublista)
    
    for lista in sublistas:
        lista.sort()
    
    return sublistas

print(calcularPrimos(100))
print(validar([1, 2.3, -3, 4, 5], 3))
print(validar([1, 2, 3, 4, 5], 3))