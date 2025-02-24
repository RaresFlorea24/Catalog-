from Domain.student import Student
from Domain.validation import ValidatorStudent
from Repository.repo_studenti import StudentRepoFile


class ServiceStudent:
    def __init__(self,repo,validator:ValidatorStudent):
        self.__repo=repo
        self.__validator=validator

    def adauga_student(self,id,nume):
        
        s=Student(id,nume)
        self.__validator.validate(s)
        self.__repo.store(s)

    def actualizeaza_student(self,id,nume):
        s=Student(id,nume)
        self.__validator.validate(s)
        self.__repo.update(s)

    def find_student(self,cod):
        
        return self.__repo.find(cod)

    def fill_studenti(self):
        return self.__repo.fill_studenti()

    def add_default(self):
        self.adauga_student(32451, "Mirel Rares")
        self.adauga_student(84251, "Popa Medeea")
        self.adauga_student(12345, "Popescu Dan")
        self.adauga_student(10000, "Ciolan Marian")
        self.adauga_student(99999, "Buta Pavel")


    def delete_student(self,id):
        student=self.find_student(id)
        return self.__repo.delete(student)

    def get_all(self):
        return self.__repo.get_all()