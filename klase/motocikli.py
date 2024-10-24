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
        self.s=snaga_motora
        self.m=marka
    def __repr__(self):
        return f'Sportski motocikl brzina: {self.b} cijena: {self.c} snaga_motora:{self.s} marka:{self.m}'
    def __str__(self):
        return self.__repr__()


class Cruiser(Motocikl):
    def __init__(self, brzina, cijena, visina, godina_proizvodnje):
       
        super().__init__(brzina, cijena)
        self.v=visina
        self.g=godina_proizvodnje
    def __repr__(self):
        return f'Cruiser motocikl brzina: {self.b} cijena: {self.c} visina:{self.v} godina_proizvodnje:{self.g}'
    def __str__(self):
        return self.__repr__()


class Skuter(Motocikl):
    def __init__(self, brzina, cijena, težina, boja):
 
        super().__init__(brzina, cijena)
        self.t=težina
        self.boja=boja
    def __repr__(self):
       return f'Skuter brzina: {self.b} cijena: {self.c} težina:{self.t} boja:{self.boja}'
    def __str__(self):
        return self.__repr__()
