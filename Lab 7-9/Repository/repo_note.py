"""
class NoteMemoryRepository:
    def __init__(self):
        self.__note=[]

    def store(self,nota):
        self.__note.append(nota)

    def find(self,cod):
        for nota in self.__note:
            if nota.disciplina().get_idDisciplina()==cod:
                return nota
        return None

    def get_all(self):
        return self.__note
"""
from Domain.disciplina import Disciplina
from Domain.student import Student
from Domain.nota import Nota


class NoteRepoFile:
    def __init__(self, filename):
        self.__filename = filename

    def __load_from_file(self):
        lista = []
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    student, disciplina, nota = line.split("|")
                    student = student.strip()
                    idstudent, nume_stud = student.split(",")
                    idstudent = int(idstudent)
                    disciplina = disciplina.strip()
                    iddisciplina, nume_disc, prof = disciplina.split(",")
                    iddisciplina = int(iddisciplina)
                    stud = Student(idstudent, nume_stud)
                    disc = Disciplina(iddisciplina, nume_disc, prof)
                    nota = float(nota)
                    mark = Nota(stud, disc, nota)
                    lista.append(mark)

            return lista

    def __save_to_file(self, note):
        with open(self.__filename, "w") as f:
            for nota in note:
                nota_str = (
                        str(nota.student().get_IDstudent()) + "," +
                        nota.student().get_nume() + "| " +
                        str(nota.disciplina().get_idDisciplina()) + ", " +
                        nota.disciplina().get_nume() + ", " +
                        nota.disciplina().get_profesor() + "| " +
                        str(nota.nota()) + "\n"
                )
                f.write(nota_str)

    def find(self, cod):
        note=self.get_all()
        for nota in note:
            if nota.disciplina().get_idDisciplina() == cod:
                return nota
        return None

    def store(self, nota):
        note=self.get_all()
        note.append(nota)
        self.__save_to_file(note)

    def get_all(self):
        return self.__load_from_file()