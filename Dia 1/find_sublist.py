from math import ceil

def find_sublists(L: list[int], t: int) -> list[list[int]]:
    if len(L) == 0: # Si la lista está vacía, retornar lista vacía
        return []
    
    if len(L) == 1 and t in L: # Si tiene un solo elemento y ese elemento es el mismo t, retornar L
        return L
    
    # Verificar que los números en L sean positivos
    for n in L:
        if n < 0:
            raise Exception("Error: los números deben ser estrictamente positivos y sin cifras decimales")
        
    
    # Si t es 1 y 1 en L:
    """
    if t == 1 and 1 in L:
        retorno = [[]]
        for i in range(0, L.count(1)):
            retorno[0].append(1)
        
        retorno.append([1])
        return retorno
    """
    # Crear combinaciones de unos
    unoCount = L.count(1)
    combinacionesUno = []
    for n in range(1, unoCount + 2):
        nuevaCombinacionUno = []
        for i in range(0, n - 1):
            nuevaCombinacionUno.append(1)
        
        if len(nuevaCombinacionUno) >= 1:
            combinacionesUno.append(nuevaCombinacionUno)
    
    if t == 1 and 1 in L:
        return combinacionesUno

    # Primer paso: ordenar la lista
    # L.sort()

    # Segundo paso: establecer eliminación, t/2
    limit = ceil(t / 2)
    
    # Tercer paso: criba
    numerosMenoresQueT = list(range(1, limit + 1))
    primosMenoresQueT = numerosMenoresQueT.copy()
    d = 0
    while primosMenoresQueT[d] ** 2 < limit:
    #while d < limit:
        for n in primosMenoresQueT:
            if n != d:
                if n % primosMenoresQueT[d] == 0:
                    primosMenoresQueT.remove(n)
        
        d += 1

    # Descomposición en factores primos
    listaPrimos = []
    tTemp = t
    i = 0
    while True:
        if tTemp % primosMenoresQueT[i] == 0:
            listaPrimos.append(primosMenoresQueT[i])
            tTemp /= primosMenoresQueT[i]
        else:
            i += 1

        if i == len(primosMenoresQueT):
            break

    # Si no tiene factores primos, es decir, es primo, devolver si está contenido en L
    if len(listaPrimos) == 0 and t in L:
        return [[t], [1, t]]

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
    #print(f'listaDeSublistas: {listaListasAProbar}')

    # Eliminar las lostas repetidas del último nivel
    listaListasAProbar[-1] = [listaListasAProbar[-1][0]]

    # concentrar las sublistas en sublistasAProbar
    for nivel in listaListasAProbar:
        for sublista in nivel:
            sublistasAProbar.append(sublista)

    #print(f'Listas a probar {sublistasAProbar}')

    
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
    
    # Si L contiene 1, añadir 1 a todas las sublistas conocidas
    """
    sublistasMasUno = sublistas.copy()
    if 1 in L:
        for lista in sublistas:
            sublistasMasUno.append(lista.copy())
            sublistasMasUno[-1].append(1)
    """

    # Añadir los unos
    # Aplicar las combinaciones de 1 a todas las sublistas creadas
    sublistasMasUno = []
    for i, lista in enumerate(sublistas):
        sublistasMasUno.append(lista)
        
        for unoComb in combinacionesUno:
            sublistasMasUno.append(lista + unoComb)
    
    return sublistasMasUno


# Caso 3
print(find_sublists([1, 1, 2, 3, 5, 8, 11, 11, 13, 17, 19, 55], 55))

# Caso 4
print(find_sublists([1, 1, 2, 3, 5, 8, 11, 11, 13, 17, 19, 55], 110))

# Caso 7
print(find_sublists([1, 1, 1], 1))