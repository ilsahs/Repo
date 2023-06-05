class Employee:
    def __init__(self, name, age, id, department):
        if type(name) == int:
            raise Exception("name can not be an integer.")
        self.name = name
        if age < 0:
            raise Exception("ID can not be a negative number.")
        self.age = age
        if id < 0:
            raise Exception("ID can not be a negative number.")
        self.id = id
        self.department = department

class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        for emp in self.employees:
            if emp.id == employee.id:
                raise Exception("Duplicate student ID")
        self.employees.append(employee)

    def show_employee(self,id):
        e = 0
        for emp in self.employees:
            if emp.id == id:
                print(f"Name: {emp.name}, Age: {emp.age}, ID: {emp.id}, Department: {emp.department}")
                e = 1
        if e == 0:
            print("Employee not found")
        
        
    def show_employees(self):
        for employee in self.employees:
            print(f"Name: {employee.name}, Age: {employee.age}, ID: {employee.id}, Department: {employee.department}")

    def delete_employee(self, id):
        for i, employee in enumerate(self.employees):
            if employee.id == id:
                del self.employees[i]
                break
        else:
            raise Exception("Employee not found")

"""
ob = EmployeeManagement()

employee1 = Employee("John",20,1,"HR")
employee2 = Employee("Jack",32,2,"IT")
ob.add_employee(employee1)
ob.add_employee(employee2)
ob.show_employees()
ob.show_employee(1)
"""
