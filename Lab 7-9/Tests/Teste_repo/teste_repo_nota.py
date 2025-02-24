from Domain.nota import Nota
from Domain.student import Student
from Domain.disciplina import Disciplina
from Repository.repo_note import NoteRepoFile

"""
def test_store_repo_nota():
    repo = NoteMemoryRepository()
    assert len(repo.get_all()) == 0

    disciplina = Disciplina(1, "Matematica", "Popescu")
    student = Student(101, "Ionescu")
    nota1 = Nota(disciplina, student, 8.5)

    repo.store(nota1)
    assert len(repo.get_all()) == 1

    # Test duplicat (ar trebui permis, deoarece repo-ul nu previne duplicatele)
    nota2 = Nota(disciplina, student, 9.5)
    repo.store(nota2)
    assert len(repo.get_all()) == 2


def test_find_repo_nota():
    repo = NoteMemoryRepository()

    disciplina1 = Disciplina(1, "Matematica", "Popescu")
    disciplina2 = Disciplina(2, "Fizica", "Ionescu")
    student = Student(101, "Ionescu")
    nota1 = Nota(disciplina1, student, 8.5)
    nota2 = Nota(disciplina2, student, 9.0)

    repo.store(nota1)
    repo.store(nota2)

    # Găsim nota asociată disciplinei 1
    found_nota = repo.find(1)
    assert found_nota is not None
    assert found_nota.disciplina().get_nume() == "Matematica"

    # Nu găsim nota asociată disciplinei inexistente
    assert repo.find(3) is None


def test_get_all_repo_nota():
    repo = NoteMemoryRepository()

    disciplina1 = Disciplina(1, "Matematica", "Popescu")
    disciplina2 = Disciplina(2, "Fizica", "Ionescu")
    student1 = Student(101, "Ionescu")
    student2 = Student(102, "Popescu")
    nota1 = Nota(disciplina1, student1, 8.5)
    nota2 = Nota(disciplina2, student2, 9.0)

    repo.store(nota1)
    repo.store(nota2)

    # Obținem toate notele
    all_notes = repo.get_all()
    assert len(all_notes) == 2
    assert all_notes[0].nota() == 8.5
    assert all_notes[1].nota() == 9.0
"""

import unittest
import os
from Domain.student import Student
from Domain.disciplina import Disciplina
from Domain.nota import Nota
from Repository.repo_note import NoteRepoFile


class TestNoteRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.test_filename = "test_note.txt.txt"
        with open(self.test_filename, "w") as f:
            f.write("1,John Doe| 101,Math,Dr. Smith| 9.5\n")
            f.write("2,Jane Roe| 102,Physics,Dr. Brown| 8.0\n")

        self.repo = NoteRepoFile(self.test_filename)

    """
    def test_get_all(self):
        notes = self.repo.get_all()
        self.assertEqual(len(notes), 2)

        # Validate first note

        self.assertEqual(notes[0].disciplina().get_idDisciplina(), 101)
        self.assertEqual(notes[0].disciplina().get_nume(), "Math")
        self.assertEqual(notes[0].disciplina().get_profesor(), "Dr. Smith")

        # Validate second note
        self.assertEqual(notes[1].disciplina().get_idDisciplina(), 102)
        self.assertEqual(notes[1].disciplina().get_nume(), "Physics")
        self.assertEqual(notes[1].disciplina().get_profesor(), "Dr. Brown")

    
    def test_store(self):
        student = Student(3, "Alice Smith")
        disciplina = Disciplina(103, "Chemistry", "Dr. Green")
        nota = Nota(student, disciplina, 7.5)

        initial_size = len(self.repo.get_all())
        self.repo.store(nota)
        notes = self.repo.get_all()

        self.assertEqual(len(notes), initial_size + 1)
        self.assertEqual(notes[-1].disciplina().get_idDisciplina(), 103)
        self.assertEqual(notes[-1].disciplina().get_nume(), "Chemistry")
        self.assertEqual(notes[-1].disciplina().get_profesor(), "Dr. Green")
        """


    def test_save_to_file(self):
        student = Student(4, "Mark Johnson")
        disciplina = Disciplina(104, "Biology", "Dr. Adams")
        nota = Nota(student, disciplina, 10.0)

        #self.repo.store(nota)

        with open(self.test_filename, "r") as f:
            lines = f.readlines()

        self.assertEqual(len(lines), 2)  # Initial 2 notes + 1 new note

    def tearDown(self) -> None:
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

if __name__ == "__main__":
    unittest.main()