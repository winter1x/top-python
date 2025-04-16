"""
Студент
имя
возраст
список оценок

добавление оценки в список
средний балл
получение имени

Курс
название
описание
список студентов

добавление студента на курс
получить студентов
о курсе


Преподаватель
имя
список курсов

добавление курса
список курсов
инфо
"""
from online.outType import student


class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)

    def get_average(self):
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)
        return 0

    def get_name(self):
        return self.__name

class Course:
    def __init__(self, title, description):
        self.__title = title
        self.__description = description
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def get_students(self):
        return [student.get_name() for student in self.__students]

    def get_course_info(self):
        return f"курс: {self.__title}\nОписание: {self.__description}"

class Teacher:
    def __init__(self, name):
        self.__name = name
        self.__courses = []

    def add_course(self, course):
        self.__courses.append(course)

    def get_courses(self):
        return [course.get_course_info() for course in self.__courses]

    def get_teacher_info(self):
        return f"преп {self.__name}"

student = Student("иван", 20)
course = Course("math", 'math')
teacher = Teacher('иванов')
teacher.add_course(course)
course.add_student(student)

print(teacher.get_teacher_info())
print(course.get_students())