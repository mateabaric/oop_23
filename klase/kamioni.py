class Kamion:
    def __init__(self, dužina, namjena):
        
        self.d=dužina
        self.n=namjena
    def __repr__(self):
        return 'dužina (namjena):'+self.d+'( '+self.n + ')'
    def __str__(self):
        return self.__repr__()

class Šleper(Kamion):
    def __init__(self,  dužina, namjena, vrsta_robe, prikolica):
        
        super().__init__(dužina, namjena)
        self.r=vrsta_robe
        self.p=prikolica
    def __repr__(self):
        return f'Dužina šlepera: {self.d}, njegova namjena: {self.n}, vrsta robe koju prevozi:{self.r}, kakvu prikolicu ima:{self.p}'
    def __str__(self):
        return self.__repr__()


class Autotransporter(Kamion):
    def __init__(self, dužina, namjena, broj_katova, platforma):
       
        super().__init__(dužina, namjena)
        self.k=broj_katova
        self.plat=platforma
    def __repr__(self):
        return f'Dužina autotransportera: {self.d}, njegova namjena: {self.n}, koliko katova ima:{self.k}, kakva mu je platforma:{self.plat}'
    def __str__(self):
        return self.__repr__()
