class Disciplina:
    def __init__(self, idDisciplina: int, nume: str, profesor: str):
        self.__idDisciplina = idDisciplina
        self.__nume = nume
        self.__profesor = profesor

    def get_idDisciplina(self):
        return self.__idDisciplina

    def get_nume(self):
        return self.__nume

    def get_profesor(self):
        return self.__profesor

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.get_idDisciplina() == other.get_idDisciplina()

    def __str__(self):
        return "[" + str(self.__idDisciplina) + "] Disciplina: " + self.__nume + " | Profesor: " + self.__profesor
