from employee import Employee

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def get_salary(self):
        return 10000  # Example salary calculation for a manager
