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


class Vinogradarski(Traktor):
    def __init__(self, težina, namjena, cijena, spremnik):
       
        super().__init__(težina, namjena)
        self.c=cijena
        self.spr=spremnik
    def __repr__(self):
        return f'Vinogradarski traktor težina: {self.t} namjena: {self.n} cijena:{self.c} spremnik:{self.spr}'
    def __str__(self):
        return self.__repr__()

