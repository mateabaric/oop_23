class Traktor:
    def __init__(self, težina, namjena):
        
        self.t=težina
        self.n=namjena
    def __repr__(self):
        return 'težina (namjena):'+self.t+'( '+self.n + ')'
    def __str__(self):
        return self.__repr__()

class Poljoprivredni(Traktor):
    def __init__(self,  težina, namjena, model, snaga):
        
        super().__init__(težina, namjena)
        self.m=model
        self.s=snaga
    def __repr__(self):
        return f'Poljoprivredni traktor težina: {self.t} namjena: {self.n} model:{self.m} snaga:{self.s}'
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
