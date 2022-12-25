students_list = []
lecturers_list = []


class Student:
    def __init__(self, name, surname, gender, lst=students_list):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        lst.append(self)

    def feedback(self, teacher, course, grade):
        if isinstance(teacher, Lecturer) and course in self.courses_in_progress and course in teacher.courses_attached:
            if course in teacher.lecture_grades:
                teacher.lecture_grades[course] += [grade]
            else:
                teacher.lecture_grades[course] = [grade]
        else:
            print("Error in the evaluation of the lecturer \n")

    def average_mark(self):
        if self.grades != {}:
            grades = []
            for course in self.grades:
                grades += list(self.grades[course])
            average = sum(grades) / len(grades)
            return average
        else:
            return 'Student without marks \n'

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашние задания: {self.average_mark()} \n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)} \n'

    def __lt__(self, other):
        if isinstance(other, Student):
            if type(self.average_mark()) == str or type(other.average_mark()) == str:
                print('One student without mark \n')
                return
            else:
                return self.average_mark() < other.average_mark()
        else:
            print('One person is not a student \n')
            return


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, lst=lecturers_list):
        super().__init__(name, surname)
        self.lecture_grades = {}
        lst.append(self)

    def average_mark(self):
        if self.lecture_grades != {}:
            grades = []
            for course_marks in list(self.lecture_grades.values()):
                grades += course_marks
            average = sum(grades) / len(grades)
            return average
        else:
            return 'Without marks'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \n' \
               f'Средняя оценка за лекции: {self.average_mark()} \n'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if type(self.average_mark()) == str or type(other.average_mark()) == str:
                print('One lecturer without mark \n')
                return
            else:
                return self.average_mark() < other.average_mark()
        else:
            print('One person is not a lecturer \n')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
                and course in student.courses_in_progress and 0 < grade <= 10
                and type(grade) == int):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка \n'

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n'


def student_course_average(students, course):
    marks = []
    for stud in students:
        if course in list(stud.grades.keys()):
            marks += stud.grades[course]
    if len(marks) != 0:
        average = sum(marks) / len(marks)
        print(f"Students' average mark of {course}:", average)
        return average
    else:
        print('Without mark \n')
        return


def lecturer_course_average(lecturers, course):
    marks = []
    for teacher in lecturers:
        if course in teacher.courses_attached:
            marks.extend(teacher.lecture_grades[course])
    if len(marks) != 0:
        average = sum(marks) / len(marks)
        print(f"Lecturers' average mark of {course}:", average)
        return average
    else:
        print('Without mark \n')
        return


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Math']

son_of_rector = Student('Mark', 'Spencer', 'male')
son_of_rector.courses_in_progress += ['Python']
son_of_rector.courses_in_progress += ['Git']
son_of_rector.courses_in_progress += ['Math']
son_of_rector.courses_in_progress += ['Geometry']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

maths_lecturer = Lecturer('Gregory', 'Perelman')
maths_lecturer.courses_attached += ['Math']
maths_lecturer.courses_attached += ['Geometry']
maths_lecturer.courses_attached += ['Git']

examinator_python = Reviewer('Alex', 'Black')
examinator_python.courses_attached += ['Python']

examinator_git = Reviewer('Robert', 'Newman')
examinator_git.courses_attached += ['Git']

best_student.feedback(cool_lecturer, 'Python', 9)
best_student.feedback(cool_lecturer, 'Git', 6)
best_student.feedback(maths_lecturer, 'Git', 7)

son_of_rector.feedback(maths_lecturer, 'Math', 10)
son_of_rector.feedback(maths_lecturer, 'Geometry', 10)
son_of_rector.feedback(maths_lecturer, 'Git', 10)

examinator_python.rate_hw(best_student, 'Python', 9)
examinator_python.rate_hw(best_student, 'Python', 8)
examinator_python.rate_hw(son_of_rector, 'Python', 10)
examinator_python.rate_hw(son_of_rector, 'Python', 10)

examinator_git.rate_hw(best_student, 'Git', 6)
examinator_git.rate_hw(son_of_rector, 'Git', 10)

print('Лучший студент:', best_student, sep='\n')
print('Сын ректора:', son_of_rector, sep='\n')
print(cool_lecturer)
print(maths_lecturer)
print(examinator_python)
print(examinator_git)

print(best_student < son_of_rector)
print(cool_lecturer < maths_lecturer)

student_course_average(students_list, 'Python')
lecturer_course_average(lecturers_list, 'Git')
