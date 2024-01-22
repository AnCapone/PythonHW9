# Створити ієрархію класів для опису академії.
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
# Продумати архітектуру: реалізувати принципи ООП

class Person:
    __name = "noname"
    __age = 60

    def __init__(self, name, age):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name > 2:
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