class Auto:
    def __init__(self,broj_kotača, namjena):
        
        self.k=broj_kotača
        self.n=namjena
    def __repr__(self):
        return 'broj kotača (namjena):'+self.k+'( '+self.n + ')'
    def __str__(self):
        return self.__repr__()

class Pickup(Auto):
    def __init__(self, broj_kotača, namjena, broj_vrata, kapacitet):
        
        super().__init__(broj_kotača, namjena)
        self.v=broj_vrata
        self.kap=kapacitet
    def __repr__(self):
        return f'Pickup broj  kotača: {self.k} namjena: {self.n} broj vrata:{self.v} kapacitet:{self.kap}'
    def __str__(self):
        return self.__repr__()


class SUV(Auto):
    def __init__(self, broj_kotača, namjena, cijena, visina):
       
        super().__init__(broj_kotača, namjena)
        self.c=cijena
        self.vis=visina
    def __repr__(self):
        return f'SUV broj  kotača: {self.k} namjena: {self.n} cijena:{self.c} visina:{self.vis}'
    def __str__(self):
        return self.__repr__()


class Limuzina(Auto):
    def __init__(self, broj_kotača, namjena, dužina, boja):
 
        super().__init__(broj_kotača, namjena)
        self.d=dužina
        self.b=boja
    def __repr__(self):
        return f'Limuzina broj  kotača: {self.k} namjena: {self.n} dužina:{self.d} boja:{self.b}'
    def __str__(self):
        return self.__repr__()
