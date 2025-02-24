"""
import unittest
from Domain.student import Student
from Domain.disciplina import Disciplina
from Service.nota_controller import ServiceNota
from Repository.repo_discipline import DisciplineRepoFile
from Repository.repo_studenti import StudentRepoFile
from Repository.repo_note import NoteRepoFile
from Domain.validation import ValidatorNota


class TestServiceNota(unittest.TestCase):
    def setUp(self) -> None:
        # Initialize actual repositories
        self.repo_discipline = DisciplineRepoFile("test_discipline_service.txt")
        self.repo_studenti = StudentRepoFile("test_studenti_service.txt")
        self.repo_note = NoteRepoFile("test_note_service.txt")
        self.validator_nota = ValidatorNota()

        # Add test data to repositories
        self.disciplina = Disciplina(101, "Matematica", "Iliescu Vasile")
        self.student = Student(12345, "Popescu Dan")
        self.repo_discipline.store(self.disciplina)
        self.repo_studenti.store(self.student)

        # Initialize the service
        self.service = ServiceNota(
            self.repo_discipline, self.repo_studenti, self.repo_note, self.validator_nota
        )

    def tearDown(self) -> None:
        # Clean up repositories after each test
        pass

    def test_adauga_nota_valid(self):
        self.service.adauga_nota(101, 12345, 9.5)
        all_notes = self.service.get_all()
        self.assertEqual(len(all_notes), 1)
        self.assertEqual(all_notes[0].nota, 9.5)

    def test_adauga_nota_invalid_disciplina(self):
        with self.assertRaises(ValueError) as context:
            self.service.adauga_nota(999, 12345, 9.5)
        self.assertEqual(str(context.exception), "Nu exista disciplina cu ID-ul dat")

    def test_adauga_nota_invalid_student(self):
        with self.assertRaises(ValueError) as context:
            self.service.adauga_nota(101, 99999, 9.5)
        self.assertEqual(str(context.exception), "Nu exista student cu ID-ul dat")

    def test_adauga_nota_invalid_value(self):
        with self.assertRaises(ValueError) as context:
            self.service.adauga_nota(101, 12345, 11)  # Invalid grade
        self.assertEqual(str(context.exception), "Nota trebuie să fie între 1 și 10")

    def test_find_nota(self):
        self.service.adauga_nota(101, 12345, 8.0)
        nota = self.service.find_nota(101)
        self.assertIsNotNone(nota)
        self.assertEqual(nota.nota, 8.0)

    def test_get_all_notes(self):
        self.service.adauga_nota(101, 12345, 8.0)
        self.service.adauga_nota(101, 12345, 9.5)
        all_notes = self.service.get_all()
        self.assertEqual(len(all_notes), 2)
        self.assertEqual(all_notes[0].nota, 8.0)
        self.assertEqual(all_notes[1].nota, 9.5)


if __name__ == "__main__":
    unittest.main()
"""
from Domain.student import Student
from Domain.disciplina import Disciplina
from Repository.repo_discipline import DisciplineRepoFile
from Repository.repo_studenti import StudentRepoFile
from Repository.repo_note import NoteRepoFile
from Domain.validation import ValidatorNota
from Service.nota_controller import ServiceNota


def test_adauga_nota():
    repo_discipline = DisciplineRepoFile("test_discipline_service.txt")
    repo_studenti = StudentRepoFile("test_studenti_service.txt")
    repo_note = NoteRepoFile("test_note_service.txt")
    validator_nota = ValidatorNota()

    service = ServiceNota(repo_discipline, repo_studenti, repo_note, validator_nota)

    disciplina = Disciplina(101, "Matematica", "Iliescu Vasile")
    student = Student(12345, "Popescu Dan")
    repo_discipline.store(disciplina)
    repo_studenti.store(student)

    # Adăugăm o notă validă
    service.adauga_nota(101, 12345, 9.5)
    all_notes = service.get_all()
    assert len(all_notes) == 1
    assert all_notes[0].nota == 9.5

    # Încercăm să adăugăm o notă cu disciplină inexistentă
    try:
        service.adauga_nota(999, 12345, 8.0)
        assert False
    except ValueError as e:
        assert str(e) == "Nu exista disciplina cu ID-ul dat"

    # Încercăm să adăugăm o notă cu student inexistent
    try:
        service.adauga_nota(101, 99999, 7.0)
        assert False
    except ValueError as e:
        assert str(e) == "Nu exista student cu ID-ul dat"

    # Încercăm să adăugăm o notă invalidă
    try:
        service.adauga_nota(101, 12345, 11)
        assert False
    except ValueError as e:
        assert str(e) == "Nota trebuie să fie între 1 și 10"


