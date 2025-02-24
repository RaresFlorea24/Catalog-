from Domain.disciplina import Disciplina
import random

"""
class DisciplinaMemoryRepository:
    def __init__(self):
        self.__elements=[]

    def find(self,cod:int)->Disciplina|None:
        
        Cauta disciplina cu cod dat
        :param cod: cod-ul cautat
        :return: obiect de tip Disciplina daca exista disciplina cu acest cod, None altfel
        
        for disciplina in self.__elements:
            if disciplina.get_idDisciplina()==cod:
                return disciplina
        return None

    def store(self,disciplina:Disciplina):
        
        Adauga disciplina la lista de discipline
        :param disciplina: disciplina de adaugat
        :return: -;lista de discipline se modifica prin adaugarea disciplinei date
                postconditie: disciplina apartine listei de discipline
        :raises: ValueError daca se incearca adaugarea unei discipline care deja exista
        
        if self.find(disciplina.get_idDisciplina())is not None:
            raise ValueError("Exista deja disciplina cu acest ID")
        self.__elements.append(disciplina)

    def __find_pos(self,cod :int):
        pos=-1
        for index,disciplina in enumerate(self.__elements):
            if disciplina.get_idDisciplina()==cod:
                pos=index
                break
        return pos

    def update(self,disciplina_actualizata):

        pos=self.__find_pos(disciplina_actualizata.get_idDisciplina())
        if pos==-1:
            raise ValueError("Nu exista disciplina cu cod dat")
        self.__elements[pos]=disciplina_actualizata

    def delete(self,disciplina:Disciplina):
        disciplinadorita=self.find(disciplina.get_idDisciplina())
        if disciplinadorita is not None and disciplinadorita.get_idDisciplina() == disciplina.get_idDisciplina() and disciplinadorita.get_nume() == disciplina.get_nume() and disciplinadorita.get_profesor()== disciplina.get_profesor():
            self.__elements.remove(disciplinadorita)
        else:
            raise ValueError('Disciplina nu exista')

    def fill_discipline(self):
        discipline = []
        random.seed(6481)
        for i in range(random.randint(1, 20)):
            nume = ''
            for j in range(random.randint(2, 20)):
                nume += chr(random.randint(97, 122))
            prof=''
            for k in range(random.randint(2,20)):
                prof+=chr(random.randint(97,122))

            discipline.append(Disciplina(int(random.randint(100, 999)), nume, prof))

        return discipline

    def get_all(self)->list:
        return self.__elements

    def get_size(self):
        return len(self.__elements)
        """


class DisciplineRepoFile:
    def __init__(self, filename):
        self.__filename = filename

    def __load_from_file(self):
        lista = []
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    cod, nume, profesor = line.split(",")
                    cod = int(cod)
                    dis = Disciplina(cod, nume, profesor)
                    lista.append(dis)

            return lista

    def __save_to_file(self, discipline):
        with open(self.__filename, "w") as f:
            for disciplina in discipline:
                disc_str = str(
                    disciplina.get_idDisciplina()) + ", " + disciplina.get_nume() + ", " + disciplina.get_profesor() + "\n"
                f.write(disc_str)

    def find(self, cod: int) -> Disciplina | None:
        discipline = self.get_all()
        for disciplina in discipline:
            if disciplina.get_idDisciplina() == cod:
                return disciplina
        return None

    def store(self, disciplina: Disciplina):
        if self.find(disciplina.get_idDisciplina()) is not None:
            raise ValueError("Exista deja disciplina cu acest ID")
        discipline = self.get_all()
        discipline.append(disciplina)
        self.__save_to_file(discipline)

    def __find_pos(self, cod: int):
        discipline=self.get_all()
        pos = -1
        for index, disciplina in enumerate(discipline):
            if disciplina.get_idDisciplina() == cod:
                pos = index
                break
        return pos

    def update(self, disciplina_actualizata):
        dsicipline=self.get_all()
        pos = self.__find_pos(disciplina_actualizata.get_idDisciplina())
        if pos == -1:
            raise ValueError("Nu exista disciplina cu cod dat")
        dsicipline[pos] = disciplina_actualizata
        self.__save_to_file(dsicipline)

    def delete(self, disciplina: Disciplina):
        discipline = self.get_all()
        disciplinadorita = self.find(disciplina.get_idDisciplina())
        if disciplinadorita is not None and disciplinadorita.get_idDisciplina() == disciplina.get_idDisciplina() and disciplinadorita.get_nume() == disciplina.get_nume() and disciplinadorita.get_profesor() == disciplina.get_profesor():
            discipline.remove(disciplinadorita)
        else:
            raise ValueError('Disciplina nu exista')

    def fill_discipline(self):
        discipline = []
        random.seed(6481)
        for i in range(random.randint(1, 20)):
            nume = ''
            for j in range(random.randint(2, 20)):
                nume += chr(random.randint(97, 122))
            prof = ''
            for k in range(random.randint(2, 20)):
                prof += chr(random.randint(97, 122))

            discipline.append(Disciplina(int(random.randint(100, 999)), nume, prof))

        self.__save_to_file(discipline)

    def get_all(self):
        return self.__load_from_file()

    def get_size(self):
        return len(self.get_all())