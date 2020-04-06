class Kolor:
    def set_kolor(self, k):
        self.__kolor = k
    @property
    def kolor(self):
        return self.__kolor

class Samochod(Kolor):
    def set_marka(self, m):
        self.__marka = m

    @property
    def marka(self):
        return self.__marka

    def set_model(self, m_p):
        self.__model = m_p

    @property
    def model(self):
        return self.__model

    def set_cena(self, cena):
        self.__cena = cena

    @property
    def cena(self):
        return self.__cena


    def display(self):
        print('Marka:', self.marka)
        print('Model:', self.model)
        print('Kolor:',self.kolor)
        print('Cena:', self.cena)


S = Samochod()
S.set_marka('Volvo')
S.set_model('V40')
S.set_kolor('Czarny')
S.set_cena('130000 zł')
S.display()