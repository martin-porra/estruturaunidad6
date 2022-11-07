from Grafo import Grafo
if __name__ == '__main__':
    grafito = Grafo(4)
    grafito.CrearArista(1,2)
    grafito.CrearArista(2,3 )
    grafito.CrearArista(1,3)
    grafito.CrearArista(3,4)
    grafito.mostrar()
    print('La cantidad de puntos criticos es: ',grafito.getCantidadCriticos())
