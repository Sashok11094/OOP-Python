class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def attach_course(self, course):
        if course not in self.courses_attached:
            self.courses_attached.append(course)

    def detach_course(self, course):
        if course in self.courses_attached:
            self.courses_attached.remove(course)

class Lecturer(Mentor):
    pass
class Reviewer(Mentor):
    pass

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Петр', 'Петров')

print(isinstance(lecturer, Mentor))
print(isinstance(reviewer, Mentor))
print(lecturer.courses_attached)
print(reviewer.courses_attached)

