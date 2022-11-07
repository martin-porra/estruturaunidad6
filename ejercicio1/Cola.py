class Nodo:
 __dato = None
 __Siguiente = None
 def __init__(self,dato):
     self.__dato = dato
     self.__Siguiente = None
 def setsiguiente(self,sig):
     self.__Siguiente = sig
 def getsiguiente(self):
     return self.__Siguiente
 def getdato(self):
     return self.__dato

class ColaEnlazada:
    __cant = None
    __pr = None
    __ul = None
    def __init__(self,xpr=None,xul=None,xcant=0):
        self.__pr =xpr
        self.__ul = xul
        self.__cant = xcant

    def vacia(self):
        return (self.__cant == 0)
    def insertar(self,x):
        ps1 = Nodo(x)
        if self.__ul == None:
            self.__pr=ps1
        else:
            self.__ul.setsiguiente(ps1)
        self.__ul = ps1
        self.__cant+=1

    def suprimir(self):
        aux = None
        x=None
        if self.vacia():
            print('Cola vacia')
            return 0
        else:
            aux = self.__pr
            x=self.__pr.getdato()
            self.__pr = self.__pr.getsiguiente()
            self.__cant-=1
            if self.__pr == None:
                self.__ul = None
            del aux
        return x
    def recorrer(self,aux):
        if aux == 1:
            aux = self.__pr
        if aux != None:
            print(aux.getdato())
            self.recorrer(aux.getsiguiente())