import unittest
import employee_management

class TestEmployeeManagement(unittest.TestCase):

    def test_employee_name(self):
        management = employee_management.EmployeeManagement()
        employee1 = employee_management.Employee(1,21,1,"IT")
        management.add_employee(employee1)
        with self.assertRaises(Exception):
            management.add_employee(employee1)

    def test_employee_ID(self):
        management = employee_management.EmployeeManagement()
        employee1 = employee_management.Employee("John",20,-1,"HR")
        management.add_employee(employee1)
        with self.assertRaises(Exception):
            management.add_employee(employee1)

    def test_employee_Age(self):
        management = employee_management.EmployeeManagement()
        employee1 = employee_management.Employee("John",-20,1,"HR")
        management.add_employee(employee1)
        with self.assertRaises(Exception):
            management.add_employee(employee1)

    def test_add_employee(self):
        management = employee_management.EmployeeManagement()
        employee1 = employee_management.Employee("John",20,1,"HR")
        management.add_employee(employee1)
        self.assertIn(employee1,management.employees)

    def test_duplicate_employee(self):
        management = employee_management.EmployeeManagement()
        employee1 = employee_management.Employee("John",20,1,"HR")
        employee2 = employee_management.Employee("Jane",21,1,"IT")
        management.add_employee(employee1)
        with self.assertRaises(Exception):
            management.add_employee(employee2)

    
    def test_show_employee(self):
        management = employee_management.EmployeeManagement()
        employee1 = employee_management.Employee("John",20,1,"HR")
        employee2 = employee_management.Employee("Jane",21,2,"IT")         
        management.add_employee(employee1)
        management.add_employee(employee2)
        expected_output1 = "Name: John, Age: 20, ID: 1, Department: HR"
        expected_output2 = "Name: Jane, Age: 21, ID: 2, Department: IT"
        expected_output3 = "Employee not found"
        self.assertEqual(expected_output1, self.get_output_string(management.show_employee, 1))
        self.assertEqual(expected_output2, self.get_output_string(management.show_employee, 2))
        self.assertEqual(expected_output3, self.get_output_string(management.show_employee, 4))

    def test_show_employees(self):
        management = employee_management.EmployeeManagement()
        employee1 = employee_management.Employee("John",20,1,"HR")
        employee2 = employee_management.Employee("Jane",21,2,"IT")
        management.add_employee(employee1)
        management.add_employee(employee2)
        expected_output1 = "Name: John, Age: 20, ID: 1, Department: HRName: Jane, Age: 21, ID: 2, Department: IT"
        self.assertEqual(expected_output1, self.get_output_strings(management.show_employees))

    def test_delete_employee(self):
        management = employee_management.EmployeeManagement()
        employee1 = employee_management.Employee("John",20,1,"HR")
        employee2 = employee_management.Employee("Jane",21,2,"IT")
        management.add_employee(employee1)
        management.add_employee(employee2)
        management.delete_employee(2)
        self.assertNotIn(employee2, management.employees)

    def test_delete_missing_employee(self):
        management = employee_management.EmployeeManagement()
        with self.assertRaises(Exception):
            management.delete_employee(1)

    def get_output_string(self, func, param):
        import io
        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            func(param)
        return f.getvalue().replace("\n","")
    
    def get_output_strings(self, func):
        import io
        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            func()
        return f.getvalue().replace("\n","")
    

