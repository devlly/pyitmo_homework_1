class Course():
    all_crs = {}
    def __init__(self, name, teacher=None, students=None, grades=None, st_grades=None):
        self.name = name
        self.grades = {}
        self.st_grades = []
        # if aud not None:
        #     self.aud = aud
        if teacher not None:
            self.teacher = teacher
        if students is None:
            self.students = []
        else:
            self.students = students

        Course.all_crs[self.name] = self.teacher, self.st_grades


    def add_teacher(self, tch):
        if tch is not self.teacher:
            self.teacher = tch
            Course.all_crs.update


    def add_students(self, st):
        if st not in self.students:
            self.students.append(st)
            all_crs.update(self.name = )

    def add_grades(self, st, gr):
        if st in self.students:
            self.grades[st]= self.st_grades.append(gr) '''gonna mix all grades for all student in same lst???'''

    def find_teacher(self):
        return self.teacher


    def update_info(self):
        Course.all_crs[self.name] = self.aud, self.teacher, self.st_grades

    def find_crs_by_tch(self, fullname):
        if fullname in all_crs[values]:
            yield all_crs[key]
        for fullname in all_crs.values:
            return '''something to find and print key by part of value'''



class Human():
    def __init__(self, name, last):
        self.name = name
        self.last = last

class Teacher(Human):
    lst = []
    def __init__(self, name, last, courses=None):
        super().__init__(name, last)
        Teacher.lst.append(name + last)
        # if courses is None:
        #     self.courses = []
        # else:
        #     self.course = courses


    def add_course(self, course):
        if course not in courses:
            self.courses.append(course)

class Student(Human):
    # def __init__(self, st_grades=None):
    #     self.st_grades = {}
    #
    # def add_grades(self, crs, gr):




#maybe class Grades
