class Bus:
    def __init__(self, namjena, kapacitet):
        
        self.n=namjena
        self.k=kapacitet
    def __repr__(self):
        return 'namjena (kapacitet):'+self.n+'( '+self.k + ')'
    def __str__(self):
        return self.__repr__()

class Gradski(Bus):
    def __init__(self, namjena, kapacitet, broj_linija, broj_stanica):
        
        super().__init__(namjena, kapacitet)
        self.l=broj_linija
        self.s=broj_stanica
    def __repr__(self):
        return f'Namjena gradskog busa: {self.n}, njegov kapacitet: {self.k}, broj linija koje voze:{self.l}, broj stanica na kojima staje:{self.s}'
    def __str__(self):
        return self.__repr__()


class Turistički(Bus):
    def __init__(self, namjena, kapacitet, vrsta_krova, wc):
       
        super().__init__(namjena, kapacitet)
        self.krov=vrsta_krova
        self.w=wc
    def __repr__(self):
        return f'Namjena turističkog busa: {self.n}, njegov kapacitet: {self.k}, vrsta krova:{self.krov}, ima li wc:{self.w}'
    def __str__(self):
        return self.__repr__()
