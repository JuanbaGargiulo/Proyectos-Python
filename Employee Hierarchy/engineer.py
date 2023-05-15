from employee import Employee
class Engineer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language

    def get_salary(self):
        return 8000  # Example salary calculation for an engineer

