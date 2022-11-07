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
             self.__matriz[v2-1][v1-1] = 1
        else:
            print('ERROR: Vertices no validos')

    def getVertice(self):
        return self.__cantidadV

    def Adyacentes(self,matriz, v):
        list = []
        if v < self.__cantidadV and v >= 0:
            for j in range(self.__cantidadV):
                if matriz[v][j] == 1:
                    list.append(j)
        return list
    def mostrar(self):
        print(self.__matriz)

    def Conexo(self, matriz, vertice):
        band = True
        i = 0
        while i < self.__cantidadV and band:
            if len(self.Adyacentes( matriz,i)) == 0 and i != vertice:
                band = False
            i += 1
        return band

    def getCantidadCriticos(self):
        count = 0
        for i in range(self.__cantidadV):
            arrAux = np.copy(self.__matriz)
            arrAux[i, :] = 0
            arrAux[:, i] = 0
            print(arrAux)
            if not self.Conexo(arrAux, i):
                count += 1
        return count
