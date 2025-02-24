from Domain.student import Student
import random

"""
class StudentMemoryRepository:
    def __init__(self):
        self.__elements = []

    def find(self, cod: int):
        for student in self.__elements:
            if student.get_IDstudent() == cod:
                return student
        return None

    def store(self, student: Student):
        
        if self.find(student.get_IDstudent()) is not None:
            raise ValueError("Exista deja student cu acest ID")
        self.__elements.append(student)

    def update(self, student_actualizat):

        pos = self.__find_pos(student_actualizat.get_IDstudent())
        if pos == -1:
            raise ValueError("Nu exista student cu cod dat")
        self.__elements[pos] = student_actualizat

    def __find_pos(self, cod: int):
        
        pos = -1
        for index, student in enumerate(self.__elements):
            if student.get_IDstudent() == cod:
                pos = index
                break
        return pos

    def delete(self, student):
        student_dorit = self.find(student.get_IDstudent())
        if student_dorit is not None and student_dorit.get_IDstudent() == student.get_IDstudent() and student_dorit.get_nume() == student.get_nume():
            self.__elements.remove(student_dorit)
        else:
            raise ValueError('Studentul nu exista')

    def fill_studenti(self):
        studenti = []
        random.seed(6481)
        for i in range(random.randint(1, 20)):
            nume = ''
            for j in range(random.randint(2, 20)):
                nume += chr(random.randint(97, 122))

            studenti.append(Student(int(random.randint(10000, 99999)), nume))

        return studenti

    def get_all(self):
        return self.__elements

    def size(self):
        return len(self.__elements)

"""
class StudentRepoFile:
    def __init__(self, filename):
        self.__filename = filename

    def __load_from_file(self):
        lista = []
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    cod, nume = line.split(",")
                    cod = int(cod)
                    stud = Student(cod, nume)
                    lista.append(stud)

            return lista

    def __save_to_file(self, studenti):
        with open(self.__filename, "w") as f:
            for student in studenti:
                stud_str = str(student.get_IDstudent()) + ", " + student.get_nume() + "\n"
                f.write(stud_str)

    def find(self, cod:int) -> Student|None:
        studenti=self.get_all()
        for student in studenti:
            if student.get_IDstudent() == cod:
                return student
        return None

    def store(self, student: Student):
        studenti=self.get_all()
        if self.find(student.get_IDstudent()) is not None:
            raise ValueError("Exista deja student cu acest ID")
        studenti.append(student)
        self.__save_to_file(studenti)

    def update(self, student_actualizat):
        studenti=self.get_all()
        pos = self.__find_pos(student_actualizat.get_IDstudent())
        if pos == -1:
            raise ValueError("Nu exista student cu cod dat")
        studenti[pos] = student_actualizat
        self.__save_to_file(studenti)

    def __find_pos(self, cod: int):
        studenti=self.get_all()
        pos = -1
        for index, student in enumerate(studenti):
            if student.get_IDstudent() == cod:
                pos = index
                break
        return pos

    def delete(self, student):
        studenti=self.get_all()
        student_dorit = self.find(student.get_IDstudent())
        if student_dorit is not None and student_dorit.get_IDstudent() == student.get_IDstudent() and student_dorit.get_nume() == student.get_nume():
            studenti.remove(student_dorit)
        else:
            raise ValueError('Studentul nu exista')
        self.__save_to_file(studenti)

    def fill_studenti(self):
        studenti = self.get_all()  # Load existing students
        used_ids = {student.get_IDstudent() for student in studenti}  # Store existing IDs

        for _ in range(random.randint(1, 20)):
            nume = ''.join(chr(random.randint(97, 122)) for _ in range(random.randint(2, 20)))

            id_student = random.randint(10000, 99999)
            while id_student in used_ids:  # Ensure ID does not exist
                id_student = random.randint(10000, 99999)

            used_ids.add(id_student)
            studenti.append(Student(id_student, nume))

        self.__save_to_file(studenti)
        return studenti

    def get_all(self):
        return self.__load_from_file()

    def size(self):
        return len(self.get_all())