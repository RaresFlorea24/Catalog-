from Domain.nota import Nota

class ServiceNota:
    def __init__(self,repo_discipline,repo_studenti,repo_note,validator_nota):
        self.__repo_discipline=repo_discipline
        self.__repo_studenti=repo_studenti
        self.__repo_note=repo_note
        self.__validator_nota=validator_nota

    def adauga_nota(self,id_disciplina,id_student,nota):
        disciplina=self.__repo_discipline.find(id_disciplina)
        if disciplina is None:
            raise ValueError("Nu exista disciplina cu ID-ul dat")

        student=self.__repo_studenti.find(id_student)
        if student is None:
            raise ValueError("Nu exista student cu ID-ul dat")

        scor=Nota(disciplina,student,nota)
        self.__validator_nota.validate(scor)
        self.__repo_note.store(scor)

    def find_nota(self,id_disciplina):
        return self.__repo_note.find(id_disciplina)

    def get_all(self):
        return self.__repo_note.get_all()

    @staticmethod
    def bubble_sort(arr, key=None, reverse=False):
        if key is None:
            key = lambda x: x

        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if (key(arr[j]) > key(arr[j + 1])) != reverse:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    @staticmethod
    def shell_sort(arr, key=None, reverse=False):
        if key is None:
            key = lambda x: x

        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and ((key(arr[j - gap]) > key(temp)) != reverse):
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

        return arr

    def calculeaza_medii(self, note):
        medii = {}
        for nota in note:
            if nota.student().get_nume() not in medii:
                medii[nota.student().get_nume()] = []
            medii[nota.student().get_nume()].append(nota.nota())

        for student in medii:
            medii[student] = sum(medii[student]) / len(medii[student])
        return medii

    def primii_20_la_suta(self, note):
        medii = self.calculeaza_medii(note)
        studenti_ordonati = self.bubble_sort(medii.items(), key=lambda x: x[1], reverse=True)
        top_20 = int(0.2 * len(studenti_ordonati))
        return studenti_ordonati[:top_20]