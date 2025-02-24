
class Student:
    def __init__(self, IDstudent: int, nume: str):
        self.__IDstudent = IDstudent
        self.__nume = nume
        self.__medie = 0

    def get_IDstudent(self):
        return self.__IDstudent

    def get_nume(self):
        return self.__nume

    def get_medie(self):
        return self.__medie


    def nume(self,new_name):
        self.__nume=new_name

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.get_IDstudent() == other.get_IDstudent()

    def __str__(self):
        return "[" + str(self.get_IDstudent()) + "] Student: " + self.get_nume()
