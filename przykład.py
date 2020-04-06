class Cat(object):
    def __init__(self, name):
        self.set_name(name)

    @property
    def name(self):
        return self.__name
    #setter
    def set_name(self, name):
        if name == 'Misia':
            self.__name = 'piekna kotka'
        elif name == 'Rudy':
            self.__name = 'piekny kocur'
        else:
            self.__name = 'piekne koty'
kotka = Cat('Misia')
print(kotka.name)
parakotow = Cat('Koty')
print(parakotow.name)