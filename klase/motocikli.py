class Motocikl:
    def __init__(self, brzina, cijena):
        
        self.b=brzina
        self.c=cijena
    def __repr__(self):
        return 'brzina (cijena):'+self.b+'( '+self.c + ')'
    def __str__(self):
        return self.__repr__()

class Sportski(Motocikl):
    def __init__(self, brzina, cijena, snaga_motora, marka):
        
        super().__init__(brzina, cijena)
        self.r=vrsta_robe
        self.p=prikolica
    def __repr__(self):
        return f'Šleper dužina: {self.d} namjena: {self.n} vrsta_robe:{self.r} prikolica:{self.p}'
    def __str__(self):
        return self.__repr__()


class Autotransporter(Kamion):
    def __init__(self, težina, namjena, broj_katova, platforma):
       
        super().__init__(težina, namjena)
        self.k=broj_katova
        self.plat=platforma
    def __repr__(self):
        return f'Autotransporter dužina: {self.d} namjena: {self.n} broj_katova:{self.k} platforma:{self.plat}'
    def __str__(self):
        return self.__repr__()


class Cisterna(Kamion):
    def __init__(self, broj_kotača, namjena, tekućina, kapacitet):
 
        super().__init__(težina, namjena)
        self.tek=tekućina
        self.kap=kapacitet
    def __repr__(self):
        return f'Cisterna dužina: {self.d} namjena: {self.n} tekućina:{self.tek} kapacitet:{self.kap}'
    def __str__(self):
        return self.__repr__()
