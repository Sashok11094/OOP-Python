class  Person:
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


def average_homework_grade_for_course(students, course):
    all_grades = []
    for student in students:
        if course in student.homework_grades:
            all_grades.extend(student.homework_grades[course])
    return sum(all_grades) / len(all_grades) if all_grades else 0

def average_lecture_grade_for_course(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    return sum(all_grades) / len(all_grades) if all_grades else 0


reviewer1 = Reviewer('Ivan', 'Ivanov')
reviewer2 = Reviewer('Maria', 'Petrova')

lecturer1 = Lecturer('Petr', 'Petrov')
lecturer1.grades['Python'] = [10, 9, 10]
lecturer1.grades['JavaScript'] = [8, 9, 9]

lecturer2 = Lecturer('Anna', 'Sidorova')
lecturer2.grades['Python'] = [9, 8, 10]
lecturer2.grades['Git'] = [10, 10, 9]

student1 = Student('Oleg', 'Kozlov', 'male')
student1.courses_in_progress = ['Python', 'Git']
student1.finished_course = ['Введение в программирование']
student1.homework_grades['Python'] = [9, 9, 10]
student1.homework_grades['Git'] = [8, 9, 8]

student2 = Student('Elena', 'Volkova', 'female')
student2.courses_in_progress = ['JavaScript', 'Python']
student2.finished_course = ['HTML/CSS']
student2.homework_grades['Python'] = [10, 8, 9]
student2.homework_grades['JavaScript'] = [9, 9, 8]

print("=== РЕЦЕНЗЕНТЫ ===")
print(reviewer1)
print()
print(reviewer2)
print()

print("=== ЛЕКТОРЫ ===")
print(lecturer1)
print()
print(lecturer2)
print()

print("=== СТУДЕНТЫ ===")
print(student1)
print()
print(student2)
print()

print("=== СРАВНЕНИЕ ЛЕКТОРОВ ===")
print(f"{lecturer1.name} > {lecturer2.name}: {lecturer1 > lecturer2}")
print(f"{lecturer1.name} < {lecturer2.name}: {lecturer1 < lecturer2}")
print(f"{lecturer1.name} == {lecturer2.name}: {lecturer1 == lecturer2}")
print()

print("=== СРАВНЕНИЕ СТУДЕНТОВ ===")
print(f"{student1.name} > {student2.name}: {student1 > student2}")
print(f"{student1.name} < {student2.name}: {student1 < student2}")
print(f"{student1.name} == {student2.name}: {student1 == student2}")
print()

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print("=== СРЕДНИЕ ОЦЕНКИ ПО КУРСАМ ===")
print(f"Средняя оценка за домашние задания по Python: {average_homework_grade_for_course(students_list, 'Python'):.2f}")
print(f"Средняя оценка за домашние задания по JavaScript: {average_homework_grade_for_course(students_list, 'JavaScript'):.2f}")
print(f"Средняя оценка за лекции по Python: {average_lecture_grade_for_course(lecturers_list, 'Python'):.2f}")
print(f"Средняя оценка за лекции по Git: {average_lecture_grade_for_course(lecturers_list, 'Git'):.2f}")