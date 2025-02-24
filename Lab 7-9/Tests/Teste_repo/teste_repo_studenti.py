"""
from Domain.student import Student
from Repository.repo_studenti import StudentMemoryRepository


def test_store_repo_student():
    repo = StudentMemoryRepository()
    assert repo.size() == 0

    student1 = Student(1, "Ionescu")
    repo.store(student1)
    assert repo.size() == 1

    # Test duplicat (ar trebui să arunce eroare)
    try:
        repo.store(student1)
        assert False
    except ValueError:
        assert True

    assert repo.size() == 1

    student2 = Student(2, "Popescu")
    repo.store(student2)
    assert repo.size() == 2


def test_find_repo_student():
    repo = StudentMemoryRepository()

    student1 = Student(1, "Ionescu")
    student2 = Student(2, "Popescu")

    repo.store(student1)
    repo.store(student2)

    # Găsim studentul după ID
    found_student = repo.find(1)
    assert found_student is not None
    assert found_student.get_nume() == "Ionescu"

    # Nu găsim studentul pentru un ID inexistent
    assert repo.find(3) is None


def test_update_repo_student():
    repo = StudentMemoryRepository()

    student1 = Student(1, "Ionescu")
    repo.store(student1)

    # Actualizăm studentul
    student_updated = Student(1, "Ionescu Alexandru")
    repo.update(student_updated)

    found_student = repo.find(1)
    assert found_student is not None
    assert found_student.get_nume() == "Ionescu Alexandru"

    # Încercăm să actualizăm un student care nu există
    try:
        repo.update(Student(2, "Popescu"))
        assert False
    except ValueError:
        assert True


def test_delete_repo_student():
    repo = StudentMemoryRepository()

    student1 = Student(1, "Ionescu")
    student2 = Student(2, "Popescu")

    repo.store(student1)
    repo.store(student2)
    assert repo.size() == 2

    # Ștergem un student existent
    repo.delete(student1)
    assert repo.size() == 1
    assert repo.find(1) is None

    # Încercăm să ștergem un student care nu există
    try:
        repo.delete(student1)
        assert False
    except ValueError:
        assert True

    assert repo.size() == 1


def test_get_all_repo_student():
    repo = StudentMemoryRepository()

    student1 = Student(1, "Ionescu")
    student2 = Student(2, "Popescu")

    repo.store(student1)
    repo.store(student2)

    all_students = repo.get_all()
    assert len(all_students) == 2
    assert all_students[0].get_nume() == "Ionescu"
    assert all_students[1].get_nume() == "Popescu"
    """
import unittest
import os
from Domain.student import Student
from Repository.repo_studenti import StudentRepoFile


class TestStudentRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        # Create a test file for the repository
        self.test_filename = "test_studenti.txt"
        with open(self.test_filename, "w") as f:
            f.write("10101, Florea Rares\n")
            f.write("12321, Armeana Medeea\n")

        self.repo = StudentRepoFile(self.test_filename)

    def test_load_from_file(self):
        studenti = self.repo.get_all()
        self.assertEqual(len(studenti), 2)
        self.assertEqual(studenti[0].get_IDstudent(), 10101)
        self.assertEqual(studenti[0].get_nume(), " Florea Rares")
        self.assertEqual(studenti[1].get_IDstudent(), 12321)
        self.assertEqual(studenti[1].get_nume(), " Armeana Medeea")

    def test_store(self):
        initial_size = self.repo.size()
        new_student = Student(12345, " Popescu Dan")
        self.repo.store(new_student)

        self.assertEqual(self.repo.size(), initial_size + 1)
        stored_student = self.repo.find(12345)
        self.assertIsNotNone(stored_student)
        self.assertEqual(stored_student.get_nume(), "  Popescu Dan")

        # Test storing a student with an existing ID
        with self.assertRaises(ValueError):
            self.repo.store(Student(12345, "Popescu Maria"))

    def test_update(self):
        updated_student = Student(10101, "Florea Mihai")
        self.repo.update(updated_student)

        student = self.repo.find(10101)
        self.assertIsNotNone(student)
        self.assertEqual(student.get_nume(), " Florea Mihai")

        # Updatam un student care nu exista
        with self.assertRaises(ValueError):
            self.repo.update(Student(99999, "Vasile Ioan"))

    def test_find(self):
        student = self.repo.find(12321)
        self.assertIsNotNone(student)
        self.assertEqual(student.get_nume(), " Armeana Medeea")

        #Incercam sa gasim un student care nu exista
        student = self.repo.find(99999)
        self.assertIsNone(student)

    def test_delete(self):
        initial_size = self.repo.size()
        student_to_delete = Student(10101, "Florea Rares")


        #incercam sa stergem un student care nu exista
        with self.assertRaises(ValueError):
            self.repo.delete(Student(99999, "Vasile Ioan"))

    def test_fill_studenti(self):
        self.repo.fill_studenti()
        studenti = self.repo.get_all()
        self.assertGreater(len(studenti), 0)

    def test_get_all(self):
        studenti = self.repo.get_all()
        self.assertEqual(len(studenti), 2)

    def test_size(self):
        size = self.repo.size()
        self.assertEqual(size, 2)

    def tearDown(self) -> None:
        #curatam test file
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    if __name__ == "__main__":
        unittest.main()