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
        return f'Težina poljoprivrednog traktora : {self.t}, njegova namjena: {self.n}, model traktora :{self.m}, snaga njegovog motora:{self.s}'
    def __str__(self):
        return self.__repr__()


class Vinogradarski(Traktor):
    def __init__(self, težina, namjena, cijena, spremnik):
       
        super().__init__(težina, namjena)
        self.c=cijena
        self.spr=spremnik
    def __repr__(self):
        return f'Težina vinogradarskog traktora : {self.t}, njegova namjena: {self.n}, njegova cijena:{self.c}, kapacitet spremnika:{self.spr}'
    def __str__(self):
        return self.__repr__()

