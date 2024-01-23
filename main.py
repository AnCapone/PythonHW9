# Створити ієрархію класів для опису академії.
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
# Продумати архітектуру: реалізувати принципи ООП
import re


class Person:
    __name = "noname"
    __age = 60

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 2:
            self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 18:
            self.__age = age

    def show_info(self):
        print(f"This person's name is {self.name}. {self.age} years old.")


class Subject:
    __name = "noname"

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 2:
            self.__name = name


class Teacher(Person):

    def __init__(self, name, age, subj: Subject):
        super().__init__(name, age)
        self.__subject = subj

    @property
    def subject(self):
        return self.__subject

    def show_info(self):
        print(f"This teacher's name is {self.name}. {self.age} years old. Teaches {self.subject.name}")


class Student(Person):

    def show_info(self):
        print(f"This student's name is {self.name}. {self.age} years old. Studying in academy")


class Academy:
    __name = "no name"
    students = []
    teachers = []
    subjects = []

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if re.fullmatch(r'\b\w{3,}\b', name):
            self.__name = name

    def add_teacher(self, teacher: Teacher):
        if isinstance(teacher, Teacher):
            self.teachers.append(teacher)

    def add_student(self, student: Student):
        if isinstance(student, Student):
            self.students.append(student)

    def add_subject(self, subject: Subject):
        if isinstance(subject, Subject):
            self.subjects.append(subject)

    def show_teachers(self):
        for teacher in self.teachers:
            print(teacher.name)

    def show_students(self):
        for student in self.students:
            print(student.name)

    def show_subjects(self):
        for subject in self.subjects:
            print(subject.name)

    def show_info(self):
        print(f"Welcome to {self.name}. In our academy teaches {len(self.teachers)} teachers and studying "
              f"{len(self.students)} students.")
        print(f"Teachers of our academy:")
        self.show_teachers()
        print("Students of our academy:")
        self.show_students()
        print("Our subjects:")
        self.show_subjects()


person = Person("Vasya", 25)
person.show_info()
teacher_viktor = Teacher("Viktor", 52, Subject("Mathematics"))
teacher_viktor.show_info()
student_mark = Student("Mark", 19)
student_mark.show_info()
academy = Academy("Python_Academy")
academy.add_student(student_mark)
academy.add_student(Student("Petya", 20))
academy.add_student(Student("Mathew", 18))
academy.add_subject(Subject("Mathematics"))
academy.add_subject(Subject("Physics"))
academy.add_subject(Subject("Literature"))
academy.add_teacher(teacher_viktor)
academy.add_teacher(Teacher("Semen Semenovich", 58, Subject("Physics")))
academy.show_info()
