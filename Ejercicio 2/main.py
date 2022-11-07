from Grafo import Grafo
from  GrafoEncadenao import GrafoEncadenao
if __name__ == '__main__':
    grafito = GrafoEncadenao(6)
    grafito.CrearArista(1, 5)
    grafito.CrearArista(1,2 )
    grafito.CrearArista(2,5)
    grafito.CrearArista(5,4)
    grafito.CrearArista(2,3)
    grafito.CrearArista(4,3)
    grafito.CrearArista(6,1)
    grafito.mostrar()
    #print(grafito.Adyacentes(1))
    #print(grafito.getCamino(1,6))
    print(grafito.camino(1,3))
    print(grafito.camino_minimo(1,1))
    grafito.Conexo()
