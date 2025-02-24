import unittest
import os
from Domain.student import Student
from Domain.validation import ValidatorStudent
from Repository.repo_studenti import StudentRepoFile
from Service.student_controller import ServiceStudent


class TestServiceStudent(unittest.TestCase):
    def setUp(self) -> None:
        """
        Sets up test files and initializes the necessary repository and service.
        """
        # Test file
        self.test_file_studenti = "test_studenti_service.txt"

        # Populate test student file
        with open(self.test_file_studenti, "w") as f:
            f.write("10101, Florea Rares\n")
            f.write("12321, Armeana Medeea\n")

        # Initialize repository and validator
        self.repo = StudentRepoFile(self.test_file_studenti)
        self.validator = ValidatorStudent()
        self.service = ServiceStudent(self.repo, self.validator)

    def test_adauga_student(self):
        """
        Test adding a new student.
        """
        initial_size = len(self.service.get_all())

        # Add a valid student
        self.service.adauga_student(12345, "Popescu Dan")
        self.assertEqual(len(self.service.get_all()), initial_size + 1)

        # Test adding a duplicate student
        with self.assertRaises(ValueError):
            self.service.adauga_student(12345, "Popescu Dan")

        # Test adding a student with invalid data
        with self.assertRaises(ValueError):
            self.service.adauga_student(-1, "")

    def test_actualizeaza_student(self):
        """
        Test updating an existing student.
        """
        # Update existing student
        self.service.actualizeaza_student(12321, "Florea Medeea")
        updated_student = self.service.find_student(12321)
        self.assertIsNotNone(updated_student)
        self.assertEqual(updated_student.get_nume().strip(), "Florea Medeea")

        # Update a non-existent student
        with self.assertRaises(ValueError):
            self.service.actualizeaza_student(99999, "Buta Pavel")

    def test_find_student(self):
        """
        Test finding a student by ID.
        """
        student = self.service.find_student(10101)
        self.assertIsNotNone(student)
        self.assertEqual(student.get_nume().strip(), "Florea Rares")

        # Find a non-existent student
        student = self.service.find_student(99999)
        self.assertIsNone(student)

    def test_delete_student(self):
        """
        Test deleting a student.
        """
        initial_size = len(self.service.get_all())

        # Delete existing student
        self.service.delete_student(10101)
        self.assertEqual(len(self.service.get_all()), initial_size - 1)

    def test_fill_studenti(self):
        """
        Test filling the repository with random students.
        """
        self.service.fill_studenti()
        self.assertGreater(len(self.service.get_all()), 0)

    def test_add_default(self):

        initial_size = len(self.service.get_all())
        self.service.add_default()
        self.assertEqual(len(self.service.get_all()), initial_size + 5)

    def test_get_all(self):
        """
        Test retrieving all students.
        """
        all_students = self.service.get_all()
        self.assertEqual(len(all_students), 2)

        # Check student data
        self.assertEqual(all_students[0].get_IDstudent(), 10101)
        self.assertEqual(all_students[1].get_nume().strip(), "Armeana Medeea")

    def tearDown(self) -> None:
        """
        Cleans up the test file after the tests.
        """
        if os.path.exists(self.test_file_studenti):
            os.remove(self.test_file_studenti)

    if __name__ == "__main__":
        unittest.main()
