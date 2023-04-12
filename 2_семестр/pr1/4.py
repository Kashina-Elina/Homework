class Learner:
    def __init__(self):
        self.classes = []

    def enrol(self, course):
        self.classes.append(course)


class Teacher:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Person:
    def __init__(self, name, surname, number, learner=None, teacher=None):
        self.name = name
        self.surname = surname
        self.number = number

        self.learner = learner
        self.teacher = teacher

    def enrol(self, course):
        if self.learner == None:
            raise Exception("Атрибут не установлен")
        self.learner.enrol(course)

    def assign_teaching(self, course):
        if self.teacher == None:
            raise Exception("Атрибут не установлен")
        self.teacher.assign_teaching(course)


jane = Person("Jane", "Smith", "SMTJNX045", Learner(), Teacher())
jane.enrol('a_postgrad_course')
jane.assign_teaching('an_undergrad_course')