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

    def _avg_grade(self):
        grade_list = []
        for grade in self.grades.values():
            grade_list.extend(grade)
        res = sum(grade_list) / len(grade_list)
        return round(res, 1)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n' \
              f'Средняя оценка за домашние задания: {self._avg_grade()} \n' \
              f'Курсы в процессе обучения: {", ".join(self.courses_in_progress)} \n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)} \n'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _avg_grade(self):
        grade_list = []
        for grade in self.grades.values():
            grade_list.extend(grade)
        res = sum(grade_list) / len(grade_list)
        return round(res, 1)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n' \
              f'Средняя оценка за лекции: {self._avg_grade()} \n'
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self._avg_grade() < other._avg_grade()
        elif isinstance(other, Student):
            return self._avg_grade() < other._avg_grade()
        else:
            return 'Нужно сравнивать либо лекторов либо студентов!'


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

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n'
        return res


best_student = Student('Ruoy', 'Eman', 'male')
good_student = Student('Vasya', 'Pupkin', 'male')
best_student.courses_in_progress += ['Python']
good_student.courses_in_progress += ['Python', 'Git']
good_student.finished_courses += ['Введение в Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_reviewer = Reviewer('some', 'body')
cool_reviewer.courses_attached += ['Python', 'Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(good_student, 'Python', 10)
cool_reviewer.rate_hw(good_student, 'Git', 10)
cool_reviewer.rate_hw(good_student, 'Git', 7)
cool_reviewer.rate_hw(good_student, 'Python', 9)

first_lector = Lecturer('Petr', 'Petrovich')
second_lector = Lecturer('Ivan', 'Ivanovich')
best_student.rate_lection(first_lector, 'Python', 8)
best_student.rate_lection(first_lector, 'Python', 9)
good_student.rate_lection(second_lector, 'Python', 10)
good_student.rate_lection(second_lector, 'Git', 9)
good_student.rate_lection(second_lector, 'Git', 7)


def avg_grades(some_list, course, sum_grade=0, i=0):
    for person in some_list:
        if course in person.grades:
            for grade in person.grades[course]:
                sum_grade += grade
                i += 1
            av = round(sum_grade / i, 1)
            if isinstance(some_list[0], Student):
                res = f'Средняя оценка у студентов по курсу {course}: {av}'
                return res
            elif isinstance(some_list[0], Lecturer):
                res = f'Средняя оценка у лекторов по курсу {course}: {av}'
                return res
    return 'Такого курса нет!'


students = [best_student, good_student]
lectors = [first_lector, second_lector]
print(avg_grades(students, 'Python'))
print(avg_grades(lectors, 'Git'))
print()

print(good_student)
print(best_student)
print(first_lector)
print(second_lector)
print(first_lector < second_lector)
