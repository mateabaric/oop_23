class Bicikl:
    def __init__(self, namjena, način_pogona):
        
        self.n=namjena
        self.p=način_pogona
    def __repr__(self):
        return 'namjena (način_pogona):'+self.n+'( '+self.p + ')'
    def __str__(self):
        return self.__repr__()

class Cestovni(Bicikl):
    def __init__(self, namjena, način_pogona, boja, broj_brzina):
        
        super().__init__(namjena, način_pogona)
        self.b=boja
        self.br=broj_brzina
    def __repr__(self):
        return f'Cestovni bicikl namjena: {self.n} način_pogona: {self.p} boja:{self.b} broj_brzina:{self.br}'
    def __str__(self):
        return self.__repr__()


class BMX(Bicikl):
    def __init__(self, namjena, način_pogona, brzina, tip):
       
        super().__init__(namjena, način_pogona)
        self.brz=brzina
        self.tip=tip
    def __repr__(self):
       return f'BMX bicikl namjena: {self.n} način_pogona: {self.p} brzina:{self.brz} tip:{self.tip}'
    def __str__(self):
        return self.__repr__()


class Dječji(Bus):
    def __init__(self, namjena, način_pogona, broj_kotača, visina):
 
        super().__init__(namjena, način_pogona)
        self.k=broj_kotača
        self.v=visina
    def __repr__(self):
       return f'Dječji bicikl namjena: {self.n} način_pogona: {self.p} broj_kotača:{self.k} visina:{self.v}'
    def __str__(self):
        return self.__repr__()
