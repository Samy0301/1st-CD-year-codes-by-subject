class Nodo:
    def __init__(self, value):
        self.v=value

    def add(self, n:Nodo ):
        self.prox=n

    def _iter__(self): #iterador
        return self

    def __next__(self):
        return self.prox

class Linkedlist:
    def __init__(self, head:Nodo):
        self.head=head

    def __iter__(self): #generador
        return self.head

    def add(self, x:Nodo, pos:int):
        n=self.__iter__()
        while pos==1:
            n=n.__next__()
        x.add(n.__next__())
        n.add(x)
