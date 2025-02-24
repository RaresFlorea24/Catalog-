import unittest
from Domain.nota import Nota
from Domain.student import Student
from Domain.disciplina import Disciplina

class TestNota(unittest.TestCase):
    def setUp(self) -> None:
        self.disciplina = Disciplina(101, "Matematica", "Iliescu Vasile")
        self.student = Student(12345, "Popescu Dan")
        self.nota = Nota(self.disciplina, self.student, 9.5)

    def test_get_disciplina(self):

        self.assertEqual(self.nota.disciplina(), self.disciplina)

    def test_get_student(self):

        self.assertEqual(self.nota.student(), self.student)

    def test_get_nota(self):

        self.assertEqual(self.nota.nota(), 9.5)

    def test_eq(self):
        nota2 = Nota(self.disciplina, self.student, 9.5)
        self.assertEqual(self.nota, nota2)  # Obiectele sunt de același tip și sunt egale


    def tearDown(self) -> None:
        pass

if __name__ == "__main__":
    unittest.main()
