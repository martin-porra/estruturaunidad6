from Grafo import Grafo
from  GrafoEncadenao import GrafoEncadenao
if __name__ == '__main__':
    grafito = Grafo(6)
    grafito.CrearArista(1, 5)
    grafito.CrearArista(1,2 )
    grafito.CrearArista(2,5)
    grafito.CrearArista(5,4)
    grafito.CrearArista(2,3)
    grafito.CrearArista(4,3)
    grafito.CrearArista(6,4)
    grafito.mostrar()
    #print(grafito.Adyacentes())
    print(grafito.camino_minimo(1,2))
    print(grafito.camino(5, 6))
    print(grafito.REP(6))
    grafito.Conexo()
