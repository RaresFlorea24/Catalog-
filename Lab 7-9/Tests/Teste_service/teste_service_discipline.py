import unittest
import os
from Domain.disciplina import Disciplina
from Domain.validation import ValidatorDisciplina
from Repository.repo_discipline import DisciplineRepoFile
from Service.disciplina_controller import ServiceDisciplina


class TestServiceDisciplina(unittest.TestCase):
    def setUp(self) -> None:

        self.test_filename = "test_discipline_service.txt"
        with open(self.test_filename, "w") as f:
            f.write("101, Matematica, Iliescu Vasile\n")
            f.write("102, Informatica, Simion George\n")
            f.write("103, Limba romana, Dancila Viorel\n")

        self.repo = DisciplineRepoFile(self.test_filename)
        self.validator = ValidatorDisciplina()
        self.service = ServiceDisciplina(self.repo, self.validator)

    def test_adauga_disciplina(self):
        initial_size = len(self.service.get_all())
        self.service.adauga_disciplina(104, "Fizica", "Popescu Maria")
        self.assertEqual(len(self.service.get_all()), initial_size + 1)

        with self.assertRaises(ValueError):
            self.service.adauga_disciplina(101, "Chimie", "Ionescu Mihai")


    def test_actualizeaza_disciplina(self):

        self.service.actualizeaza_disciplina(101, "Geometrie", "Stanescu Dan")
        disciplina = self.service.find_disciplina(101)

        self.assertIsNotNone(disciplina)
        self.assertEqual(disciplina.get_nume().strip(), "Geometrie")
        self.assertEqual(disciplina.get_profesor().strip(), "Stanescu Dan")

        with self.assertRaises(ValueError):
            self.service.actualizeaza_disciplina(999, "Biologie", "Popescu Ioana")

    def test_find_disciplina(self):

        disciplina = self.service.find_disciplina(102)
        self.assertIsNotNone(disciplina)
        self.assertEqual(disciplina.get_nume().strip(), "Informatica")

        disciplina = self.service.find_disciplina(999)
        self.assertIsNone(disciplina)

    def test_delete_disciplina(self):


        # Test deleting a non-existent discipline
        with self.assertRaises(ValueError):
            self.service.delete_disciplina(999, "Istorie", "Ion Pop")

    def test_get_all(self):

        all_discipline = self.service.get_all()
        self.assertEqual(len(all_discipline), 3)

        expected_names = ["Matematica", "Informatica", "Limba romana"]
        self.assertListEqual([d.get_nume().strip() for d in all_discipline], expected_names)

    def test_fill_discipline(self):

        self.service.fill_discipline()
        all_discipline = self.service.get_all()
        self.assertGreater(len(all_discipline), 0)

    def tearDown(self) -> None:

        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

if __name__ == "__main__":
    unittest.main()