class Nota:
    def __init__(self,disciplina,student,nota:float):
        self.__disciplina=disciplina
        self.__student=student
        self.__nota=nota

    def disciplina(self):
        return self.__disciplina

    def student(self):
        return self.__student

    def nota(self):
        return self.__nota

    def __eq__(self, other):
        if type(self)!=type(other):
            return False
        return type(self)==type(other)

    def __str__(self):
        return str(self.__student)+" NOTA "+str(self.__nota)+"|"+str(self.__disciplina)
