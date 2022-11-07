from Grafo import Grafo
if __name__ == '__main__':
    obj = Grafo(6)
    obj.CrearArista(0, 1, 3)
    obj.CrearArista(0, 3, 6)
    obj.CrearArista(1, 2, 1)
    obj.CrearArista(1, 4, 1)
    obj.CrearArista(1, 5, 2)
    obj.CrearArista(2, 3, 2)
    obj.CrearArista(3, 1, 3)
    obj.CrearArista(4, 3, 3)
    obj.CrearArista(4, 5, 2)
    obj.CrearArista(5, 3, 1)
    obj.CrearArista(5, 0, 5)
    obj.Dijkstra(0, 4)  # camino mas corto de A a D