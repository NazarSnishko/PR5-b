class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, new_name):
        self.name = new_name

class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# Приклад використання
student1 = Student("Максим", 20, "Київський університет")
print("Ім'я:", student1.name)
print("Вік:", student1.age)
print("Університет:", student1.university)

student1.add_grade(90)
student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(100)


print("Список оцінок:", student1.grades)
print("Середня оцінка:", student1.average_grade())

student1.change_name("Марія")
print("Нове ім'я:", student1.name)
