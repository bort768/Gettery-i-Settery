class Ocena:
    def set_ocena(self, o):
        self.__ocena = o
    def get_ocena(self):
        return self.__ocena
    @property
    def ocena(self):
        return self.__ocena

class Student(Ocena):

    def set_name(self, n):
        self.__name = n

    def get_name(self):
        return self.__name

    def display(self):
        print('Name: ', self.get_name())
        print('Ocena: ', self.get_ocena())
        print('Ocena przy pomocy @property :',self.ocena)

S = Student()
S.set_name('John')
S.set_ocena(4)
S.display()