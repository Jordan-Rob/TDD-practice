import unittest
import student


class TestStudent(unittest.TestCase):

    def test_fullname(self):
        student1 = student.Student('jon', 'snow', 19)
        student2 = student.Student('kayla', 'daniels', 20)

        self.assertEqual(student1.fullname(), 'jon snow')
        self.assertEqual(student2.fullname(), 'kayla daniels')

    def test_email(self):
        student1 = student.Student('jon', 'snow', 19)
        student2 = student.Student('kayla', 'daniels', 20)

        self.assertEqual(student1.email(), 'jon.snow@student.utamu.ac')
        self.assertEqual(student2.email(), 'kayla.daniels@student.utamu.ac')

    def test_student_id(self):
        student1 = student.Student('jon', 'snow', 19)
        student2 = student.Student('kayla', 'daniels', 20)

        self.assertEqual(student1.student_id(), 'jon.snow.12557')
        self.assertEqual(student2.student_id(),
                         'kayla.daniels.12557')


if __name__ == '__main__':
    unittest.main()
