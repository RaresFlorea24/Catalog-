import unittest
from Domain.student import Student

class TestStudent(unittest.TestCase):
    def setUp(self) -> None:

        self.student = Student(12345, "Popescu Dan")

    def test_get_IDstudent(self):

        self.assertEqual(self.student.get_IDstudent(), 12345)

    def test_get_nume(self):

        self.assertEqual(self.student.get_nume(), "Popescu Dan")

    def test_get_medie(self):

        self.assertEqual(self.student.get_medie(), 0)

    def test_set_nume(self):

        self.student.nume("Ion Popescu")
        self.assertEqual(self.student.get_nume(), "Ion Popescu")

    def test_eq(self):

        student2 = Student(12345, "Ion Popescu")  # Are același ID
        self.assertEqual(self.student, student2)

        student3 = Student(54321, "Popescu Dan")  # ID diferit
        self.assertNotEqual(self.student, student3)

    def test_str(self):

        expected_output = "[12345] Student: Popescu Dan"
        self.assertEqual(str(self.student), expected_output)

    def tearDown(self) -> None:

        pass


if __name__ == "__main__":
    unittest.main()
