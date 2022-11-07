import numpy as np
import random
from Cola import ColaEnlazada
class Grafo:
    __matriz = None
    __cantidadV = None
    def __init__(self,vertice=2):
        self.__cantidadV = vertice
        self.__matriz = np.zeros((vertice,vertice),dtype=int)

    def CrearArista(self, v1, v2):
        if (v1 <= self.__cantidadV and v2 <= self.__cantidadV) and (v1 >= 1 and v2 >= 1):
             self.__matriz[v1 - 1][v2 - 1] = 1
             #self.__matriz[v2-1][v1-1] = 1
        else:
            print('ERROR: Vertices no validos')

    def getVertice(self):
        return self.__cantidadV

    def Adyacentes(self, v):
        list = []
        if v < self.__cantidadV and v >= 0:
            for j in range(self.__cantidadV):
                if self.__matriz[v][j] == 1:
                    list.append(j)
        return list
    def mostrar(self):
        print(self.__matriz)

    def REP(self, actual, arreglo=None, recorrido=None, iniciar=False):
        if not iniciar:
            if actual - 1 >= 0 and actual - 1 < self.__cantidadV:
                arreglo = np.zeros(self.__cantidadV, dtype=int)
                recorrido = []
                recorrido = self.REP(actual=actual - 1, arreglo=arreglo, recorrido=recorrido, iniciar=True)
            else:
                print('ERROR: vertice origen no valido')
                return None
        else:
            recorrido.append(actual + 1)
            arreglo[actual] = 1
            adyacentes = self.Adyacentes(actual)
            for adyacente in adyacentes:
                if arreglo[adyacente] == 0:
                    recorrido = self.REP(adyacente, arreglo=arreglo, recorrido=recorrido, iniciar=True)

        return recorrido

    def REA(self, origen):
        arreglo = np.empty(self.__cantidadV, dtype=int)
        cola = ColaEnlazada()
        recorrido = []
        predecesores = np.zeros(self.__cantidadV, dtype=int)
        for i in range(self.__cantidadV):
            arreglo[i] = 99999
            arreglo[origen - 1] = 0  # Marcamos el vertice de origen
            cola.insertar(origen - 1)
            while not cola.vacia():
                nodo = cola.suprimir()
                recorrido.append(nodo + 1)
                for ady in self.Adyacentes(nodo):
                    if arreglo[ady] == 99999:
                        arreglo[ady] = 0
                        predecesores[ady] = nodo
                        cola.insertar(ady)
        return recorrido

    def Warshall(self):
        P = self.__matriz
        for k in range(self.__cantidadV):
            for i in range(self.__cantidadV):
                for j in range(self.__cantidadV):
                    if P[i][j] == 1 or (P[i][k] * P[k][j]) == 1:
                        P[i][j] = 1
                    else:
                        P[i][j] = 0
        return P

    def Conexo(self):
        matriz_caminos = self.Warshall()
        band = True
        i = 0
        while i < self.__cantidadV and band:
            j = 0
            while j < self.__cantidadV:
                if matriz_caminos[i][j] == 0:
                    band = False
                j += 1
            i += 1
        if band == True:
            print('Es conexo')
        else:
            print('Es disconexo')
    def getPredecesoresREA(self, origen):
        arreglo = np.empty(self.__cantidadV, dtype=int)
        cola = ColaEnlazada()
        predecesores = np.zeros(self.__cantidadV, dtype=int)
        for i in range(self.__cantidadV):
            arreglo[i] = 99999
        arreglo[origen] = 0  # Marcamos el vertice de origen
        cola.insertar(origen)
        while not cola.vacia():
            nodo = cola.suprimir()
            for ady in self.Adyacentes(nodo):
                if arreglo[ady] == 99999:
                    arreglo[ady] = 0
                    predecesores[ady] = nodo + 1
                    cola.insertar(ady)
        return predecesores

        # Metodo para obtener los predecesores de todos los nodos des utilizando el recorrido en profundidad a partir de un nodo de origen

    def getPredecesoresREP(self, actual, predecesores=None, arreglo=None, recorrido=None, iniciar=False):
        if not iniciar:
            if actual - 1 >= 0 and actual - 1 < self.__cantidadV:
                arreglo = np.zeros(self.__cantidadV, dtype=int)
                predecesores = np.zeros(self.__cantidadV, dtype=int)
                predecesores = self.getPredecesoresREP(actual=actual - 1, arreglo=arreglo, predecesores=predecesores,
                                                       iniciar=True)
            else:
                print('ERROR: vertice  origen no valido')
                return None
        else:
            arreglo[actual] = 1
            adyacentes = self.Adyacentes(actual)
            for adyacente in adyacentes:
                if arreglo[adyacente] == 0:
                    predecesores[adyacente] = actual + 1
                    predecesores = self.getPredecesoresREP(adyacente, arreglo=arreglo, predecesores=predecesores,
                                                           iniciar=True)
        return predecesores

    def camino_minimo(self, origen, destino):
        predecesores = self.getPredecesoresREA(origen - 1)
        camino = []
        actual = destino
        while actual != 0:
            camino.append(actual)
            actual = predecesores[actual - 1]
        if origen < destino:
            camino.sort(reverse=False)
        else:
            camino.sort(reverse=True)
        return camino

    def camino(self, origen, destino):
        predecesores = self.getPredecesoresREP(origen)
        actual = destino
        camino = []
        while actual != 0:
            camino.append(actual)

            actual = predecesores[actual - 1]

        if origen < destino:
            camino.sort(reverse=False)
        else:
            camino.sort(reverse=True)
        return camino