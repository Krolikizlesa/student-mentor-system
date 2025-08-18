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


# Тестирование
# Создаем лекторов
lecturer1 = Lecturer("Иван", "Иванов")
lecturer1.courses_attached += ["Python"]
lecturer2 = Lecturer("Петр", "Петров")
lecturer2.courses_attached += ["Python"]

# Создаем проверяющих
reviewer = Reviewer("Сидор", "Сидоров")
reviewer.courses_attached += ["Python"]

# Создаем студентов
student1 = Student("Анна", "Кузнецова", "ж")
student1.courses_in_progress += ["Python"]
student1.finished_courses += ["Введение в программирование"]

student2 = Student("Дмитрий", "Смирнов", "м")
student2.courses_in_progress += ["Python"]
student2.finished_courses += ["Git"]

# Лекторы получают оценки
student1.rate_lecture(lecturer1, "Python", 9)
student1.rate_lecture(lecturer1, "Python", 8)
student2.rate_lecture(lecturer1, "Python", 10)

student1.rate_lecture(lecturer2, "Python", 7)
student2.rate_lecture(lecturer2, "Python", 9)

# Студенты получают оценки за ДЗ
reviewer.rate_hw(student1, "Python", 10)
reviewer.rate_hw(student1, "Python", 9)
reviewer.rate_hw(student1, "Python", 8)

reviewer.rate_hw(student2, "Python", 7)
reviewer.rate_hw(student2, "Python", 8)
reviewer.rate_hw(student2, "Python", 9)

# Вывод информации
print("=" * 50)
print(reviewer)
print("=" * 50)
print(lecturer1)
print("=" * 50)
print(lecturer2)
print("=" * 50)
print(student1)
print("=" * 50)
print(student2)
print("=" * 50)

# Сравнение
print(f"Средняя оценка лектора {lecturer1.surname}: {lecturer1.avg_grade():.1f}")
print(f"Средняя оценка лектора {lecturer2.surname}: {lecturer2.avg_grade():.1f}")
print(f"Лектор1 > Лектор2: {lecturer1 > lecturer2}")
print(f"Лектор1 == Лектор2: {lecturer1 == lecturer2}")

print(f"\nСредняя оценка студента {student1.surname}: {student1.avg_grade():.1f}")
print(f"Средняя оценка студента {student2.surname}: {student2.avg_grade():.1f}")
print(f"Студент1 < Студент2: {student1 < student2}")
print(f"Студент1 == Студент2: {student1 == student2}")