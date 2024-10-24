class Bicikl:
    def __init__(self, namjena, način_pogona):
        
        self.n=namjena
        self.p=način_pogona
    def __repr__(self):
        return 'namjena (način_pogona):'+self.n+'( '+self.p + ')'
    def __str__(self):
        return self.__repr__()

class Cestovni(Bicikl):
    def __init__(self, namjena, način_pogona, broj_linija, broj_stanica):
        
        super().__init__(namjena, način_pogona)
        self.l=broj_linija
        self.s=broj_stanica
    def __repr__(self):
        return f'Gradski bus namjena: {self.n} kapacitet: {self.k} broj_linija:{self.l} broj_stanica:{self.s}'
    def __str__(self):
        return self.__repr__()


class Turistički(Bus):
    def __init__(self, namjena, način_pogona, vrsta_krova, wc):
       
        super().__init__(namjena, način_pogona)
        self.krov=vrsta_krova
        self.w=wc
    def __repr__(self):
        return f'Turistički bus namjena: {self.n} kapacitet: {self.k} vrsta_krova:{self.krov} wc:{self.w}'
    def __str__(self):
        return self.__repr__()


class Školski(Bus):
    def __init__(self, namjena, način_pogona, težina, boja):
 
        super().__init__(namjena, način_pogona)
        self.t=težina
        self.boja=boja
    def __repr__(self):
       return f'Skuter brzina: {self.b} cijena: {self.c} težina:{self.t} boja:{self.boja}'
    def __str__(self):
        return self.__repr__()
