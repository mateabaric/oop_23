class Auto:
    def __init__(self,naziv, kapacitet):
        '''klasa za aktivnosti'''
        self.n=naziv
        self.k=kapacitet
    def __repr__(self):
        return 'Naziv (kapacitet):'+self.n+'( '+self.k + ')'
    def __str__(self):
        return self.__repr__()

class Pickup(Auto):
    def __init__(self, naziv, kapacitet,grad, cijena):
        '''nasljeđuje klasu Aktivnost'''
        super().__init__(naziv,kapacitet)
        self.g=grad
        self.c=cijena
    def __repr__(self):
        return f'Razgledavanje:{self.n} ({self.k},{self.g},{self.c})'
    def __str__(self):
        return self.__repr__()


class SUV(Auto):
    def __init__(self, naziv, kapacitet,polaziste, odrediste, cijena):
        '''nasljeđuje klasu Ucenik, ali dodaje rječnik matura koji ima oblik {'naziv predmeta na maturi':'razina A ili B'}'''
        super().__init__(naziv,kapacitet)
        self.p=polaziste
        self.o=odrediste
        self.c=cijena
    def __repr__(self):
        return f'Izlet:{self.n} ({self.k},{self.p}-{self.o},{self.c})'
    def __str__(self):
        return self.__repr__()


class Limuzina(Auto):
    def __init__(self, naziv, kapacitet,polaziste, odrediste, cijena):
        '''nasljeđuje klasu Ucenik, ali dodaje rječnik matura koji ima oblik {'naziv predmeta na maturi':'razina A ili B'}'''
        super().__init__(naziv,kapacitet)
        self.p=polaziste
        self.o=odrediste
        self.c=cijena
    def __repr__(self):
        return f'Izlet:{self.n} ({self.k},{self.p}-{self.o},{self.c})'
    def __str__(self):
        return self.__repr__()
