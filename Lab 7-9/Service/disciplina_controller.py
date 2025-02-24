from Domain.disciplina import Disciplina
from Domain.validation import ValidatorDisciplina
from Repository.repo_discipline import DisciplineRepoFile


class ServiceDisciplina:
    def __init__(self, repo, validator: ValidatorDisciplina):
        self.__repo = repo
        self.__validator = validator

    def adauga_disciplina(self, cod, nume, profesor):
        """
        Adauga disciplina in lista de discipline
        :param cod:cod-ul noii discipline
        :param nume:numele disciplinei
        :param profesor:numele profesorului
        :return:-;lista data se modifica prin adaugarea disciplinei
        :raises: ValueError daca disciplina nu este valida
                 ValueError daca cod-ul disciplinei este deja folosit
        """
        d = Disciplina(cod, nume, profesor)
        self.__validator.validate(d)
        self.__repo.store(d)

    def actualizeaza_disciplina(self, cod, nume_nou, profesor_nou):
        """

        :param cod:
        :param nume_nou:
        :param profesor_nou:
        :return:
        """
        d_nou = Disciplina(cod, nume_nou, profesor_nou)
        self.__validator.validate(d_nou)
        self.__repo.update(d_nou)

    def find_disciplina(self, cod):
        """
        Cauta disciplina cu cod dat
        :param cod: cod-ul cautat
        :return: disciplina cautata,None daca nu exista
        """
        return self.__repo.find(cod)

    def fill_discipline(self):
        return self.__repo.fill_discipline()

    def add_default(self):
        self.adauga_disciplina(101, "Matematica", "Iliescu Vasile")
        self.adauga_disciplina(102, "Informatica", "Simion George")
        self.adauga_disciplina(103, "Limba romana", "Dancila Viorel")

    def delete_disciplina(self,cod,nume,prof):
        newDisc=Disciplina(cod,nume,prof)
        self.__validator.validate(newDisc)
        self.__repo.delete(newDisc)

    def get_all(self)->list:
        """
        Returneaza toata lista de discipline
        :return:
        """
        return self.__repo.get_all()
