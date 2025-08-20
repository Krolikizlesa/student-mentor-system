class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return "Ошибка: Это не лектор"
        if (course in lecturer.courses_attached and
                course in self.courses_in_progress and
                1 <= grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def avg_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count > 0 else 0

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.avg_grade():.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count > 0 else 0

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.avg_grade():.1f}")

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()


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

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# Функции для подсчета средних оценок
def average_hw_grade(students, course):
    """Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса"""
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return total / count if count > 0 else 0


def average_lecture_grade(lecturers, course):
    """Подсчет средней оценки за лекции всех лекторов в рамках курса"""
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total / count if count > 0 else 0


# Создаем по 2 экземпляра каждого класса
# Лекторы
lecturer1 = Lecturer("Иван", "Иванов")
lecturer1.courses_attached += ["Python", "Git"]

lecturer2 = Lecturer("Петр", "Петров")
lecturer2.courses_attached += ["Python", "Java"]

# Проверяющие
reviewer1 = Reviewer("Сидор", "Сидоров")
reviewer1.courses_attached += ["Python", "Git"]

reviewer2 = Reviewer("Ольга", "Олеговна")
reviewer2.courses_attached += ["Python", "Java"]

# Студенты
student1 = Student("Анна", "Кузнецова", "ж")
student1.courses_in_progress += ["Python", "Git"]
student1.finished_courses += ["Введение в программирование"]

student2 = Student("Дмитрий", "Смирнов", "м")
student2.courses_in_progress += ["Python", "Java"]
student2.finished_courses += ["Git"]

# Выставляем оценки лекторам
student1.rate_lecture(lecturer1, "Python", 9)
student1.rate_lecture(lecturer1, "Git", 8)
student1.rate_lecture(lecturer2, "Python", 7)

student2.rate_lecture(lecturer1, "Python", 10)
student2.rate_lecture(lecturer2, "Python", 9)
student2.rate_lecture(lecturer2, "Java", 8)

# Выставляем оценки за ДЗ студентам
reviewer1.rate_hw(student1, "Python", 10)
reviewer1.rate_hw(student1, "Python", 9)
reviewer1.rate_hw(student1, "Git", 8)

reviewer2.rate_hw(student2, "Python", 8)
reviewer2.rate_hw(student2, "Python", 7)
reviewer2.rate_hw(student2, "Java", 9)

# Вызываем все созданные методы
print("=" * 50)
print("Информация о проверяющих:")
print(reviewer1)
print("-" * 20)
print(reviewer2)

print("\nИнформация о лекторах:")
print(lecturer1)
print("-" * 20)
print(lecturer2)

print("\nИнформация о студентах:")
print(student1)
print("-" * 20)
print(student2)
print("=" * 50)

# Сравнение студентов и лекторов
print(f"\nСравнение лекторов: {lecturer1.surname} и {lecturer2.surname}")
print(f"Лектор1 > Лектор2: {lecturer1 > lecturer2}")
print(f"Лектор1 == Лектор2: {lecturer1 == lecturer2}")

print(f"\nСравнение студентов: {student1.surname} и {student2.surname}")
print(f"Студент1 < Студент2: {student1 < student2}")
print(f"Студент1 == Студент2: {student1 == student2}")
print("=" * 50)

# Тестируем функции подсчета средних оценок
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print("\nСредние оценки по курсу Python:")
print(f"Средняя оценка за ДЗ: {average_hw_grade(students_list, 'Python'):.1f}")
print(f"Средняя оценка за лекции: {average_lecture_grade(lecturers_list, 'Python'):.1f}")

print("\nСредние оценки по курсу Git:")
print(f"Средняя оценка за ДЗ: {average_hw_grade(students_list, 'Git'):.1f}")
print(f"Средняя оценка за лекции: {average_lecture_grade(lecturers_list, 'Git'):.1f}")

print("\nСредние оценки по курсу Java:")
print(f"Средняя оценка за ДЗ: {average_hw_grade(students_list, 'Java'):.1f}")
print(f"Средняя оценка за лекции: {average_lecture_grade(lecturers_list, 'Java'):.1f}")
