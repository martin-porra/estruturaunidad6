from Grafo import Grafo
if __name__ == '__main__':
    obj = Grafo(6)
    obj.CrearArista(0, 1)
    obj.CrearArista(0, 3)
    obj.CrearArista(1, 2)
    obj.CrearArista(1, 4)
    obj.CrearArista(1, 5)
    obj.CrearArista(2, 3)
    obj.CrearArista(3, 1)
    obj.CrearArista(4, 3)
    obj.CrearArista(4, 5)
    obj.CrearArista(5, 3)
    obj.CrearArista(5, 0)
    obj.Dijkstra(0, 4)