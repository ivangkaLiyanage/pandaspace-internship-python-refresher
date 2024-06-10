class Person():
    def __init__(self, name, age, contactNumber):
        self.name = name
        self.age = age
        self.contactNumber = contactNumber

    def salaryCalculate(self):
        print(f'Salary for {self.name} of {self.age} age with contact number {self.contactNumber} is LKR {self.salary}')


class Manager(Person):
    def __init__(self, name, age, contactNumber, salary):
        super().__init__(name, age, contactNumber)
        self.salary = salary

class FloorWorker(Person):
    def __init__(self, name, age, contactNumber, salary):
        super().__init__(name,age,contactNumber)
        self.salary = salary

class SalesExecutive(Person):
    pass