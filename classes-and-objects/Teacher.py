# class Student():
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades

#     def averageGrade(self):
#         avg = 0
#         for grade in self.grades:
#             avg += grade
#         averageValue = "{:.2f}".format(avg/len(self.grades))

#         print(f'{"Average grade of student "}{self.name}{" is "}{averageValue}')




# inheritence
class Teacher():
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def averageGrade(self):
        avg = 0
        for grade in self.grades:
            avg += grade
        averageValue = "{:.2f}".format(avg/len(self.grades))
        return averageValue


class Student(Teacher):
    def display(self):
        avg = self.averageGrade()
        print(f'{"Average grade of student "}{self.name}{" is "}{avg}')




