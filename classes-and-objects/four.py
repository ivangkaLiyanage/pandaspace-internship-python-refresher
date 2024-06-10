# create a class called Person - details, salaryCalculate
# create a class called Manager - day salary = 500
# class called floor worker - salary 200
# class called sales executive - salary 300

# Person(name, age, contact number)
# SalesExec(name, age, contact number, value)

from Person import Manager, FloorWorker, SalesExecutive

manager = Manager("James", 26, 77342645, 500)
floorWorker = FloorWorker("Thime", 22, 774569841, 200)
salesExecutive = SalesExecutive("Jessica", 45, 774569812, 100)

manager.salaryCalculate()
floorWorker.salaryCalculate()
salesExecutive.salaryCalculate()