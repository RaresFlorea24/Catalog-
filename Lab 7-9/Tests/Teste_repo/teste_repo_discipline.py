
"""
def test_store_repo():
    repo = DisciplinaMemoryRepository()
    assert repo.get_size() == 0

    d1 = Disciplina(1, "Matematica", "Popescu")
    repo.store(d1)
    assert repo.get_size() == 1

    d2 = Disciplina(1, "Fizica", "Ionescu")
    try:
        repo.store(d2)
        assert False
    except ValueError:
        assert True

    assert repo.get_size() == 1

    d3 = Disciplina(2, "Informatica", "Georgescu")
    repo.store(d3)
    assert repo.get_size() == 2


def test_update_repo():
    repo = DisciplinaMemoryRepository()
    assert repo.get_size() == 0

    d1 = Disciplina(1, "Matematica", "Popescu")
    try:
        repo.update(d1)
        assert False
    except ValueError:
        assert True

    repo.store(d1)
    assert repo.get_size() == 1

    d_updated = Disciplina(1, "Matematica Avansata", "Popescu")
    repo.update(d_updated)

    d_found = repo.find(1)
    assert d_found.get_nume() == "Matematica Avansata"
    assert d_found.get_profesor() == "Popescu"

    d_invalid = Disciplina(3, "Chimie", "Vasilescu")
    try:
        repo.update(d_invalid)
        assert False
    except ValueError:
        assert True
    assert repo.get_size() == 1


def test_find_repo():
    repo = DisciplinaMemoryRepository()
    assert repo.get_size() == 0
    assert repo.find(1) is None

    d1 = Disciplina(1, "Matematica", "Popescu")
    d2 = Disciplina(2, "Fizica", "Ionescu")
    d3 = Disciplina(3, "Chimie", "Vasilescu")

    repo.store(d1)
    repo.store(d2)
    repo.store(d3)

    assert repo.get_size() == 3

    d1_found = repo.find(1)
    assert d1_found.get_nume() == "Matematica"
    assert d1_found.get_profesor() == "Popescu"

    d4_found = repo.find(4)
    assert d4_found is None


def test_delete_repo():
    repo = DisciplinaMemoryRepository()
    d1 = Disciplina(1, "Matematica", "Popescu")
    d2 = Disciplina(2, "Fizica", "Ionescu")

    repo.store(d1)
    repo.store(d2)
    assert repo.get_size() == 2

    repo.delete(d1)
    assert repo.get_size() == 1
    assert repo.find(1) is None

    try:
        repo.delete(d1)
        assert False
    except ValueError:
        assert True

    assert repo.get_size() == 1


def test_get_all_repo():
    repo = DisciplinaMemoryRepository()
    d1 = Disciplina(1, "Matematica", "Popescu")
    d2 = Disciplina(2, "Fizica", "Ionescu")

    repo.store(d1)
    repo.store(d2)

    all_disciplines = repo.get_all()
    assert len(all_disciplines) == 2
    assert all_disciplines[0].get_nume() == "Matematica"
    assert all_disciplines[1].get_nume() == "Fizica"
    """
import unittest
import os
from Domain.disciplina import Disciplina
from Repository.repo_discipline import DisciplineRepoFile


class TestDisciplineRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.test_filename = "test_discipline.txt"
        with open(self.test_filename, "w") as f:
            f.write("101,Matematica,Iliescu Vasile\n")
            f.write("102,Informatica,Simion George\n")

        self.repo = DisciplineRepoFile(self.test_filename)

    def test_load_from_file(self):
        discipline = self.repo.get_all()
        self.assertEqual(len(discipline), 2)
        self.assertEqual(discipline[0].get_idDisciplina(), 101)
        self.assertEqual(discipline[0].get_nume(), "Matematica")
        self.assertEqual(discipline[0].get_profesor(), "Iliescu Vasile")
        self.assertEqual(discipline[1].get_idDisciplina(), 102)
        self.assertEqual(discipline[1].get_nume(), "Informatica")
        self.assertEqual(discipline[1].get_profesor(), "Simion George")

    def test_store(self):
        initial_size = self.repo.get_size()
        new_disciplina = Disciplina(103, "Fizica", "Popescu Ion")
        self.repo.store(new_disciplina)

        self.assertEqual(self.repo.get_size(), initial_size + 1)
        stored_disciplina = self.repo.find(103)
        self.assertIsNotNone(stored_disciplina)
        self.assertEqual(stored_disciplina.get_nume(), " Fizica")
        self.assertEqual(stored_disciplina.get_profesor(), " Popescu Ion")

        with self.assertRaises(ValueError):
            self.repo.store(Disciplina(103, "Chimie", "Ionescu Maria"))

    def test_update(self):
        updated_disciplina = Disciplina(101, " Algebra", "Iliescu Mihai")
        self.repo.update(updated_disciplina)

        disciplina = self.repo.find(101)
        self.assertIsNotNone(disciplina)
        self.assertEqual(disciplina.get_nume(), "  Algebra")
        self.assertEqual(disciplina.get_profesor(), " Iliescu Mihai")

        #Update la o disciplina care nu exista
        with self.assertRaises(ValueError):
            self.repo.update(Disciplina(999, "Biologie", "Vasilescu Ioan"))

    def test_find(self):
        disciplina = self.repo.find(102)
        self.assertIsNotNone(disciplina)
        self.assertEqual(disciplina.get_nume(), "Informatica")
        self.assertEqual(disciplina.get_profesor(), "Simion George")

        #Find la o disciplina care nu exista
        disciplina = self.repo.find(999)
        self.assertIsNone(disciplina)

    def test_delete(self):
        initial_size = self.repo.get_size()
        disciplina_to_delete = Disciplina(101, "Matematica", "Iliescu Vasile")
        self.repo.delete(disciplina_to_delete)


        # Sterg o disciplina care nu exista
        with self.assertRaises(ValueError):
            self.repo.delete(Disciplina(999, "Biologie", "Vasilescu Ioan"))

    def test_fill_discipline(self):
        self.repo.fill_discipline()
        discipline = self.repo.get_all()
        self.assertGreater(len(discipline), 0)

    def test_get_all(self):
        discipline = self.repo.get_all()
        self.assertEqual(len(discipline), 2)

    def test_get_size(self):
        size = self.repo.get_size()
        self.assertEqual(size, 2)

    def run_tests_repo_disciplina(self):
        self.setUp()
        self.test_find()
        self.test_store()
        self.test_load_from_file()
        self.test_delete()
        self.test_update()
        self.test_get_size()
        self.tearDown()

    def tearDown(self) -> None:
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    if __name__ == "__main__":
        unittest.main()

