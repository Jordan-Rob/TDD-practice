
class Student():

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def email(self):
        return "{}.{}@student.utamu.ac".format(self.first, self.last)

    def student_id(self):
        return "{}.{}.12557".format(self.first, self.last)
