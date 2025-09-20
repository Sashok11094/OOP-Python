from exercise1 import lecturer


class Person:
    def __init__(self, name ,surname):
        self.name = name
        self.surname = surname

class Lecturer(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def add_course(self, course_name):
        if course_name not in self.courses_attached:
            self.courses_attached.append(course_name)

    def rate_lecture(self, student, course, grade):
        print("Преподаватели не оценивают себя")

class Reviewer(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def review_homework(self, student, course, grade):
        pass

class Student(Person):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender
        self.courses_in_progress = []
        self.finished_course = []

    def add_course(self, course_name):
        if course_name not in self.courses_in_progress:
            self.courses_in_progress.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course not in lecturer.grades:
                lecturer.grades[course] = []

            if isinstance(grade, int) and 1 <= grade <= 10:
                lecturer.grades[course].append(grade)
            else:
                raise ValueError("Оценка должна быть числом от 1 до 10")

        elif course not in self.courses_in_progress:
            return f"Ошибка:{self.surname} не проходит курс '{course}'."

        elif course not in lecturer.courses_attached:
            return f"Ошибка:{lecturer.name} не ведет курс '{course}'."

        else:
            return "Ошибка: невозможо поставить оценку!!!"


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))
print(student.rate_lecture(lecturer, 'Java', 8))
print(student.rate_lecture(lecturer, 'С++', 8))
print(student.rate_lecture(reviewer, 'Python', 6))

print(lecturer.grades)