def test_find_nota():
    repo_discipline = DisciplineRepoFile("test_discipline_service.txt")
    repo_studenti = StudentRepoFile("test_studenti_service.txt")
    repo_note = NoteRepoFile("test_note_service.txt")
    validator_nota = ValidatorNota()

    service = ServiceNota(repo_discipline, repo_studenti, repo_note, validator_nota)

    disciplina = Disciplina(101, "Matematica", "Iliescu Vasile")
    student = Student(12345, "Popescu Dan")
    repo_discipline.store(disciplina)
    repo_studenti.store(student)

    service.adauga_nota(101, 12345, 8.5)
    nota = service.find_nota(101)
    assert nota is not None
    assert nota.nota == 8.5

    # Încercăm să găsim o notă pentru o disciplină inexistentă
    assert service.find_nota(999) is None


def test_get_all_notes():
    repo_discipline = DisciplineRepoFile("test_discipline_service.txt")
    repo_studenti = StudentRepoFile("test_studenti_service.txt")
    repo_note = NoteRepoFile("test_note_service.txt")
    validator_nota = ValidatorNota()

    service = ServiceNota(repo_discipline, repo_studenti, repo_note, validator_nota)

    disciplina = Disciplina(101, "Matematica", "Iliescu Vasile")
    student = Student(12345, "Popescu Dan")
    repo_discipline.store(disciplina)
    repo_studenti.store(student)

    service.adauga_nota(101, 12345, 7.0)
    service.adauga_nota(101, 12345, 8.0)

    all_notes = service.get_all()
    assert len(all_notes) == 2
    assert all_notes[0].nota == 7.0
    assert all_notes[1].nota == 8.0

    def test_bubble_sort():
        data_numbers = [5, 2, 9, 1, 5, 6]
        data_strings = ["banana", "apple", "cherry"]
        data_objects = [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 20},
            {"name": "Charlie", "age": 23}
        ]

        # Test sorting numbers
        sorted_numbers = SortingMethods.bubble_sort(data_numbers.copy())
        assert sorted_numbers == [1, 2, 5, 5, 6, 9]

        # Test sorting strings
        sorted_strings = SortingMethods.bubble_sort(data_strings.copy())
        assert sorted_strings == ["apple", "banana", "cherry"]

        # Test sorting objects by age
        sorted_objects = SortingMethods.bubble_sort(data_objects.copy(), key=lambda x: x["age"])
        assert sorted_objects == [
            {"name": "Bob", "age": 20},
            {"name": "Charlie", "age": 23},
            {"name": "Alice", "age": 25}
        ]

        # Test reverse sorting
        sorted_numbers_desc = SortingMethods.bubble_sort(data_numbers.copy(), reverse=True)
        assert sorted_numbers_desc == [9, 6, 5, 5, 2, 1]

    def test_shell_sort():
        data_numbers = [5, 2, 9, 1, 5, 6]
        data_strings = ["banana", "apple", "cherry"]
        data_objects = [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 20},
            {"name": "Charlie", "age": 23}
        ]

        # Test sorting numbers
        sorted_numbers = SortingMethods.shell_sort(data_numbers.copy())
        assert sorted_numbers == [1, 2, 5, 5, 6, 9]

        # Test sorting strings
        sorted_strings = SortingMethods.shell_sort(data_strings.copy())
        assert sorted_strings == ["apple", "banana", "cherry"]

        # Test sorting objects by age
        sorted_objects = SortingMethods.shell_sort(data_objects.copy(), key=lambda x: x["age"])
        assert sorted_objects == [
            {"name": "Bob", "age": 20},
            {"name": "Charlie", "age": 23},
            {"name": "Alice", "age": 25}
        ]

        # Test reverse sorting
        sorted_numbers_desc = SortingMethods.shell_sort(data_numbers.copy(), reverse=True)
        assert sorted_numbers_desc == [9, 6, 5, 5, 2, 1]

    class SortingMethods:
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

    if __name__ == "__main__":
        test_bubble_sort()
        print("Bubble sort tests passed!")

        test_shell_sort()
        print("Shell sort tests passed!")

