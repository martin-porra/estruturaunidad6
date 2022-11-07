import sys


class Tabla:
    __conocido = None
    __distancia = None
    __camino = None

    def __init__(self):
        self.__conocido = False
        self.__distancia = sys.maxsize
        self.__camino = None

    def getEstado(self):
        return self.__conocido

    def getDistancia(self):
        return self.__distancia

    def setConocido(self):
        self.__conocido = True

    def setDistancia(self, distancia):
        self.__distancia = distancia

    def setCamino(self, vertice):
        self.__camino = vertice

    def getCamino(self):
        return self.__camino

    def setDistancia(self, distancia):
        self.__distancia = distancia
