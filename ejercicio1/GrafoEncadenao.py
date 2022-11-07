import numpy as np
from Cola import ColaEnlazada
from Lista import  ListaEncadenada
class GrafoEncadenao:
    __cantidadV =None
    __arreglo = None

    def __init__(self, cantidad_vertices):
        self.__arreglo = np.empty(cantidad_vertices, dtype=ListaEncadenada)
        self.__cantidadV = cantidad_vertices
        for i in range(self.__cantidadV):
            lista_adyacencia = ListaEncadenada()
            self.__arreglo[i] = lista_adyacencia

    def CrearArista(self, v1, v2):
        if (v1 <= self.__cantidadV and v2 <= self.__cantidadV) and (v1 >= 1 and v2 >= 1):
            p1 = self.__arreglo[v1 - 1].getTamanio()
            p2 = self.__arreglo[v2 - 1].getTamanio()
            self.__arreglo[v1 - 1].insertar(v2 - 1, p1)
            self.__arreglo[v2 - 1].insertar(v1 - 1, p2)

        else:
            print('ERROR: Vertices no validos')

    def Adyacentes(self, vertice):
        lista = None
        if vertice >= 0 and vertice < self.__cantidadV:
            lista = self.__arreglo[vertice].getVertices()

        else:
            print('Error: vertice no valido')
        return lista

    def mostrar(self):
        for i in range(self.__cantidadV):
            print(str(i+1) + ' -> '+ str(self.__arreglo[i].mostrar()))

    def getCamino(self, inicio, fin):
        print('a')
        d = np.zeros(self.__cantidadV, dtype=int)
        resultado = self.buscarCamino(inicio, fin, d)
        if isinstance(resultado, list):
            resultado.insert(0, inicio)
        return resultado

    def buscarCamino(self, nodo_origen, nodo_destino, d):
        d[nodo_origen] = 1
        adys = self.Adyacentes(nodo_origen-1)
        for nodos in adys:
            print('a')
            if nodos == nodo_destino:
                return [nodo_destino]
            if d[nodos] == 0:
                retorno = self.buscarCamino(nodos, nodo_destino, d)
                if isinstance(retorno, list):
                    retorno.insert(0, nodos)
                    return retorno
        return 0

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

    def Conexo(self):
        band = True
        for i in range(self.__cantidadV):
            if len(self.Adyacentes(i)) == 0:
                band = False
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

    def Ciclico(self, actual, arreglo=None, recorrido=None, ciclico=None, iniciar=False):
        if not iniciar:
            if actual - 1 >= 0 and actual - 1 < self.__cantidadV:
                arreglo = np.zeros(self.__cantidadV, dtype=int)
                recorrido = []
                ciclico = self.Ciclico(actual=actual - 1, arreglo=arreglo, recorrido=recorrido, ciclico=ciclico,
                                       iniciar=True)
            else:
                print('ERROR: vertice  origen no valido')
                return None
        else:
            if ciclico == True:
                return ciclico
            recorrido.append(actual + 1)
            arreglo[actual] = 1
            adyacentes = self.Adyacentes(actual)
            for adyacente in adyacentes:
                if arreglo[adyacente] == 0:
                    ciclico = self.Ciclico(adyacente, arreglo=arreglo, recorrido=recorrido, ciclico=ciclico,
                                           iniciar=True)
                elif len(recorrido) >= 3:
                    ciclico = True
        return