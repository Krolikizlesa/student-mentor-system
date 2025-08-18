class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        # Проверяем что лектор - экземпляр класса Lecturer
        if not isinstance(lecturer, Lecturer):
            return "Ошибка: Это не лектор"

        # Проверяем что курс прикреплен к лектору и студент проходит этот курс
        if (course in lecturer.courses_attached and
                course in self.courses_in_progress and
                1 <= grade <= 10):

            # Добавляем оценку лектору
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Словарь для хранения оценок лектора


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (course in self.courses_attached and
                course in student.courses_in_progress):

            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Тестирование по условиям задания
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

# Назначаем курсы
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

# Тестируем выставление оценок
print(student.rate_lecture(lecturer, 'Python', 7))  # Успешно
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка: лектор не прикреплен к Java
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка: студент не проходит С++
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка: reviewer не лектор

print(lecturer.grades)  # {'Python': [7]}

# Дополнительное тестирование из предыдущей версии
best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)

print(best_student.grades)  # {'Python': [10, 9, 8]}

