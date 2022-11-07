import sys
import numpy as np
from Tabla import Tabla


class Grafo:
    __matrizAdyacencia = None
    __cantVertices = None

    def __init__(self, cantVertices):
        self.__matrizAdyacencia = np.zeros((cantVertices, cantVertices), dtype=int)
        self.__cantVertices = cantVertices

    def CrearArista(self, v1, v2, ):
        if (v1 >= 0 and v1 < self.__cantVertices) and (v2 >= 0 and v2 < self.__cantVertices):
            self.__matrizAdyacencia[v1][v2] = 1
        else:
            print('ERROR: Vertice/s no valido/s')

    def mostrarMatriz(self):
        print(self.__matrizAdyacencia)

    def getVertice(self, Tabla):
        v = 0
        mindist = sys.maxsize
        for i in range(len(Tabla)):
            if Tabla[i].getEstado() == False and Tabla[i].getDistancia() < mindist:
                v = i
                mindist = Tabla[i].getDistancia()
        return v

    def Adyacentes(self, v):
        list = []
        if v < self.__cantVertices and v >= 0:
            for j in range(self.__cantVertices):
                if self.__matrizAdyacencia[v][j] == 1:
                    list.append(j)
        return list

    def Dijkstra(self, origen, destino):
        Tablas = np.empty(self.__cantVertices, dtype=Tabla)
        for i in range(self.__cantVertices):
            Tablas[i] = Tabla()
        v = origen
        Tablas[origen].setDistancia(0)
        for i in range(self.__cantVertices):
            v = self.getVertice(Tablas)
            Tablas[v].setConocido()
            for w in self.Adyacentes(v):
                if Tablas[w].getEstado() == False:
                    if (Tablas[v].getDistancia() + self.__matrizAdyacencia[v][w]) < Tablas[w].getDistancia():
                        Tablas[w].setDistancia(Tablas[v].getDistancia() + self.__matrizAdyacencia[v][w])
                        Tablas[w].setCamino(v)
        v = destino
        camino = [v]
        # print(Tablas[v].getCamino())
        while Tablas[v].getCamino() != None:
            v = Tablas[v].getCamino()
            camino.insert(0, v)
        print(camino)


