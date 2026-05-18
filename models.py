class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def __str__(self):
        return f"Person: {self._name}"


class Student(Person):
    def __init__(self, student_id, name):
        super().__init__(name)
        self.__student_id = student_id
        self.grades = {}

    def get_student_id(self):
        return self.__student_id

    def add_grade(self, assignment, score):
        self.grades[assignment] = score

    def get_grades(self):
        return self.grades

    def calculate_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        avg = self.calculate_average()
        return f"ID: {self.__student_id} | Student: {self.get_name()} | Average: {avg:.2f}"