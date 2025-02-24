import unittest
from Domain.disciplina import Disciplina

class TestDisciplina(unittest.TestCase):
    def setUp(self) -> None:
        # Configurare inițială pentru fiecare test
        self.disciplina = Disciplina(101, "Matematica", "Iliescu Vasile")

    def test_get_idDisciplina(self):
        self.assertEqual(self.disciplina.get_idDisciplina(), 101)

    def test_get_nume(self):
        self.assertEqual(self.disciplina.get_nume(), "Matematica")

    def test_get_profesor(self):
        self.assertEqual(self.disciplina.get_profesor(), "Iliescu Vasile")

    def test_eq(self):
        disciplina2 = Disciplina(101, "Fizica", "Popescu Ion")
        disciplina3 = Disciplina(102, "Chimie", "Popescu Ion")
        self.assertEqual(self.disciplina, disciplina2)  # ID-urile sunt la fel, deci obiectele sunt egale
        self.assertNotEqual(self.disciplina, disciplina3)  # ID-urile diferă, deci obiectele sunt diferite

    def test_str(self):
        expected_output = "[101] Disciplina: Matematica | Profesor: Iliescu Vasile"
        self.assertEqual(str(self.disciplina), expected_output)

    def tearDown(self) -> None:
        # Resetarea resurselor (dacă este necesar)
        pass

if __name__ == "__main__":
    unittest.main()
