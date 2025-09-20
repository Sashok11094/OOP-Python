class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_grade(self):
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self.average_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}'

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()


class Reviewer(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Student(Person):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender
        self.courses_in_progress = []
        self.finished_course = []
        self.homework_grades = {}

    def average_homework_grade(self):
        all_grades = [grade for grades_list in self.homework_grades.values() for grade in grades_list]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_hw_grade = self.average_homework_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_course_str = ', '.join(self.finished_course)
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {avg_hw_grade:.1f}\n'
            f'Курсы в процессе изучения: {courses_in_progress_str}\n'
            f'Завершенные курсы: {finished_course_str}'
        )

    def __lt__(self, other):
        return self.average_homework_grade() < other.average_homework_grade()

    def __gt__(self, other):
        return self.average_homework_grade() > other.average_homework_grade()

    def __eq__(self, other):
        return self.average_homework_grade() == other.average_homework_grade()

    def __le__(self, other):
        return self.average_homework_grade() <= other.average_homework_grade()

    def __ge__(self, other):
        return self.average_homework_grade() >= other.average_homework_grade()

    def __ne__(self, other):
        return self.average_homework_grade() != other.average_homework_grade()


some_reviewer = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.grades['Python'] = [10, 9, 10]

another_lecturer = Lecturer('John', 'Doe')
another_lecturer.grades['JavaScript'] = [8, 9, 7]

some_student = Student('Ruoy', 'Eman', 'male')
some_student.courses_in_progress = ['Python', 'Git']
some_student.finished_course = ['Введение в программирование']
some_student.homework_grades['Python'] = [9, 9, 10]

another_student = Student('Anna', 'Smith', 'female')
another_student.homework_grades['JavaScript'] = [8, 7, 9]

print(some_reviewer)
print()
print(some_lecturer)
print()
print(some_student)
print()


print("Сравнение лекторов:")
print(f"{some_lecturer.name} > {another_lecturer.name}: {some_lecturer > another_lecturer}")
print(f"{some_lecturer.name} < {another_lecturer.name}: {some_lecturer < another_lecturer}")
print(f"{some_lecturer.name} == {another_lecturer.name}: {some_lecturer == another_lecturer}")
print()

print("Сравнение студентов:")
print(f"{some_student.name} > {another_student.name}: {some_student > another_student}")
print(f"{some_student.name} < {another_student.name}: {some_student < another_student}")
print(f"{some_student.name} == {another_student.name}: {some_student == another_student}")
