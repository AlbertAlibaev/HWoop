class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lection(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'male')
good_student = Student('Vasya', 'Pupkin', 'male')
best_student.courses_in_progress += ['Python']
good_student.courses_in_progress += ['Python', 'Git']

cool_mentor = Mentor('Some', 'Buddy')
cool_reviewer = Reviewer('some', 'body')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)

first_lector = Lecturer('Petr', 'Petrovich')
second_lector = Lecturer('Ivan', 'Ivanovich')
best_student.rate_lection(first_lector, 'Python', 8)
best_student.rate_lection(second_lector, 'Git', 7)

print(best_student.grades)
print(first_lector.grades)
